from locale import CHAR_MAX
import sys, pygame, math

pygame.init()

size = width, height = 1000, 600
speed = [1, 1]
black = 0, 0, 0

screen = pygame.display.set_mode(size)

ball = pygame.image.load("dvd.png")
ballrect = ball.get_rect()

wall = pygame.image.load("tilefloor.jpg")
wallrect = wall.get_rect()

count = 0
char_X = 0
char_Y = 0

sqrt2 = math.sqrt(2)

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    
    keys = pygame.key.get_pressed()
    
    if keys[pygame.K_a] and keys[pygame.K_w]:
        if ballrect.left > 0 and ballrect.top > 0:
            ballrect.move_ip(-1, -1)
        elif ballrect.left > 0:
            ballrect.move_ip(-1, 0)
        elif ballrect.top > 0:
            ballrect.move_ip(0, -1)
    #if keys[pygame.K_a]:
    #    if ballrect.left > 0:
    #        ballrect.move_ip(-1, 0)
    #if keys[pygame.K_w]:
    #    if ballrect.top > 0:
    #        ballrect.move_ip(0, -1)
    if keys[pygame.K_d]:
        if ballrect.right < width:
            ballrect.move_ip(1, 0)
    if keys[pygame.K_s]:
        if ballrect.bottom < height:
            ballrect.move_ip(0, 1)

    for y in range(0, height, 400):
        for x in range(0, width, 400):
            screen.blit(wall, (x , y))
            #print(f'width: {x} height: {y}')
    
    #screen.fill(black)

    screen.blit(ball, ballrect)
    pygame.display.flip()