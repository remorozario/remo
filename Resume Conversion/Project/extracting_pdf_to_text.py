# Import the necessary modules
# PdfReader is a class that allows reading PDF files
from PyPDF2 import PdfReader
import os

def pdftotext(newfilepath):

    # Use PdfReader(newfilepath) to create a PdfReader object, which reads the PDF file specified by the file path newfilepath
    # The reader variable holds this object
    reader=PdfReader(newfilepath)

    # Get the total number of pages in the PDF
    n=len(reader.pages)

    for i in range(0,n):
        # terate through each page in the PDF file using a for loop with range(0,n).
        # For each page, extract the text using page.extract_text() and assign it to the variable text
        # This extracts the text content of the current page.
        page=reader.pages[i]
        text=page.extract_text()
        print(text)

        # Open a new file named "pdf_to_txt" in the "./OutputData" directory for writing using open()
        file1 = open("./OutputData/pdf_to_txt.txt","w")
        file1.writelines(text)
        file1.close()
        
    