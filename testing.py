import sys, pygame

pygame.init()

size = width, height = 1000, 600
speed = [1, 1]
black = 0, 0, 0

screen = pygame.display.set_mode(size)

ball = pygame.image.load("dvd.png")
ballrect = ball.get_rect()

count = 0

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    
    keys = pygame.key.get_pressed()
    
    if keys[pygame.K_a]:
        print("Testa")
        if ballrect.left > 0:
            ballrect.move_ip(-1, 0)
    if keys[pygame.K_w]:
        print("Tests")
        if ballrect.top > 0:
            ballrect.move_ip(0, -1)
    if keys[pygame.K_d]:
        print("Testd")
        if ballrect.right < width:
            ballrect.move_ip(1, 0)
    if keys[pygame.K_s]:
        print("Tests")
        if ballrect.bottom < height:
            ballrect.move_ip(0, 1)


    screen.fill(black)
    screen.blit(ball, ballrect)
    pygame.display.flip()