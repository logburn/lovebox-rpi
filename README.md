# Raspberry Pi lovebox
in abstract terms, this projec lets me send messages from my website to the screen of a Raspberry Pi, which can then be read by pushing a button on the display.

## motivation
this is a Christmas present for my lovely girlfriend :)

## build status
project may be worked on if requested by girlfriend
some tentative plans include: 
 - making message dissapear after five minutes
 - indicating on the website that the message has been read

## coding style
horrible practices utilized, few comments, philosphy of "it works, so don't touch it" rampant

## method
there are 2 main components here:

 1. Raspberry Pi running python in a cron job
 2. website hosting an editable text file

this repo is only for the raspberry pi aspect.

the pi runs a cron job that checks the website for updates, and if there is one, the screen will update to indicate this. a listener on the GPIO will wait for a button press to show the message on the screen, at which point the listener will stop and the cron will be the only thing running.

## hardware used
 - Raspberry Pi 4, 1GB
 - [2.7 inch Waveshare display](https://www.amazon.com/2-7inch-Resolution-Two-Color-Interface-Raspberry/dp/B07PKSZ3XK/ref=sr_1_4)
 - box to hold RPi, solely for presentation
 - chord to keep pi running 24/7
