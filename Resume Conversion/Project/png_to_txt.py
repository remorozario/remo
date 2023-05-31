from PIL import Image
import pytesseract
import pytesseract as pt
from pytesseract import Output
import os

def pngg(filepath):
        
    image = Image.open(r"D:\Intern VENV\InputDataLoad\bill.png")
    img_text = pt.image_to_string(image)
    print(img_text)

    # image = Image.open("D:\Intern VENV\InputDataLoad\Remo.jpg")  
    # # image = Image.open()
    # print(image)

    text = pytesseract.image_to_string(image)
    print(text)

    filename = "D:\Intern VENV\OutputData\demo2.txt"
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    with open(filename, "w") as f:
        f.write(text)

