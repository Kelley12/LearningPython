#! python3
# largeFileFinder.py - Searches for the largest files in a given path
# and displays those on the screen.

import os

def largeFileSearch(folder):
    folder = os.path.abspath(folder) # make sure folder is absolute
    os.chdir(folder)

    # Loop through the files in the folder finding all that are over 100MB
    for folderName, subfolders, filenames in os.walk(folder):
        for filename in filenames:
            filePath = os.path.join(folderName,filename)
            if os.path.getsize(filePath) > 100000000:
                print(filePath)

print("***** Search for the largest files in a given path *****")
folder = input("Enter the folder path to search in:")
largeFileSearch(folder)
