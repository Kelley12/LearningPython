#! python3
# Saving variables with the shelve modules examples from Chapter 8

import os,shelve

fileCreationPath = 'C:\\Users\\bkell\\Google Drive\\Programming\\Python\\LearningPython\\Blake\\Chapter 8'
testFileDirectory = 'testFiles'
testFilePath = os.path.join(fileCreationPath,testFileDirectory)

if os.path.exists(testFilePath):
    os.chdir(testFilePath)
else:
    os.makedirs(testFilePath)
    os.chdir(testFilePath)

print('Create a shelf file with some data:')
shelfFile = shelve.open('mydata')
motorbikes = ['Yamaha','Honda','Kawasaki','Suzuki','KTM','Husqvarna','Beta']
for bike in motorbikes:
    print('\t' + bike)
shelfFile['motorbikes'] = motorbikes
shelfFile.close()

print('Reopen the shelf file and read the content')
shelfFile = shelve.open('mydata')

print('Shelf file keys:')
for key in list(shelfFile.keys()):
    print('\t' + key)

print('Shelf file values:')
for valueList in list(shelfFile.values()):
    for value in valueList:
        print('\t' + value)
shelfFile.close()
