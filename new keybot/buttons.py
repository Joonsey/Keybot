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
        self.queue = []
        self.queuelock = threading.Lock()
        threading.Thread(target=self.getInput).start()
        threading.Thread(target=self.main).start()



    def update(self, piano):
        while True:
            if piano.poll():
                
                event = piano.read(2)[0]
                return event    

    def checkKey(self, event, pianokey):
        if event[1] == pianokey:
            
            return True
        else:
            return False

    def keystatus(self, event):
        keystatus = ""
        if event[0] == 128:
            print('released')
            keystatus = "up"
        elif event[0] == 144:
            keystatus = "down"
        return keystatus

    def pressKey(self, event):
        if event[1] == self.pianokey:
            if self.keystatus(event) == 'down':
                pydirectinput.keyDown(self.key)
            elif self.keystatus(event) == 'up': 
                pydirectinput.keyUp(self.key)
            else:
                pass


    def getInput(self):
        while True:
            if self.piano.poll():
                event = self.piano.read(2)[0]
                with self.queuelock:
                    self.queue.append(event[0])
                    print('added ', event[0], ' to the queue')
                
                

    def main(self):
        while True:
            if len(self.queue) > 0:
                with self.queuelock:
                    print(self.queue)
                    self.pressKey(self.queue.pop())



a = button('a',21, my_input)
b = button('b',23, my_input)



#my_input.close()



