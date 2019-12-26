import urllib2
import textwrap
from customWaveshare import *
import os
import time

resp = urllib2.urlopen('https://lukeogburn.com/lovebox/current.txt').read()
resp = textwrap.fill(resp, 21)
curr = open("current.txt","r").read()


if resp != curr:
    f = open("current.txt", "w")
    f.write(resp)
    f.close()
    os.system("python newMessage.py")
