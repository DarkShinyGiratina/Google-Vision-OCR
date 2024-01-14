import os
import sys
import mss
from pynput import mouse
import keyboard
import pyperclip
import google.auth
from tkinter import Tk, Canvas

creds_file = os.environ.get('GOOGLE_APPLICATION_CREDENTIALS')
creds = google.auth.load_credentials_from_file(creds_file)[0] if creds_file else None

root = Tk()


def detect_text(path):
    """Detects text in the file."""
    from google.cloud import vision
    if creds:
        client = vision.ImageAnnotatorClient(credentials=creds)
    else:
        client = vision.ImageAnnotatorClient()

    with open(path, "rb") as image_file:
        content = image_file.read()

    image = vision.Image(content=content)

    response = client.text_detection(image=image)
    texts = response.text_annotations
    if texts:
        return texts[0].description.strip()
    else:
        return "No Text Found"


start_pos = (0, 0)
end_pos = (0, 0)


def on_click(x, y, button, pressed):
    global start_pos, end_pos, root
    if pressed:
        start_pos = (x, y)
    if not pressed:
        end_pos = (x, y)

        smaller_x = min(start_pos[0], end_pos[0])
        bigger_x = max(start_pos[0], end_pos[0])

        smaller_y = min(start_pos[1], end_pos[1])
        bigger_y = max(start_pos[1], end_pos[1])

        if bigger_x - smaller_x == 0 or bigger_y - smaller_y == 0:
            return

        with mss.mss() as sct:
            monitor = {"top": smaller_y, "left": smaller_x,
                       "width": bigger_x - smaller_x, "height": bigger_y - smaller_y}
            sct_img = sct.grab(monitor)
            mss.tools.to_png(sct_img.rgb, sct_img.size, output="to_ocr.png")
        ocr_output = detect_text("to_ocr.png")
        pyperclip.copy(ocr_output)
        # Stop listener
        print('"' + ocr_output + '"' + " copied to clipboard!")
        return False


def make_gui():
    global root
    root = Tk()
    root.attributes("-fullscreen", True, '-topmost', True, "-alpha", 0.3)
    root["bg"] = "grey"
    start_x = start_y = 0
    rect = -1

    def on_click(event):
        nonlocal rect, start_x, start_y
        start_x, start_y = (event.x, event.y)
        rect = canvas.create_rectangle(
            start_x, start_y, start_x, start_y, fill="light sky blue")

    def on_move(event):
        curX, curY = (event.x, event.y)
        canvas.coords(rect, start_x, start_y, curX, curY)

    canvas = Canvas(root)
    canvas.bind("<ButtonPress-1>", on_click)
    canvas.bind("<B1-Motion>", on_move)
    canvas.pack(fill='both', expand=1)


def new_ocr():
    global root
    listener = mouse.Listener(on_move=None, on_click=on_click, on_scroll=None)
    print("Ready for screenshot! Drag a selection!")
    listener.start()
    make_gui()
    while listener.running:
        if keyboard.is_pressed('esc'):
            listener.stop()
            break
        root.update()
    root.destroy()


def main():
    print("Ctrl+Alt+Y to set up a screenshot.")
    keyboard.add_hotkey('ctrl+alt+y', new_ocr)
    keyboard.wait()


if __name__ == '__main__':
    if hasattr(sys, '_MEIPASS'):
        saved_dir = os.getcwd()
        os.chdir(sys._MEIPASS)
        try:
            main()
        finally:
            os.chdir(saved_dir)
    else:
        main()
