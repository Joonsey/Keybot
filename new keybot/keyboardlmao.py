from pynput.keyboard import Key, Controller
import pygame.midi
import time
keyboard = Controller()

def readInput(input_device):
    while True:
        if input_device.poll():
            event = input_device.read(2)[0]
            #print ("Raw input: ", event)
            keyVal = event[0][1]
            print(keyVal)
            print(event)
            keyStatus = ""
            if(keyVal != 64 and keyVal != 67):
                keyStatusInt = event[0][0]
                if(keyStatusInt == 144): keyStatus = "down"
                if(keyStatusInt == 128): keyStatus = "up"
                #print(keyStatusInt)
            else:
                if(event[0][2] > 0):
                    keyStatus = "down"
                else: keyStatus = "up"

            # movement

            if keyVal == 23:
                if(keyStatus == "down"): keyboard.press('w')
                elif(keyStatus == "up"): keyboard.release('w')
            if keyVal == 38:
                if(keyStatus == "down"): keyboard.press('s')
                elif(keyStatus == "up"): keyboard.release('s')
            if keyVal == 21:
                if(keyStatus == "down"): keyboard.press('a')
                elif(keyStatus == "up"): keyboard.release('a')
            if keyVal == 24:
                if(keyStatus == "down"): keyboard.press('d')
                elif(keyStatus == "up"): keyboard.release('d')
            if keyVal == 22:
                if(keyStatus == "down"): keyboard.press(Key.space)
                elif(keyStatus == "up"): keyboard.release(Key.space)

            # target

            if keyVal == 39:
                if(keyStatus == "down"): keyboard.press(Key.tab)
                elif(keyStatus == "up"): keyboard.release(Key.tab)

            # rotation
            
            if keyVal == 40:
                if(keyStatus == "down"): keyboard.press("1")
                elif(keyStatus == "up"): keyboard.release("1")
            if keyVal == 41:
                if(keyStatus == "down"): keyboard.press("2")
                elif(keyStatus == "up"): keyboard.release("2")
            if keyVal == 42:
                if(keyStatus == "down"): keyboard.press("3")
                elif(keyStatus == "up"): keyboard.release("3")
            if keyVal == 43:
                if(keyStatus == "down"): keyboard.press("4")
                elif(keyStatus == "up"): keyboard.release("4")
            if keyVal == 45:
                if(keyStatus == "down"): keyboard.press("5")
                elif(keyStatus == "up"): keyboard.release("5")

            # league taster

            if keyVal == 28:
                if(keyStatus == "down"): keyboard.press("q")
                elif(keyStatus == "up"): keyboard.release("q")
            if keyVal == 29:
                if(keyStatus == "down"): keyboard.press("w")
                elif(keyStatus == "up"): keyboard.release("w")
            if keyVal == 31:
                if(keyStatus == "down"): keyboard.press("e")
                elif(keyStatus == "up"): keyboard.release("e")
            if keyVal == 33:
                if(keyStatus == "down"): keyboard.press("r")
                elif(keyStatus == "up"): keyboard.release("r")
            if keyVal == 30:
                if(keyStatus == "down"): keyboard.press("d")
                elif(keyStatus == "up"): keyboard.release("d")
            if keyVal == 32:
                if(keyStatus == "down"): keyboard.press("f")
                elif(keyStatus == "up"): keyboard.release("f")

            # type

            if keyVal == 26:
                keyboard.press(Key.enter)
                keyboard.release(Key.enter)
                #keyboard.type("haha this worked lmao")
                keyboard.press(Key.enter)
                keyboard.release(Key.enter)
if __name__ == '__main__':
    print("pogs")
    pygame.midi.init()
    my_input = pygame.midi.Input(1) #only in my case the id is 2
    readInput(my_input)

#def print_devices():
#    for n in range(pygame.midi.get_count()):
#        print (n,pygame.midi.get_device_info(n))
#
#pygame.midi.init()
#print_devices()aaddaad