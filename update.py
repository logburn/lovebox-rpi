import urllib2
import textwrap
from customWaveshare import *
import os
import time

url = "" # your lovebox url here! should look soething like the following: "https://example.com/current.txt"

resp = urllib2.urlopen(url).read()
resp = textwrap.fill(resp, 21)
curr = open("current.txt","r").read()


if resp != curr:
    f = open("current.txt", "w")
    f.write(resp)
    f.close()
    os.system("python newMessage.py")
