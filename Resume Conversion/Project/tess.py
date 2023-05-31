# import pytesseract
# import cv2
# img = cv2.imread("D:\Intern VENV\InputDataLoad\maxresdefault.jpg")
# img = cv2.resize(img, (720, 480))
# cv2.imshow('Result', img)
# cv2.waitKey(0)


# CONVERTING IMAGE TO STRING

# import pytesseract
# import cv2
# img = cv2.imread("D:\Intern VENV\InputDataLoad\maxresdefault.jpg")

# img = cv2.resize(img,(600,400))
# print(pytesseract.image_to_string(img))
# cv2.imshow('Result',img)
# cv2.waitKey(0)


from PIL import Image
import pytesseract
# import pytesseract as pt
from pytesseract import Output
import os

    

# '''to load png files'''
# image = Image.open(r"D:\Intern VENV\InputDataLoad\bill.png")
# img_text = pt.image_to_string(image)
# print(img_text)

# '''to load jpg files'''
#
# img = cv2.imread("D:\Intern VENV\InputDataLoad\Remo.jpg")
# img = cv2.resize(img, (720, 480))
# cv2.imshow('Result', img)
# cv2.waitKey(0)

image = Image.open("D:\Intern VENV\InputDataLoad\Remo.jpg")  
# image = Image.open()
print(image)


# image = image.resize((300,150))
# custom_config = r'-l eng --oem 3 --psm 6' 
# text = pytesseract.image_to_string(image,config=custom_config)
text = pytesseract.image_to_string(image)
print(text)


filename = "D:\Intern VENV\OutputData\demo.txt"
os.makedirs(os.path.dirname(filename), exist_ok=True)
with open(filename, "w") as f:
    f.write(text)


