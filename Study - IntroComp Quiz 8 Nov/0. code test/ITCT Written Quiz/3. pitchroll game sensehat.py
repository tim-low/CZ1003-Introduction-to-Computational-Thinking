# -*- coding: utf-8 -*-
"""
Created on Mon Nov  5 10:08:31 2018

@author: Tim
"""

#1. Board, Marble, 1D, Pitch/Roll
from sense_hat import SenseHat
sense = SenseHat()

b = (0,0,0)
w = (255,255,255)

board = [[b,b,b,b,b,b,b,b],
         [b,b,b,b,b,b,b,b],
         [b,b,b,b,b,b,b,b],
         [b,b,b,b,b,b,b,b],
         [b,b,b,b,b,b,b,b],
         [b,b,b,b,b,b,b,b],
         [b,b,b,b,b,b,b,b],
         [b,b,b,b,b,b,b,b]]

y = 2
x = 2
board[y][x] = w

board_1D = sum(board,[])
sense.set_pixels(board_1D)

def move_marble(pitch, roll, x, y):
    new_x = x
    new_y = y
    if 1 < pitch <179 and x !=0:
        new_x -= 1
    elif 179 < pitch < 359 and x!= 7:
        new_x += 1
    
    if 1 < roll <179 and x !=7:
        new_x += 1
    elif 179 < roll < 359 and x!= 0:
        new_x -= 1 
    
    return new_x, new_y

while True:
    pitch = sense.get_orientation()['pitch']
    roll = sense.get_orientation()['roll']
    
    board[y][x] = b
    x,y = move_marble(pitch,roll,x,y)
    board[y][x] = w
    sense.set_pixels(sum(board,[]))
    sleep(0.05)
