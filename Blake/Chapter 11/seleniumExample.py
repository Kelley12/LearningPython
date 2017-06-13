#! python3
# selenuimExample.py
# Selenuim documentation: http://selenium-python.readthedocs.org/.

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

browser = webdriver.Firefox()

# Open Firefox and direct it to a URL. On this page, we try to find
# elements with the class name 'bookcover', and if such an element is found,
# we print its tag name using the tag_name attribute. If no such element was
# found, we print a different message.

browser.get('http://inventwithpython.com')
try:
    elem = browser.find_element_by_class_name('bookcover')
    print('Found <%s> element with that class name!' % (elem.tag_name))
except:
    print('Was not able to find an element with that name.')

# Clicking on a page
# Opens up the browser to a web page, finds and element on the page, and clicks on it.

browser.get('http://inventwithpython.com')
linkElem = browser.find_element_by_link_text('Read It Online')
linkElem.click()

# Filling out and submitting a form
# Opens the browser to a web page, finds the form elements,
# fills them with information, and then submits the form

browser.get('https://mail.yahoo.com')
emailElem = browser.find_element_by_id('login-username')
emailElem.send_keys('not_my_real_email')
passwordElem = browser.find_element_by_id('login-passwd')
passwordElem.send_keys('12345')
passwordElem.submit()

# Sending special keys
browser.get('http://nostarch.com')
htmlElem = browser.find_element_by_tag_name('html')
htmlElem.send_keys(Keys.END) # scrolls to bottom
htmlElem.send_keys(Keys.HOME) # scrolls to top
