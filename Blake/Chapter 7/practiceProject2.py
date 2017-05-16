#! python3
# Practice Project from Chapter 7: Regex version of strip()
# If no other arguments are passed other than the string to strip,
# then whitespace characters will be removed from the beginning and
# end of the string. Otherwise, the characters specified in the second argument
# to the function will be removed from the string.

import re

# Create regexes
startWhiteSpaceRegex = re.compile(r'^\s+')
endWhiteSpaceRegex = re.compile(r'\s+$')

# Regex stip function
def strip(string,characters=None):
    if characters == None:
        # Remove any space before and after the string
        return startWhiteSpaceRegex.sub('',endWhiteSpaceRegex.sub('',string))
    else:
        # Replace the characters found in the string with an empty string
        replaceRegex = re.compile(characters)
        return replaceRegex.sub('',string)

string = ' Blake Thomas Kelley '
print('Trimming string: ' + string)
print(strip(string))

characters = 'l'
print('Trimming \'' + characters + '\' from string: ' + string)
print(strip(string,characters))
