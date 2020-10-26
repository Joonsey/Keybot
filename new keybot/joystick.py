from inputs import devices, get_gamepad, keyboard, random, win32api, win32con

for d in devices:
    print(d)

def clickKey()
while 1:
    events = get_gamepad()
    for event in events:
        print(event.code, event.state)
        if event.code == "ABS_TL" and event.state == 1:
