# Import the necessary modules: docx2txt and os
#docx2txt is a module that provides functions to extract text from Word documents
import docx2txt
import os

def wordtotext(newfilepath):
    # Use docx2txt.process() to extract the text from the Word document specified by the file path newfilepath. 
    mytext=docx2txt.process("D:\Intern VENV\InputDataLoad\Remo.docx")

# with open("Output.txt","w") as text:
#     print(mytext,file=text)

    file = open("./OutputData/word_to_txt.txt","w")

    file.writelines(mytext)
    file.close()


