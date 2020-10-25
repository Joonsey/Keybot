import time, os, pygame, pygame.midi, pyautogui, pydirectinput, threading
from pynput.keyboard import Key, Controller
from pynput.mouse import Button, Controller as Mouse

pygame.midi.init()
mouse = Mouse()
keyboard = Controller()
my_input = pygame.midi.Input(1)


# event data is [[looks like frequency indicating wether the key is pressed or released 144 = pressed 128 = released, number of key that is being pressed on piano, force of press 0 being release, no clue what this is] some id seems to be increasing]
            

def pressKey(event, nkey, k):
    if event[0][1] == nkey:
        if getKeyStatus(event, nkey) == "down":
            pydirectinput.keyDown(k)
        else:
            pydirectinput.keyUp(k)


def getKeyStatus(event, nkey):
    if event[0][1] == nkey:
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
        if getKeyStatus(event, nkey) == "down":
            mouse.move(x, y)


def click(event, nkey):
    if event[0][1] == nkey:
        pydirectinput.doubleClick() 


def readInput(n):
    while True:
        if n.poll():
            event = n.read(2)[0]
            print("key pressed: ", event[0][1])

            while event[0][2]:
                if n.poll():
                    event = n.read(2)[0]

                threading.Thread(target=pressKey, args=(event, 21, "a")).start()
                threading.Thread(target=pressKey, args=(event, 23, "w")).start()
                threading.Thread(target=pressKey, args=(event, 24, "s")).start()
                threading.Thread(target=pressKey, args=(event, 26, "d")).start()
                threading.Thread(target=pressKey, args=(event, 28, "e")).start()
                threading.Thread(target=pressKey, args=(event, 29, "f")).start()
                    
                speed = event[0][2]/1000
                DEFAULTSPEED = 1
                
                threading.Thread(target=moveMouse, args=(event, 31, -DEFAULTSPEED, 0)).start() # move left // g
                threading.Thread(target=moveMouse, args=(event, 33, 0, DEFAULTSPEED)).start() # move down // a
                threading.Thread(target=moveMouse, args=(event, 34, 0, -DEFAULTSPEED)).start() # move up // a-sharp
                threading.Thread(target=moveMouse, args=(event, 35, DEFAULTSPEED, 0)).start() # move right // b
                


                click(event, 32) # click mouse // b-sharp
            
readInput(my_input)