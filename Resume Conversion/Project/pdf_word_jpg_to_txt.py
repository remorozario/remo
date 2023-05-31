import os
import re
import extracting_pdf_to_text
import extracting_word_to_text
import jpg_to_txt
def main():
    
    # Change the current working directory to "./InputDataLoad" using os.chdir()
    # This assumes that there is a directory named "InputDataLoad" in the current working directory
    os.chdir("./InputDataLoad")
    # Get the current working directory path using os.getcwd() and assign it to the variable filepath
    filepath = os.getcwd()
    print("filepath")
    # Get a list of files and directories in the current working directory using os.listdir() and assign it to the variable folder
    folder = os.listdir()
    print("filepath:",filepath)
    # Change the current working directory back to the previous directory using os.chdir("../")
    # This brings the program back to the original working directory
    os.chdir("../")
    print("Folder inside filepath =",folder)

    # Check if the folder list is empty using if folder==[]. If it is empty, it means no files are present in the "./InputDataLoad" directory.
    # If the folder list is empty, print the string "Please upload file in the directory for converting to text".
    if folder==[]:
        print("Please upload file in the directory for converting to text")
    else:    
        for filename in folder:
            # Check if the folder list is empty using if folder==[]. If it is empty, it means no files are present in the "./InputDataLoad" directory
            # If the folder list is empty, print the string "Please upload file in the directory for converting to text"
            
            if (re.search('.(docx|doc)$',filename)):
                # If the filename matches the pattern, construct the full file path by joining filepath and filename using os.path.join() and assign it to the variable newfilepath.
                newfilepath=os.path.join(filepath,filename)  # here append filename with current filepath
                
                extracting_word_to_text.wordtotext(newfilepath)  #call function for convert word2text
                
            # If the filename does not match the pattern defined for Word documents, check if it matches the pattern .(pdf)$ using re.search()
            # This pattern matches filenames that end with ".pdf".
            elif (re.search('.(pdf)$',filename)):
                newfilepath=os.path.join(filepath,filename)  # here append filename with current filepath   
                extracting_pdf_to_text.pdftotext(newfilepath)
main()


