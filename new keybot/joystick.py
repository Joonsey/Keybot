import pygame.joystick
pygame.joystick.init()
joysticks = [pygame.joystick.Joystick(x) for x in range(pygame.joystick.get_count())]
pygame.init()
def pog(controller):
    while True:
        print(controller.get_axis(0))
        print(controller.get_button(0))

m = joysticks[0]
m.init()
print(m.get_numbuttons())
print(m.get_name())






print(pygame.event.pump())


#pog(m)