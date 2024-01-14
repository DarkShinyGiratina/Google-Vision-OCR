# Google Vision OCR

An OCR program I wrote that interfaces with Google's [Cloud Vision API](https://cloud.google.com/vision?hl=en)

## Setup

1. Follow the [Cloud Vision setup](https://cloud.google.com/vision/docs/setup) tutorial up to and including the `Authentication with user accounts` step.
   - You _do_ need to set up a Billing Account, but provided you're calling the API less than 1000 times per month it's free (and it's only $1.50 for each 1000 calls beyond that, so you're not going to pay much if at all)
2. Install the exe from [Releases](https://github.com/DarkShinyGiratina/Google-Vision-OCR/releases) and run it. That's it!

## How to Use

1. Run the script
2. While the script is running, press `Ctrl+Alt+Y` to enter screenshot mode. This will turn your **PRIMARY** monitor slightly white, and you can then drag a box around your text.
   - You can press `Escape` to cancel the screenshot if you want.
3. The program will then run the OCR and copy the result into your clipboard, allowing you to paste it anywhere (if using for language learning purposes like I am, you can paste into a [texthooker page](https://learnjapanese.moe/texthooker.html) with an extension like [Clipboard Inserter](https://chromewebstore.google.com/detail/clipboard-inserter/deahejllghicakhplliloeheabddjajm))

## Running the Python Script Instead of the EXE

Note that this script was written in Python 3.12. I'm not sure if you _need_ Python 3.12 to run it but I would make sure you have the [latest version](https://www.python.org/downloads/) installed.

If you don't want to run the exe (or you're not on Windows), just download the source code, extract it to anywhere you wish, and install the requirements by running

```
pip install -r requirements.txt
```

Then simply run the Python script:

```
python "DSG OCR.py"
```

Run in a virtual environment if you so wish.
