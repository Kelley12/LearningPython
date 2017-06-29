#! python3
# play2048.py - 2048 is a simple game where you combine tiles by sliding them up, down,
# left, or right with the arrow keys. This program will open the game at
# https://gabrielecirulli.github.io/2048/ and keep sending up, right, down, and left keystrokes
# to automatically play the game.

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

browser = webdriver.Firefox()
browser.get('https://gabrielecirulli.github.io/2048/')
htmlElem = browser.find_element_by_tag_name('html')

i = 1
while i == 1: 
    htmlElem.send_keys(Keys.UP) # send up key
    htmlElem.send_keys(Keys.RIGHT) # send right key
    htmlElem.send_keys(Keys.DOWN) # send down key
    htmlElem.send_keys(Keys.LEFT) # send left key
