#!/usr/bin/python
# -*- coding:utf-8 -*-
import sys
import os
picdir = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), 'pic')
libdir = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), 'lib')
if os.path.exists(libdir):
    sys.path.append(libdir)

import logging
from waveshare_epd import epd2in7
import time
from PIL import Image,ImageDraw,ImageFont
import traceback

logging.basicConfig(level=logging.DEBUG)
epd = epd2in7.EPD()
pinNum = 1

#def formatString(string):

def displayOnScreen(resp):
    font24 = ImageFont.truetype(os.path.join(picdir, 'Font.ttc'), 24)
    print("Screen dispaying: " + resp)
    epd.init()
    # Drawing on the Horizontal image
    Himage = Image.new('1', (epd.height, epd.width), 255)  # 255: clear the frame
    draw = ImageDraw.Draw(Himage)
    draw.text((10, 0), resp, font = font24, fill = 0)
    epd.display(epd.getbuffer(Himage))
    logging.info("Goto Sleep...")
    epd.sleep()

