import os
import re
import docx2txt
from PyPDF2 import PdfReader

def main():
    os.chdir("./InputDataLoad")
    filepath = os.getcwd()
    print("filepath")
    folder = os.listdir()
    print("filepath:",filepath)
    os.chdir("../")
    print("Folder inside filepath =",folder)

    if folder==[]:
        print("Please upload file in the directory for converting to text")
    else:    
        for filename in folder:
            if (re.search('.(docx|doc)$',filename)):
                # print("os path",os.path)
                newfilepath=os.path.join(filepath,filename)  # here append filename with current filepath
                # newfilepath = filepath + filename
                wordtotext(newfilepath)  #call function for convert word2text
                # print(filename)

            elif (re.search('.(pdf)$',filename)):
                newfilepath=os.path.join(filepath,filename)  # here append filename with current filepath   
                pdftotext(newfilepath)


def wordtotext(newfilepath):

    mytext=docx2txt.process(newfilepath)

    file = open("./OutputData/single1.txt","w")
    file.writelines(mytext)
    file.close()


def pdftotext(newfilepath):

    reader=PdfReader(newfilepath)
    n=len(reader.pages)
    for i in range(0,n):
        page=reader.pages[i]
        text=page.extract_text()
        print(text)      

        file1 = open("./OutputData/single2.txt","w")
        file1.writelines(text)
        file1.close()
    
main()