#! python3
# Playing with file manipulation examples from Chapter 8

import os

fileCreationPath = 'C:\\Users\\bkell\\Google Drive\\Programming\\Python\\LearningPython\\Blake\\Chapter 8'
testFileDirectory = 'testFiles'
testFilePath = os.path.join(fileCreationPath,testFileDirectory)
testFileName = 'hello.txt'
testFile = os.path.join(testFilePath,testFileName)

# Clear all changes
if os.path.exists(testFilePath):
    for file in os.listdir(testFilePath):
        os.remove(os.path.join(testFilePath,file))
    os.rmdir(testFilePath)

print('The current working directory is: ' + os.getcwd())
print('Changing directory to: ' + fileCreationPath)
os.chdir(fileCreationPath)
print('The current working directory is: ' + os.getcwd())

print('\nCreating a directory for storing test files: \\' + testFileDirectory)
os.makedirs(testFilePath)
os.chdir(testFilePath)
print('The current working directory is: ' + os.getcwd())

print('\nCreate a test file called: ' + testFileName)
file = open(testFileName, 'w')

print('File created with directory name: ' + os.path.dirname(testFile) + ' and base name: ' + os.path.basename(testFile))
print('Writting "Hello World!" to file')
file.write('Hello World!')
file.close() # Apparently a file must be closed and reopened in order to read the contents
file = open(testFileName)
print('Reading contents of file:')
content = file.read()
file.close()
print(content)
print('The size of the file: ' + str(os.path.getsize(testFile)) + ' bytes')

print('\nFiles in the directory:')
for file in os.listdir(testFilePath):
    print('\t' + file)
