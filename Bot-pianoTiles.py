#have a look on the read me file before proceeding to code
from pyautogui import *
import pyautogui
import time
import keyboard
import random
import win32api, win32con

#Position of tile columns for my system 
#Tile 1 Position: X:  635 Y:  400 RGB: ( 78,  80, 113) 
#Tile 2 Position: X:  740 Y:  400 RGB: ( 78,  80, 114)
#Tile 3 Position: X:  840 Y:  400 RGB: ( 78,  80, 114)
#Tile 4 Position: X:  947 Y:  400 RGB: ( 78,  80, 114)
#defining a click function 

def click(x,y):   
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(0.1) #This pauses the script for 0.01 seconds
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)

while keyboard.is_pressed('q') == False: # press 'q' to stop the program from running 
    #replace the two cordinates according to the location of tiles on your system (Replace the cordinates for the whole code)
    if pyautogui.pixel(635, 400)[0] == 0: 
        click(635, 400)
    if pyautogui.pixel(740, 400)[0] == 0:
        click(740, 400)
    if pyautogui.pixel(840, 400)[0] == 0:
        click(840, 400)
    if pyautogui.pixel(947, 400)[0] == 0:
        click(947, 400)
    
