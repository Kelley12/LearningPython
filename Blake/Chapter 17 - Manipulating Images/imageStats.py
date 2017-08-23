#! python3
# imageStats.py - Gets statistics of the given file

from PIL import Image

imagePath = ""
image = Image.open(imagePath)

print("Filename: " + image.filename)
print("Format: " + image.format)
print("Format Description: " + image.format_description)

print('Size of image: ' + image.size)

width, height = image.size
print('(Width, Height): (' + str(width) + ',' + str(height) + ')')
