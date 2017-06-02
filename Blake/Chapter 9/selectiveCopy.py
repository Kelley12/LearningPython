#! python3
# selectiveCopy.py - A program that walks through a folder tree
# and searches for files with a certain file extension (such as .pdf or .jpg).
# Copies those files from whatever location they are in to a new folder.

import os,zipfile,shutil

def selectiveCopy(folder,fileExtension):
    folder = os.path.abspath(folder) # make sure folder is absolute
    os.chdir(folder)

    # Create a new folder to copy the found files to
    newFolder = folder + "\SearchResults"

    # Loop through the files in the folder finding all that match the extension
    for folderName, subfolders, filenames in os.walk(folder):
        for filename in filenames:
            if filename.endswith(fileExtension):
                shutil.copy(filename,newFolder)

folder = input("Enter the folder path to search in:")
fileExtension = input("Enter the file extension to search for:")
selectiveCopy(folder,fileExtension)
