# -*- coding: utf-8 -*-
"""
Created on Mon Nov  5 08:50:08 2018

@author: Tim
"""

#1: Get Colour with Robustness of 3

from sense_hat import SenseHat
sense = SenseHat()

sense.set_rotation(180)

def get_colour(colour):
  keep_looping = True
  no_of_try = 1
  while keep_looping:
    colour_str = int(input("enter the value of the " + colour + " color for message (0 to 255):"))
    if 0<= colour_str <= 255:
      print("value must be between 0 to 255")
      no_of_try += 1
    if no_of_try > 3:
      print("default value of 0 selected")
      colour_str = 0
      break
    else:
      break
  return colour_str

r_int = get_colour("red")
g_int = get_colour("green")
b_int = get_colour("blue")

msg_colour = (r_int, g_int, b_int)
sense.show_message("I got it!", text_colour = msg_colour)


#2. :Set Individual Pixel Colour

from sense_hat import SenseHat
import time
from random import randint
sense = SenseHat()

r = (255,0,0)
x = (0,0,0)
sense.clear()

while True:
  a = randint(0,7)
  b = randint(0,7)
  
  sense.set_pixel(a,b,r)
  time.sleep(1)
  sense.set_pixel(a,b,x)


#3: Image Display on Sense Hat Board

from sense_hat import SenseHat
sense = SenseHat()

y = (255,255,0)
b = (0,0,0)

image_pixels = [b,b,b,b,b,b,b,b,
                b,b,b,y,b,b,b,b,
                b,b,y,y,y,b,b,b,
                b,y,b,y,b,y,b,b,
                b,b,b,y,b,b,b,b,
                b,b,b,y,b,b,b,b,
                b,b,b,y,b,b,b,b,
                b,b,b,b,b,b,b,b]

sense.set_pixels(image_pixels)


#4: Alternating Arrow Colour (unsolved)
from sense_hat import SenseHat
import time
from random import randint
sense = SenseHat()

y = (255,255,0)
g = (0,255,0)
b = (0,0,0)

image_pixels = [b,b,b,b,b,b,b,b,
                b,b,b,y,b,b,b,b,
                b,b,y,y,y,b,b,b,
                b,y,b,y,b,y,b,b,
                b,b,b,y,b,b,b,b,
                b,b,b,y,b,b,b,b,
                b,b,b,y,b,b,b,b,
                b,b,b,b,b,b,b,g]
while True:
  rot_angle = 0
  rot_angle += 90
  if rot_angle == 360:
    rot_angle = 0
  for i in range(len(image_pixels)):
    if image_pixels[i] == y:
      image_pixels[i] = g
    elif image_pixels[i] == g:
      image_pixels[i] = y
  sense.set_pixels(image_pixels)
  time.sleep(1)




