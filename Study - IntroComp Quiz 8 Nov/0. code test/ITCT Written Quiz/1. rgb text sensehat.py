# -*- coding: utf-8 -*-
"""
Created on Mon Nov  5 07:23:55 2018

@author: Tim
"""


#1: Basic Python Program
import math

radius_str = input("Enter the radius of your circle: ")
radius_int = int(radius_str)

circumference = 2 * math.pi * radius_int
area = math.pi * (radius_int**2)

print ("The circumference is:", circumference, \
       ", and the area is:", area)


#2: Basic sensehat
from sense_hat import SenseHat
sense = SenseHat()

color_txt = input("Input the text color value")
color_bg = input("Input the background color value")
speed = input("Input the speed")

sense.show_message("This is fun!", text_colour = color_txt, back_colour = color_bg, scroll_speed = speed)
sense.set_rotation(180)

#3: What if user chooses same colour for both?


#4: Program should take Message, Rotation, Colour, Background, Speed
#   Program should reject rotations above 270 and colours above 255
from sense_hat import SenseHat
sense = SenseHat()

display_message = input("Enter your message to display:")

while True:
    rotate_int = int(input("Enter your rotation angle."))
    if 0 <= rotate_int <= 270 and rotate_int%90 == 0:
        break
    else:
        print("You can only rotate by 0, 90, 180, or 270 degrees. Please try again.")

def get_colour_txt():
    colour_txt = [-1,-1,-1]
    while True:
        print("Please input colour of message in RGB: a number from 0-255")
        colour_txt[0] = int(input("red"))
        colour_txt[1] = int(input("green"))
        colour_txt[2] = int(input("blue"))
        for i in colour_txt:
            if colour_txt[i] not in range(256):
                print("your message colour is not in RGB range")
                break
            else:
                return colour_txt

def get_colour_bg():
    colour_bg = [-1,-1,-1]
    while True:
        print("Please input colour of message in RGB: a number from 0-255")
        colour_bg[0] = int(input("red"))
        colour_bg[1] = int(input("green"))
        colour_bg[2] = int(input("blue"))
        for i in colour_bg:
            if colour_bg[i] not in range(256):
                print("your message colour is not in RGB range")
                break
            else:
                return colour_bg
            
colour_txt = get_colour_txt()
colour_bg = get_colour_bg()
speed = float(input("Enter your text speed"))

while True:
    sense.set_rotation(rotate_int)
    sense.show_message(display_message, text_colour = colour_txt, back_colour = colour_bg, scroll_speed = speed)
    
    if not input("Would you like to print message again? (y/n)").upper().startswith('Y'):
        break
