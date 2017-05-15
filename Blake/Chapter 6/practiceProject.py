#! python3
# Chapter Project from Chapter 6: Adding Bullets to Wiki

import sys

tableData = [['apples', 'oranges', 'cherries', 'banana'],
            ['Alice', 'Bob', 'Carol', 'David'],
            ['dogs', 'cats', 'moose', 'goose']]

def printTable(listOfStrings):
    ''' Takes a list of lists of strings and displayes
        it in a well-organized list '''
    colWidths = [0] * len(listOfStrings)
    index = 0
    # Find the length of the largest string from each list
    for l in listOfStrings:
        for li in l:
            if len(li) > colWidths[index]:
                colWidths[index] = len(li)
        index += 1

    index = 0

    # print out the lists - This is a terrible implementation, I'm sure there is a much better way
    i = 0
    while i < len(listOfStrings[0]):
        string = ''
        for los in listOfStrings:
            string += ' ' + los[i].rjust(colWidths[index])
            index += 1
        print(string)
        index = 0
        i += 1

printTable(tableData)
