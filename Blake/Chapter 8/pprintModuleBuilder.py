#! python3
# Saving variables with the shelve modules examples from Chapter 8

import os,pprint

fileCreationPath = 'C:\\Users\\bkell\\Google Drive\\Programming\\Python\\LearningPython\\Blake\\Chapter 8'

print('Create some data:')
motorbikes = [{'name': 'Yamaha', 'color': 'blue'},{'name': 'Honda', 'color': 'red'},{'name': 'Kawasaki', 'color': 'green'},{'name': 'Suzuki', 'color': 'yellow'},{'name': 'KTM', 'color': 'orange'},{'name': 'Husqvarna', 'color': 'white'},{'name': 'Beta', 'color': 'red'}]

pprint.pformat(motorbikes)

fileObj = open('pprintModule.py', 'w')
fileObj.write('motorbikes = ' + pprint.pformat(motorbikes) + '\n')
fileObj.close()
