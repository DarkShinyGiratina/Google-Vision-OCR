# Google Vision OCR

An OCR program I wrote that interfaces with Google's [Cloud Vision API](https://cloud.google.com/vision?hl=en)

## Setup

1. Follow the instructions in the [Cloud Setup](#cloud-setup) section.
2. Install the exe from [Releases](https://github.com/DarkShinyGiratina/Google-Vision-OCR/releases) and run it. That's it!

## Cloud Setup

1. Go to Google's Cloud Vision [tutorial](https://cloud.google.com/vision/docs/setup)
2. Click the `Go to project selector` button. [Screenshot](https://prnt.sc/_i0YO4BWN1Wq)
3. Click the `Create Project` button. [Screenshot](https://prnt.sc/_i0YO4BWN1Wq)
   - If you have already made projects before, still make a new one anyway.
4. Name it whatever you want (something memorable preferably)
5. Set up Billing for the Project
   - Click on `Billing` in the sidebar. [Screenshot](https://prnt.sc/fe_ciUs_R10N)
   - Click the `Link a Billing Account` button. [Screenshot](https://prnt.sc/zEpfhW8VABzJ)
   - If you don't already have one, follow the instructions on how to create one.
     - [Step 1](https://prnt.sc/_nNCCWkV1pfW)
     - [Step 2](https://prnt.sc/D8KSrP6_z0xn)
   - **Notes**
     - If this is the first time you have set up Google Cloud, you get $300 of free credit for your first 90 days.
     - You _do_ still need to set up a Billing Account for when the free trial expires, but provided you're calling the API less than 1000 times per month it's free (and it's only $1.50 for each 1000 calls beyond that, so you're not going to pay much if at all)
       - Google Cloud doesn't bill you automatically unless you tell it to, though, so this really should not be a problem.
6. Once the billing account is set up, click the `Enable the API` button on the tutorial page, then `Next`, then `Enable`. [Screenshot](https://prnt.sc/eMBr0YFnB427)
7. Follow the [instructions](https://cloud.google.com/sdk/docs/install) for installing the Google Cloud CLI.
8. Once installed, run `gcloud init` in your Command Prompt/Terminal if it wasn't set up for you by the installer already and follow the instructions in the prompt. Pick the project with the memorable name from earlier.
9. Then run `gcloud auth application-default login` and `gcloud auth application-default set-quota-project PROJECT_ID`, replacing `PROJECT_ID` with the ID for your project which is found by navigating to the [dashboard](https://prnt.sc/l8LY5JcwaTzr) for your project. If it asks you to enable any other APIs, type `y`.

## How to Use

1. Run the script/exe
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
