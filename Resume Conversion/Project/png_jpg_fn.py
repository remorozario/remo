from PIL import Image
import pytesseract
import os,re,jpg_to_txt, png_to_txt

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
                jpg_to_txt.jpgg(filepath)
            elif re.search('\.png$', filename, re.IGNORECASE):
                filepath = os.path.join(current_directory, filename)
                png_to_txt.pngg(filepath)
            else:
                print(f"Skipping file {filename} as it is not a JPG or PNG file.")

main()

