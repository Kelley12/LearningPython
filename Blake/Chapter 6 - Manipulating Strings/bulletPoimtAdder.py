#! python3
# Chapter Project from Chapter 6: Adding Bullets to Wiki

import sys,pyperclip

text = pyperclip.paste()

# Separate lines and add stars.
lines = text.split('\n')
for i in range (len(lines)): # loop through all indexes in the "lines" list
    lines[i] = '* ' + lines[i] # add star to each string
text = '\n'.join(lines)
pyperclip.copy(text)
