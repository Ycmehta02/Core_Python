#Reading/Writing Text and CSV Files

#Reading/Writing Text Files-----------------------------------------------------------------------
#Python provides the open() function to read and write text files.

# Open the file in read mode --Reading a Text File
with open("murakami.txt", "r", encoding="utf-8") as file:
    content = file.read()  # Read entire file
    print(content)

"""
open("example.txt", "r"): Opens the file in read mode.
file.read(): Reads the complete file content.
with statement ensures that the file is closed after use.
"""

# Open the file in write mode (creates file if not exists)

with open("example.txt", "w") as file:
    file.write("Hello, this is a sample text file.\n")
    file.write("Python makes file handling easy!")

"""
"w" mode overwrites the file if it already exists.
file.write() writes text into the file.
"""


# Open file in append mode

with open("example.txt", "a") as file:
    file.write("\nThis is an additional line.")
#"a" mode appends data instead of overwriting.

#Reading/Writing CSV Files------------------------------------------------------------------------------

#reading a csv file
#import csv

# Open and read CSV file
# with open("books.csv", "r") as file:
#     reader = csv.reader(file)
#     for row in reader:
#         print(row)  # Print each row as a list

#csv.reader(file): Reads CSV content line by line.

import csv

# Sample data to write
data = [
    ["Name", "Age", "City"],
    ["Alice", 25, "New York"],
    ["Bob", 30, "London"]
]

# Open and write CSV file
with open("data.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerows(data)  # Write multiple rows
# "w" mode creates/overwrites the file.
# writer.writerows(data): Writes multiple rows.

# Append a new row
with open("data.csv", "a", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Charlie", 28, "Paris"])  # Add a single row


#Handling JSON and XML--------------------------------------------------------------------------

#JSON file(.json)***********************************
#JSON (JavaScript Object Notation) is widely used for data storage and API communication.

#Writing to a JSON file
import json
data = {
    "name": "Alice",
    "age": 25,
    "city": "New York"
}
# Open and write JSON file
with open("data.json", "w") as file:
    json.dump(data, file, indent=4)  # Pretty-print JSON
#json.dump(data, file): Writes JSON data.
#indent=4: Formats JSON output for readability.


#Writing in JSON
import json
# Open and read JSON file
with open("data.json", "r") as file:
    data = json.load(file)  # Convert JSON to Python dictionary
    print(data)
#json.load(file): Converts JSON into a Python dictionary.

#XML file(.xml)********************************************
#XML (eXtensible Markup Language) is used for structured data storage.

#Writing to an XML File----------------------
import xml.etree.ElementTree as ET

# Create root element
root = ET.Element("People")

# Add child element
person = ET.SubElement(root, "Person")
person.set("name", "Alice")
person.text = "Age: 25"

# Write to file
tree = ET.ElementTree(root)
tree.write("data.xml")

# ET.Element() creates an XML element.
# ET.SubElement() adds child elements.
# tree.write("data.xml") saves the file.

#Reading an XML File------------------------

import xml.etree.ElementTree as ET

# Parse XML file
tree = ET.parse("data.xml")
root = tree.getroot()

# Print root element
print(root.tag)

# Iterate over child elements
for child in root:
    print(child.tag, child.text)

# ET.parse("data.xml"): Loads XML file.
# root.getroot(): Retrieves the root element.
# .tag and .text: Extract tag name and text content.

#File System Operations (os, shutil Modules)----------------------------------------------------------------------------------

import os
# List all files in the current directory
files = os.listdir(".")
print(files)
#os.listdir(".") lists all files and directories in the current folder.


#Check if a File Exists
if os.path.exists("example.txt"):
    print("File exists")
else:
    print("File not found")
#os.path.exists("filename") checks if a file/directory exists.


#Remove a File
os.remove("example.txt")
print("File deleted")
#os.remove("filename") deletes a file.


#Remove an Empty Directory
# os.rmdir("new_folder")
# print("Directory removed")
#os.rmdir("dirname") removes an empty directory.

#Working with shutil Module--------------------------------------------------------------------------
#The shutil module is used for file and directory management.

#Copy a file
import shutil
shutil.copy("data.csv", "backup.csv")
print("File copied successfully")
#shutil.copy(src, dest): Copies a file.


#Move a file
#shutil.move("data.csv", "backup_folder/data.csv") #Moves a file
#print("File moved successfully")


#Remove a Directory and Its Contents
# shutil.rmtree("backup_folder")
# print("Directory deleted")


















































