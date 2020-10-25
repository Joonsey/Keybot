import pygame, pygame.midi
pygame.midi.init()

for i in range(pygame.midi.get_count()):
    print(i, pygame.midi.get_device_info(i))

input_device = pygame.midi.Input(1)
#print(input_device.read(2)[0])