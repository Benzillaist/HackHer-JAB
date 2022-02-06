from concurrent.futures import wait
from locale import CHAR_MAX
import sys, pygame, time

pygame.init()

size = width, height = 800, 800
speed = [1, 1]
black = 0, 0, 0

cameraOff_X = 0
cameraOff_Y = 0
cameraBorder = 50

bound_X = 1000
bound_Y = 1000

count = 0

screen = pygame.display.set_mode(size)

ball = pygame.image.load("girl1.png").convert()
ballrect = ball.get_rect()
ballrect.move_ip(cameraBorder, cameraBorder)

wall = pygame.image.load("office2000.png").convert()
#wall = pygame.transform.scale(wall, (20, 20))
#wallrect = wall.get_rect()

screen.blit(wall, (0,0))

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    #time.sleep(0.001)

    keys = pygame.key.get_pressed()
    
    if keys[pygame.K_a]:
        if ballrect.left > cameraBorder:
            ballrect.move_ip(-5, 0)
        elif cameraOff_X > cameraBorder:
            cameraOff_X -= 5
    elif keys[pygame.K_d]:
        if ballrect.right < width - cameraBorder:
            ballrect.move_ip(5, 0)
        elif cameraOff_X < bound_X - cameraBorder:
            cameraOff_X += 5
    if keys[pygame.K_w]:
        if ballrect.top > cameraBorder:
            ballrect.move_ip(0, -5)
        elif cameraOff_Y > cameraBorder:
            cameraOff_Y -= 5
    elif keys[pygame.K_s]:
        if ballrect.bottom <= height - cameraBorder:
            ballrect.move_ip(0, 5)
        elif cameraOff_Y < bound_Y - cameraBorder:
            cameraOff_Y += 5

    screen.blit(wall, (-cameraOff_X, -cameraOff_Y))

    screen.blit(ball, ballrect)
    pygame.display.flip()