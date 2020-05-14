import os
from pathlib import Path
#import pyautogui
import pynput
import time
from cv2 import cv2
import pyperclip
import pytesseract
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files (x86)\Tesseract-OCR\\tesseract.exe'
from PIL import ImageGrab
#from pynput.keyboard import Key, Controller, Listener



#def snippingTool():
   # pyautogui.hotkey('winleft','shift', 's')

def on_press(key):
    try:
        pass #print('alphanumeric key {0}'.format(key.char))
    except AttributeError:
        pass #print('special key {0} pressed'.format(key))

def on_release(key):
    pass
    #print('{0} released'.format(key))
    if key == pynput.keyboard.Key.esc:
        # Stop listener
        return False
    elif key == pynput.keyboard.Key.alt_l:
            #snippingTool()
            #time.sleep(2)
            im = ImageGrab.grabclipboard()
            im.save('screenGrab.png','PNG')
            img = cv2.imread('screenGrab.png')
            text = pytesseract.image_to_string(img)
            print(text)
            pyperclip.copy(text)


# Collect events until released
with pynput.keyboard.Listener(
        on_press=on_press,
        on_release=on_release) as listener:
    listener.join()

# ...or, in a non-blocking fashion:
listener = pynput.keyboard.Listener(
    on_press=on_press,
    on_release=on_release)
listener.start()


#def pressIsTrue():
    #if pynput.keyboard.Listener() == pynput.keyboard.Key.up
        #print('Yay')
