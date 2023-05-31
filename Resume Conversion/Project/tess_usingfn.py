from PIL import Image
import pytesseract
from pytesseract import Output
import os
import re

def main(newfilepath):

    # Get current working directory
    current_directory = os.getcwd()
    print("Current working directory:", current_directory)

    fol=os.listdir()
    print(fol)

    # Change directory
    new_directory = "InputDataLoad"
    os.chdir(new_directory)
    print("Changed directory to:", new_directory)

    # Get current working directory again
    current_directory = os.getcwd()
    print("Current working directory:", current_directory)

    if fol==[]:
        print("Please upload file in the directory for converting to text")
    else:
        for filename in fol:
                if (re.search('.(jpg)$',filename)):
                    # print("os path",os.path)
                    newfilepath=os.path.join(current_directory,filename)  # here append filename with current filepath
                    # newfilepath = filepath + filename
                    jpg.jpgtxt(newfilepath)  #call function for convert word2text
                    # print(filename)

                elif (re.search('.(png)$',filename)):
                    newfilepath=os.path.join(current_directory,filename)  # here append filename with current filepath   
                    png.pngtxt(newfilepath)

main()

from PIL import Image
import pytesseract
import os
import re,jpgtx,pngtxt

def jpgtxt(filepath):
    with Image.open(filepath) as img:
        text = pytesseract.image_to_string(img)
        print(text)

def pngtxt(filepath):
    with Image.open(filepath) as img:
        text = pytesseract.image_to_string(img)
        print(text)

def main():
    # Get current working directory
    current_directory = os.getcwd()
    print("Current working directory:", current_directory)

    # Change directory
    new_directory = "InputDataLoad"
    os.chdir(new_directory)
    print("Changed directory to:", new_directory)

    # Get current working directory again
    current_directory = os.getcwd()
    print("Current working directory:", current_directory)

    # Get list of files in directory
    files = os.listdir()
    print("Files in directory:", files)

    if not files:
        print("Please upload file in the directory for converting to text")
    else:
        for filename in files:
            if re.search('\.jpe?g$', filename, re.IGNORECASE):
                filepath = os.path.join(current_directory, filename)
                jpgtx(filepath)
            elif re.search('\.png$', filename, re.IGNORECASE):
                filepath = os.path.join(current_directory, filename)
                pngtxt(filepath)
            else:
                print(f"Skipping file {filename} as it is not a JPG or PNG file.")

main()