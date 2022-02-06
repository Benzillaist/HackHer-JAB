from concurrent.futures import wait
from locale import CHAR_MAX
import sys, pygame, time

pygame.init()

size = width, height = 1000, 1000
speed = [1, 1]
black = 0, 0, 0

cameraOff_X = 0
cameraOff_Y = 0
cameraBoarder = 50

bound_X = 1000
bound_Y = 1000

count = 0

screen = pygame.display.set_mode(size)

ball = pygame.image.load("dvd.png")
ballrect = ball.get_rect()
ballrect.move_ip(cameraBoarder, cameraBoarder)

wall = pygame.image.load("office2000.png")
#wall = pygame.transform.scale(wall, (20, 20))
wallrect = wall.get_rect()

screen.blit(wall, (0,0))

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    #time.sleep(0.001)

    keys = pygame.key.get_pressed()
    
    if keys[pygame.K_a]:
        if ballrect.left > cameraBoarder:
            ballrect.move_ip(-5, 0)
        elif cameraOff_X > cameraBoarder:
            cameraOff_X -= 1
    elif keys[pygame.K_d]:
        if ballrect.right < width - cameraBoarder:
            ballrect.move_ip(5, 0)
        elif cameraOff_X < bound_X - cameraBoarder:
            cameraOff_X += 1
    if keys[pygame.K_w]:
        if ballrect.top > cameraBoarder:
            ballrect.move_ip(0, -5)
        elif cameraOff_Y > cameraBoarder:
            cameraOff_Y -= 1
    elif keys[pygame.K_s]:
        if ballrect.bottom <= height - cameraBoarder:
            ballrect.move_ip(0, 5)
        elif cameraOff_Y < bound_Y - cameraBoarder:
            cameraOff_Y += 1

    #wall.scroll(-cameraOff_X, -cameraOff_Y)
    screen.blit(wall, (-cameraOff_X, -cameraOff_Y))
    

    screen.blit
    screen.blit(ball, ballrect)
    pygame.display.flip()