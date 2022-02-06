from concurrent.futures import wait
from locale import CHAR_MAX
import sys, pygame, time

pygame.init()

size = width, height = 900, 600
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

# DIALOGUES

pygame.font.init()
font = pygame.font.Font('Raleway-Medium.ttf ',30)

d1 = font.render('Welcome to your new office!', True, (0,0,0))
textRect = d1.get_rect()
textRect.center = (450,550)

d2 = font.render("My name is Cathy.", True, (0,0,0))
textRect2 = d2.get_rect()
textRect2.center = (450,550)

numPressed = 0
bg = pygame.image.load("office2000.png")

def dialogue():
    screen.blit(bg,(0,0))
    if numPressed == 0:
        screen.blit(d1, (textRect))
    elif numPressed == 1:
        screen.blit(d2, (textRect2))

# GAME LOOP 

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    #time.sleep(0.001)

    keys = pygame.key.get_pressed()
    
    if keys[pygame.K_SPACE]:
        numPressed+=1
        time.sleep(0.5)
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
    dialogue()

    screen.blit(ball, ballrect)
    pygame.display.flip()