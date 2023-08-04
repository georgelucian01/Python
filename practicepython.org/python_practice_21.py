
## July 27th 2023
## Problem number 21
## https://www.practicepython.org/exercise/2014/11/30/21-write-to-a-file.html

## Write a txt file
## ask user of a name
import re
import subprocess

# File creation function
def create_file(name, content):
    with open(f'{name}.txt', 'w') as open_file:
        open_file.write(content) 

# Open file automaticaly   
def open_file(name):
    try:
        subprocess.run(['start', '', f'{name}.txt'], shell=True)  # Windows
    except FileNotFoundError:
        print("File not FOUND")

# Remove illegal characters from the name
def clean_name(name):
    # Define a regular expression to match illegal characters
    # <, >, :, ", /, \, |, ?, and * are not allowed in Windows file names
    illegal_chars_pattern = r'[<>:"/\\|?*]'
    # Use re.sub() to replace illegal characters with an empty string
    cleaned_name = re.sub(illegal_chars_pattern, '', name)
    return cleaned_name

def main():
    content = input("Content for the txt file: ")
    name = input("Name for the txt file: ")
    legal_name = clean_name(name)
    create_file(legal_name, content)
    open_file(legal_name)

if __name__ == "__main__":
    main()
