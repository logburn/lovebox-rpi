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
a website stores a text file that is pulically accessible, and a Raspberry Pi uses a cron job to check this site every minute.
if the text on this website is changed, the screen updates to display "NEW MESSAGE", and a listener is put into (a|e)ffect for a button input (which is attatched to the display and uses GPIO).
once the button is pressed, the message is displaye don screen and stays there until the cron updates again AND finds a new message.
that's it really
