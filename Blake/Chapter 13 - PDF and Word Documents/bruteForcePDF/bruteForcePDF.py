#! python3
# bruteForcePDF.py - Attempts decrypt the PDF by trying every possible English word until it finds one
# that works. Given a text file of potential passwords, loops through each word and attempts to decrypt it.
# Attempts both uppercase and lower case forms of the words.

import PyPDF2

