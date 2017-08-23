#! python3
# lookingBusy.py - Program the moves the mouse every 10 seconds to keep the computer active

import pyautogui

while 1 == 1:
    x, y = pyautogui.position()
    pyautogui.moveTo(x+10, y+10)
    wait(10)
