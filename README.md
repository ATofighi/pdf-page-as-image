# PDF Pages as PDF of Images

This is a simple Python script (created by Microsoft Copilot!) that converts each page of a PDF to an image and then creates a new PDF from those images. This can be useful for reducing the size of a large PDF. I need this script to reduce the size of PDFs created by Microsoft OneNote. 

## Requirements

This script requires `poppler-utils`. You can install it using this command in Ubuntu:

```bash
sudo apt-get install poppler-utils
```

Then, after cloning the repository, install the Python requirements using this command:

```bash
pip install -r requirements.txt
```

## Usage
You can run this script from the command line with your input and output file names as arguments. For example:

```bash
python convert.py input.pdf output.pdf
```
