import pygame, sys
pygame.init()

black=(255,255,255)
red=(255,0,0)
white=(0,0,0)

size=(800,500)
screen=pygame.display.set_mode(size)

while True:
    for event in pygame.event.get():
        print(event)
        if event.type == pygame .QUIT:
            sys.exit()

    clock=pygame.time.Clock()
    pygame.display.flip()
    clock.tick(60)