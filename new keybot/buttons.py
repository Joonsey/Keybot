import time, os, pygame, pygame.midi, pyautogui, pydirectinput, threading
from pynput.keyboard import Key, Controller
from pynput.mouse import Button, Controller as Mouse
pygame.midi.init()
my_input = pygame.midi.Input(1)




class button:
    def __init__(self, key, pianokey, piano):
        self.key = key
        self.pianokey = pianokey
        self.piano = piano
        threading.Thread(target=self.main).start()
        


    def update(self, piano):
        while True:
            if piano.poll():
                print("updating...")
                event = piano.read(2)[0]
                return event    

    def checkKey(self, event, pianokey):
        if event[0][1] == pianokey:
            print("checking key")
            return True
        else:
            return False

    def getKeyStatus(self, event, pianokey):
        if self.checkKey(event, pianokey):
            while event[0][2]:
                self.keyStatus = True
                print('pressed')
            else:
                self.keyStatus = False
                print('released')
            return self.keyStatus

    def pressKey(self, event):
        if event[0][1] == self.pianokey:
            print(f"{self.pianokey} was pressed")
            if self.getKeyStatus(event, self.pianokey):
                pydirectinput.keyDown(self.key)
            else: 
                pydirectinput.keyUp(self.key)


    def main(self):
        while True:
            if self.piano.poll():
                event = self.piano.read(2)[0]
                while event[0][2] and self.checkKey(event, self.pianokey):
                    try:
                        event = self.piano.read(2)[0]
                    except:
                        pass
                    self.pressKey(event)
                    print(event)

            


a = button('a',21, my_input)
b = button('b',23, my_input)

#my_input.close()



