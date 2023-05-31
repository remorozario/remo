### Hi there 👋

# File Conversion Program

This program is designed to convert files to text format. It supports Word documents (.docx, .doc), PDF files (.pdf), and images (.jpg).

## Requirements

- Python 3.x
- Libraries:
  - extracting_pdf_to_text
  - extracting_word_to_text
  - pytesseract
  - PIL (Python Imaging Library)

## Usage

1. Place the files you want to convert in the appropriate directories:
   - Word documents: "./InputDataLoad"
   - PDF files: "./InputDataLoad"
   - Images: "./InputDataLoad"
2. Run the `main()` function to initiate the conversion process.
3. The program will scan the input directories for supported files and convert them to text.
4. The converted text will be stored in separate text files in the "./OutputData" directory.
5. The program will print the file paths of the converted text files.
6. For Word documents, the `extracting_word_to_text.wordtotext()` function will be used to convert them to text.
7. For PDF files, the `extracting_pdf_to_text.pdftotext()` function will be used to extract the text.
8. For images, the program will use OCR (optical character recognition) to extract text using the `pytesseract` library.

Note: Make sure to install the required libraries and provide the correct file paths in the code for image and Word document conversion.

## Example

Suppose you have the following files in the "./InputDataLoad" directory:

- document1.docx
- document2.doc
- document3.pdf
- image1.jpg

After running the program, the text files will be created in the "./OutputData" directory as follows:

- word_to_txt.txt
- word_to_txt.txt
- pdf_to_txt.txt
- jpg_to_txt.txt

The program will print the file paths of the converted text files:

