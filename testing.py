from locale import CHAR_MAX
import sys, pygame, math

pygame.init()

size = width, height = 1000, 600
speed = [1, 1]
black = 0, 0, 0

cameraOff_X = 0
cameraOff_Y = 0
cameraBoarder = 50

bound_X = 1000
bound_Y = 1000

screen = pygame.display.set_mode(size)

ball = pygame.image.load("dvd.png")
ballrect = ball.get_rect()
ballrect.move_ip(cameraBoarder, cameraBoarder)

wall = pygame.image.load("tilefloor.jpg")
wallrect = wall.get_rect()


while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    keys = pygame.key.get_pressed()
    
    if keys[pygame.K_a]:
        if ballrect.left > cameraBoarder:
            ballrect.move_ip(-1, 0)
        elif cameraOff_X > cameraBoarder:
            cameraOff_X -= 1
    if keys[pygame.K_w]:
        if ballrect.top > cameraBoarder:
            ballrect.move_ip(0, -1)
        elif cameraOff_Y > cameraBoarder:
            cameraOff_Y -= 1
    if keys[pygame.K_d]:
        if ballrect.right < width - cameraBoarder:
            ballrect.move_ip(1, 0)
        elif cameraOff_X < bound_X - cameraBoarder:
            cameraOff_X += 1
    if keys[pygame.K_s]:
        if ballrect.bottom <= height - cameraBoarder:
            ballrect.move_ip(0, 1)
        elif cameraOff_Y < bound_Y - cameraBoarder:
            cameraOff_Y += 1

    for y in range(0, bound_Y + height, ball.get_height()):
        for x in range(0, bound_X + width, ball.get_width()):
            screen.blit(wall, (x - cameraOff_X, y - cameraOff_Y))

    screen.blit(ball, ballrect)
    pygame.display.flip()