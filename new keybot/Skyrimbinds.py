import time, os, pygame, pygame.midi, pyautogui
from pynput.keyboard import Key, Controller

pygame.midi.init()
keyboard = Controller()
my_input = pygame.midi.Input(1)

# event data is [[looks like frequency indicating wether the key is pressed or released 144 = pressed 128 = released, number of key that is being pressed on piano, force of press 0 being release, no clue what this is] some id seems to be increasing]
            

def pressKey(event, nkey, k):
    if event[0][1] == nkey:
        if getKeyStatus(event) == "down":
            keyboard.press(str(k))
        else:
            keyboard.release(str(k))


def getKeyStatus(event):
    if event[0][2] > 0:
        keyStatus = "down"
    else:
        keyStatus = "up"
    return keyStatus


def isHolding(event):
    holding = False
    while event[0][2] > 0:
        holding = True
    return holding


def updateInput(n):
    return n.read(2)[0]


def moveMouse(event, nkey, x, y):
    if event[0][1] == nkey:
        if getKeyStatus(event) == "down":
            pyautogui.moveRel(x, y)
    

def click(event, nkey):
    if event[0][1] == nkey:
        pyautogui.click(pyautogui.position()) 


def readInput(n):
    while True:
        if n.poll():
            event = n.read(2)[0]
            print("key pressed: ", event[0][1])
            pressKey(event, 21, "a")
            pressKey(event, 23, "b")
            pressKey(event, 24, "c")
            pressKey(event, 26, "d")
            pressKey(event, 28, "e")
            pressKey(event, 29, "f")
            while event[0][0] == 144:
                if n.poll():
                    event = n.read(2)[0]
                    
                speed = event[0][2]
                #DEFAULTSPEED = 50
                moveMouse(event, 31, -speed, 0) # move left
                moveMouse(event, 33, 0, speed) # move down
                moveMouse(event, 35, 0, -speed) # move up
                moveMouse(event, 36, speed, 0) # move right
            click(event, 32)
            
readInput(my_input)