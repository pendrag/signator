# signator
A simple script to sign revenues from a batch PDF.

Author: sendero@gmail.com

## Requirements

* Python 3.x: Follow instructions at https://docs.conda.io/projects/conda/en/latest/user-guide/install/linux.html
* PDFtk: `sudo apt install pdftk`
* pdftotext: `sudo apt install poopler-utils`

## Installation

Get the code from `https://github.com/pendrag/signator/archive/main.zip` an unzip the package.

## Usage

1. Edit `sign.py` and set paths to files in the begining of the script. Example:
```
INPUT_PDF = 'PDFborrador.pdf'
SIGNATURE = 'signature.pdf'
CODES = 'codigos.csv'
```
2. Create an `output` directory
3. Run `python sign.py` and all the signed documents will be available at `output`

## Create transparent signature files with PDF format
 User `convert` tool and convert a PNG image with transparency to PDF:
 
 `convert signature.png -transparent white -background none signature.pdf`
