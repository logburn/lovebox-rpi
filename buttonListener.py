from customWaveshare import *
import sys
sys.path.insert(1, "../lib")
import os

from gpiozero import Button
from customWaveshare import *

btn = Button(5)
unread = True

def handleBtnPress():
    global unread
    unread = False
    os.system("python displayMessage.py")

while unread is not False:
    os.system("echo running")
    btn.when_pressed = handleBtnPress
