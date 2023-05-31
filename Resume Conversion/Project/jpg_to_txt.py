# PIL for working with images 
# pytesseract for performing OCR (optical character recognition)
# os for file operations

from PIL import Image
import pytesseract
from pytesseract import Output
import os

# This code opens an image file named "Remo.jpg" using the Image.open() function from the PIL library
# The image is stored in the image variable, and print(image) prints the image object

image = Image.open("D:\Intern VENV\InputDataLoad\Remo.jpg")
print(image)

# pytesseract.image_to_string() function takes the image object as input and performs OCR to extract the text from the image. 
# The extracted text is stored in the text variable, then prints the extracted text

text = pytesseract.image_to_string(image)
print(text)

# The filename variable stores the path and name of the output file where the extracted text will be saved
# The os.makedirs() function ensures that the directory structure leading to the output file exists
# If the directories already exist, it does nothing (exist_ok=True).

filename = "./OutputData/jpg_to_txt.txt"
os.makedirs(os.path.dirname(filename), exist_ok=True)

# This code block opens the output file in write mode using the open() function
# The with statement ensures that the file is properly closed after writing
# The extracted text (text) is written to the file using the write() method of the file object (f.write(text))

with open(filename, "w") as f:
    f.write(text)


