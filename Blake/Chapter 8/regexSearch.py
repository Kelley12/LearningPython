#! python3
# regexSearch.py - opens all .txt files in a folder and searches for any line
# that matches a user-supplied regular expression. The results are printed to the screen.

import os,sys,re

print('Enter the full path to the folder to search:')
userInputPath = input()
searchDirectoryPath = os.path.join('\\\\'.join(userInputPath.split('\\')))

# Check that the path and file exist
if os.path.exists(searchDirectoryPath) == False:
    print('Directory "' + searchDirectoryPath + '" does not exist')
    sys.exit()
else: # Change to the directory
    os.chdir(searchDirectoryPath)

print('Enter a regular expression to search for in the files:')
searchRegex = re.compile(input())

filesInDirectory = os.listdir(searchDirectoryPath)
foundFiles = []

for filename in filesInDirectory:
    if '.txt' in filename:
        fileObject = open(os.path.join(searchDirectoryPath,filename))
        fileContent = fileObject.read()
        if searchRegex.search(fileContent) != None:
            foundFiles.append(filename)

if len(foundFiles) < 1:
    print('No files contain content matching that regular expression.')
else:
    print('Files containing a match to the regular expression:')
    for matchedFile in foundFiles:
        print('\t' + matchedFile)
