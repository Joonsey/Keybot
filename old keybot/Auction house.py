from pynput.keyboard import Key, Controller
keyboard = Controller()
while True:
    keyboard.press(Key.ctrl)