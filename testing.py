from concurrent.futures import wait
from locale import CHAR_MAX
import sys, pygame, time
import ctypes

user32 = ctypes.windll.user32
screen_X = user32.GetSystemMetrics(0)
screen_Y = user32.GetSystemMetrics(1)

printerVar = 0
computerVar = 0
sexualHarassment = 0

pygame.init()

size = width, height = screen_X*0.75, screen_Y*0.75
speed = [1, 1]
black = 0, 0, 0

cameraOff_X = 0
cameraOff_Y = 0
cameraBorder = 0

count = 0

screen = pygame.display.set_mode(size)

ball = pygame.image.load("girl2.png").convert()
ballrect = ball.get_rect()
ballrect.move_ip(cameraBorder, cameraBorder)

wall = pygame.image.load("office2000.png").convert()
#wall = pygame.transform.scale(wall, (20, 20))
#wallrect = wall.get_rect()

bound_X = wall.get_width() - width
bound_Y = wall.get_height() - height

screen.blit(wall, (0,0))

# DIALOGUES

pygame.font.init()
font = pygame.font.Font('Raleway-Medium.ttf ',30)

d1 = font.render('Welcome to your new office!', True, (0,0,0))
textRect = d1.get_rect()
textRect.center = (450,550)
bound_X = wall.get_width() - width
bound_Y = wall.get_height() - height

d2 = font.render("My name is Cathy.", True, (0,0,0))
textRect2 = d2.get_rect()
textRect2.center = (450,550)

d3 = font.render("You have certain tasks to complete in each work day.", True, (0,0,0))
textRect3 = d3.get_rect()
textRect3.center = (450,550)

d4 = font.render("Your first task is printing documents using the printer at the top right of the map.", True, (0,0,0))
textRect4 = d4.get_rect()
textRect4.center = (450,550)

numPressed = 0
#bg = pygame.image.load("office2000.png")

def dialogue():
    if numPressed == 0:
        screen.blit(d1, (textRect))
    elif numPressed == 1:
        screen.blit(d2, (textRect2))
    elif numPressed == 2:
        screen.blit(d3, (textRect3))
    elif numPressed == 3:
        screen.blit(d4, (textRect4))
    elif numPressed == 4:
        screen.blit(e2, rect2)

# DIALOGUE D1S2

    #In proximity of printer

    e1 = font.render("Press P to print your documents", True, (0,0,0))
    rect = e1.get_rect()
    rect.center = (450,550)

def printerTask():
    screen.blit(e1, rect)

    #After a delay of 2 seconds - maybe loading bar?

    e2 = font.render("And you're done!", True, (0,0,0))
    rect2 = e2.get_rect()
    rect2.center = (450,550)

    #Ernest walks up and starts talking

    e3 = font.render("Ernest: Hey there! Are you the newbie?", True, (0,0,0))
    rect3 = e3.get_rect()
    rect3.center = (450,550)

    e4 = font.render("Ernest: I'm the branch manager and your boss, Ernest", True, (0,0,0))
    rect4 = e4.get_rect()
    rect4.center = (450,550)



# GAME LOOP

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    #time.sleep(0.001)

    keys = pygame.key.get_pressed()
    
    if keys[pygame.K_a]:
        if ballrect.left > cameraBorder:
            ballrect.move_ip(-1, 0)
        elif cameraOff_X > cameraBorder:
            cameraOff_X -= 5
    elif keys[pygame.K_d]:
        if ballrect.right < width - cameraBorder:
            ballrect.move_ip(1, 0)
        elif cameraOff_X < bound_X - cameraBorder:
            cameraOff_X += 5
    if keys[pygame.K_w]:
        if ballrect.top > cameraBorder:
            ballrect.move_ip(0, -1)
        elif cameraOff_Y > cameraBorder:
            cameraOff_Y -= 5
    elif keys[pygame.K_s]:
        if ballrect.bottom <= height - cameraBorder:
            ballrect.move_ip(0, 1)
        elif cameraOff_Y < bound_Y - cameraBorder:
            cameraOff_Y += 5
    if keys[pygame.K_SPACE]:
        if numPressed < 3:
            numPressed += 1
            time.sleep(0.5)
        if numPressed >= 3 and numPressed < 8 and printerTask == 1:
            numPressed+=1
            time.sleep(0.5)
    print(ballrect.center) 
    print(f'{cameraOff_X}, {cameraOff_Y}')

    screen.blit(wall, (-cameraOff_X, -cameraOff_Y))
    dialogue()

    screen.blit(ball, ballrect)
    pygame.display.flip()

    """
    if math.abs(ballrect.centerx - 657+1040) < 100 and math.abs(ballrect.centery - 331) < 100): 
        printerTask()
        if keys[pygame.K_p]:
            printerTask = 1
            dialogue()
    """ 