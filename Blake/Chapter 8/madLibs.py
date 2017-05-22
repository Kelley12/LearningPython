#! python3
# madLibs.py - Enter the path to the Mad Libs file. The program then reads through the file asking
# the user for keywords when they come up in the file. It then writes the text with the user input to file.

import os,sys

# Create a list of the keywords
keywordList = ['ADJECTIVE','NOUN','ADVERB','VERB']

print('Enter the full path to the Mad Libs file')
userInputPath = input()
madLibFilePath = os.path.join('\\\\'.join(userInputPath.split('\\')))

print(madLibFilePath)
# Split the path getting directory and file
madLibFileDirectory = os.path.dirname(madLibFilePath)
madLibFile = os.path.basename(madLibFilePath)

# Check that the path and file exist
if os.path.exists(madLibFileDirectory) == False:
    print('Mad Lib file directory "' + madLibFileDirectory + '" does not exist')
    sys.exit()
elif os.path.isfile(madLibFilePath) == False:
    print('Mad Lib file does not exist')
    sys.exit()
else: # Change to the directory
    os.chdir(madLibFileDirectory)

madLibFileObject = open(madLibFile)

madLibResultList = []

for line in madLibFileObject:
    words = line.split(' ')
    for word in words:
        for keyword in keywordList:
            if keyword in word:
                if keyword.lower() == 'adjective':
                    print('Enter an ' + keyword.lower() + ':')
                else:
                    print('Enter a ' + keyword.lower() + ':')
                userInput = input()
                word = word.replace(keyword, userInput)
        madLibResultList.append(word)
madLibFileObject.close()

madLibsResultsFile = madLibFileDirectory + '\\madLibResults.txt'
madLibFileObject = open(madLibsResultsFile, 'w')
madLibFileObject.write(' '.join(madLibResultList))
madLibFileObject.close()

print('Mad Libs results written to: ' + madLibsResultsFile)
