from concurrent.futures import wait
from locale import CHAR_MAX
import sys, pygame, time, math
import ctypes

user32 = ctypes.windll.user32
screen_X = user32.GetSystemMetrics(0)
screen_Y = user32.GetSystemMetrics(1)

printerVar = 0
computerVar = 0
sexualHarassment = 0
looped = 0

pygame.init()

size = width, height = screen_X*0.75, screen_Y*0.75
speed = [1, 1]
black = 0, 0, 0

cameraOff_X = 0
cameraOff_Y = 0
cameraBorder = 100

count = 0

screen = pygame.display.set_mode(size)

ball = pygame.image.load("girl2.png").convert()
ballrect = ball.get_rect()
ballrect.move_ip(cameraBorder, cameraBorder)

wall = pygame.image.load("office2000.png").convert()

ernest = pygame.image.load("ernest2.png").convert()
ernestrect = ernest.get_rect()

bound_X = wall.get_width() - width
bound_Y = wall.get_height() - height

screen.blit(wall, (0,0))

bound_X = wall.get_width() - width
bound_Y = wall.get_height() - height

# DIALOGUES

pygame.font.init()
font = pygame.font.Font('Raleway-Black.ttf',30)

print(f'{0.5*screen_X} {0.85*screen_Y}')

d1 = font.render('Welcome to your new office! {Press the spacebar to cycle through dialogue}', True, (0,0,0))
textRect = d1.get_rect()
textRect.center = (0.5*width, 0.85*height)

d2 = font.render("My name is Cathy.", True, (0,0,0))
textRect2 = d2.get_rect()
textRect2.center = (0.5*width, 0.85*height)

d3 = font.render("You have certain tasks to complete in each work day.", True, (0,0,0))
textRect3 = d3.get_rect()
textRect3.center = (0.5*width, 0.85*height)

d4 = font.render("Your first task is printing documents using the printer at the top right of the map.", True, (0,0,0))
textRect4 = d4.get_rect()
textRect4.center = (0.5*width, 0.85*height)

e1 = font.render("Press P to print your documents", True, (0,0,0))
rect = e1.get_rect()
rect.center = (0.5*width, 0.85*height)

e2 = font.render("And you're done!", True, (0,0,0))
rect2 = e2.get_rect()
rect2.center = (0.5*width, 0.85*height)

e3 = font.render("Ernest: Hey there! Are you the newbie?", True, (0,0,0))
rect3 = e3.get_rect()
rect3.center = (0.5*width, 0.85*height)

e4 = font.render("Ernest: I'm the branch manager and your boss, Ernest", True, (0,0,0))
rect4 = e4.get_rect()
rect4.center = (0.5*width, 0.85*height)

e5 = font.render("Ernest: Woah, you have the prettiest eyes I've ever seen.", True, (0,0,0))
rect5 = e5.get_rect()
rect5.center = (0.5*width, 0.85*height)

e6 = font.render("You: Um... thank you?", True, (0,0,0))
rect6 = e6.get_rect()
rect6.center = (0.5*width, 0.85*height)

f1 = font.render("Day 2: Head over to the top-most desk in the middle column and finish your computer task", True, (0,0,0))
rectangle1 = f1.get_rect()
rectangle1.center = (0.5*width, 0.85*height)

f2 = font.render("Press C to work on your computer.", True, (0,0,0))
rectangle2 = f2.get_rect()
rectangle2.center = (0.5*width, 0.85*height)

f3 = font.render("Ernest: Are you sure you can handle that task?", True, (0,0,0))
rectangle3 = f3.get_rect()
rectangle3.center = (0.5*width, 0.85*height)

f4 = font.render("Ernest: Here, let me take a look.", True, (0,0,0))
rectangle4 = f4.get_rect()
rectangle4.center = (0.5*width, 0.85*height)

f5 = font.render("Ernest: You know, you should smile more.", True, (0,0,0))
rectangle5 = f5.get_rect()
rectangle5.center = (0.5*width, 0.85*height)

g1 = font.render("Day 3: Head over to the coffee machine and brew some coffee.", True, (0,0,0))
rectang1 = g1.get_rect()
rectang1.center = (0.5*width, 0.85*height)

g2 = font.render("Press C to make some coffee", True, (0,0,0))
rectang2 = g2.get_rect()
rectang2.center = (0.5*width, 0.85*height)

g3 = font.render("[Ernest places his hand on your shoulder.]", True, (0,0,0))
rectang3 = g3.get_rect()
rectang3.center = (0.5*width, 0.85*height)

g4 = font.render("Ernest: You look nice today.", True, (0,0,0))
rectang4 = g4.get_rect()
rectang4.center = (0.5*width, 0.85*height)

g5 = font.render("Ernest: We could go out sometime.", True, (0,0,0))
rectang5 = g5.get_rect()
rectang5.center = (0.5*width, 0.85*height)

g6 = font.render("You feel that this has gone too far. Press R to report Ernest to HR OR Press I to ignore him.", True, (0,0,0))
rectang6 = g6.get_rect()
rectang6.center = (0.5*width, 0.85*height)

g7 = font.render("HR: Thank you for your report, we will investigate and get back to you later", True, (0,0,0))
rectang7 = g7.get_rect()
rectang7.center = (0.5*width, 0.85*height)

g8 = font.render("Press C to confront or R to resign", True, (0,0,0))
rectang8 = g8.get_rect()
rectang8.center = (0.5*width, 0.85*height)

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
        screen.blit(e1, rect)
    elif numPressed == 5:
        screen.blit(e2, rect2)
    elif numPressed == 6:
        screen.blit(e3, rect3)
    elif numPressed == 7:
        screen.blit(e4, rect4)
    elif numPressed == 8:
        screen.blit(e5, rect5)
    elif numPressed == 9:
        screen.blit(e6, rect6)
    elif numPressed == 10:
        screen.blit(f1, rectangle1)
    elif numPressed == 11:
        screen.blit(f2, rectangle2)
    elif numPressed == 12:
        screen.blit(f3, rectangle3)
    elif numPressed == 13:
        screen.blit(f4, rectangle4)
    elif numPressed == 14:
        screen.blit(f5, rectangle5)
    elif numPressed == 15:
        screen.blit(g1, rectang1)
    elif numPressed == 16:
        screen.blit(g2, rectang2)
    elif numPressed == 17:
        screen.blit(g3, rectang3)
    elif numPressed == 18:
        screen.blit(g4, rectang4)
    elif numPressed == 19:
        screen.blit(g5, rectang5)
    elif numPressed == 20 and looped == 0:
        screen.blit(g6, rectang6)
    elif numPressed == 21 and looped == 0:
        screen.blit(g7, rectang7)
    elif numPressed == 20 and looped == 1:
        screen.blit(g8, rectang8)

# DIALOGUE D1S2

    #In proximity of printer


def printerText():
    screen.blit(e1, rect)

# GAME LOOP

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    #time.sleep(0.001)
    print(looped)
    keys = pygame.key.get_pressed()
    if(numPressed < 5 or numPressed == 9 or numPressed == 10 or numPressed == 14 or numPressed == 15):
        if keys[pygame.K_a]:
            if ballrect.left > cameraBorder:
                ballrect.move_ip(-1, 0)
            elif cameraOff_X > cameraBorder:
                cameraOff_X -= 1
        elif keys[pygame.K_d]:
            if ballrect.right < width - cameraBorder:
                ballrect.move_ip(1, 0)
            elif cameraOff_X < bound_X - cameraBorder:
                cameraOff_X += 1
        if keys[pygame.K_w]:
            if ballrect.top > cameraBorder:
                ballrect.move_ip(0, -1)
            elif cameraOff_Y > cameraBorder:
                cameraOff_Y -= 1
        elif keys[pygame.K_s]:
            if ballrect.bottom <= height - cameraBorder:
                ballrect.move_ip(0, 1)
            elif cameraOff_Y < bound_Y - cameraBorder:
                cameraOff_Y += 1
    
    print(f'numpressed: {numPressed}')

    if keys[pygame.K_SPACE]:
        if numPressed < 3:
            numPressed += 1
            time.sleep(0.5)
        elif numPressed >= 5 and numPressed <=8 and printerVar == 1:
            numPressed += 1
            time.sleep(0.5)
        elif numPressed == 9:
            numPressed += 1
            ball = pygame.image.load("girl2.png").convert()
            ballrect = ball.get_rect()
            ballrect.move_ip(cameraBorder, cameraBorder)
            cameraOff_X = 0
            cameraOff_Y = 0
            time.sleep(0.5)
        elif numPressed >= 11 and numPressed < 14 and computerVar == 1:
            numPressed+=1
            time.sleep(0.5)
        elif numPressed == 14:
            numPressed += 1
            ball = pygame.image.load("girl2.png").convert()
            ballrect = ball.get_rect()
            ballrect.move_ip(cameraBorder, cameraBorder)
            cameraOff_X = 0
            cameraOff_Y = 0
            time.sleep(0.5)
        elif numPressed >= 17 and numPressed < 20 and sexualHarassment == 1:
            numPressed+=1
            time.sleep(0.5)

    if abs(ballrect.centerx + cameraOff_X - 1697) < 100 and abs(ballrect.centery + cameraOff_Y - 331) < 100:
        printerText()
        if numPressed == 3:
            numPressed += 1
        if keys[pygame.K_p] and numPressed == 4:
            numPressed += 1
            printerVar = 1
            time.sleep(0.5)

    if abs(ballrect.centerx + cameraOff_X - 750) < 100 and abs(ballrect.centery + cameraOff_Y - 800) < 100:
        if numPressed == 10:
            numPressed += 1 # go to the computer and send your emails
            time.sleep(0.5) 
        if keys[pygame.K_c] and numPressed == 11:
            numPressed += 1
            computerVar = 1
            time.sleep(0.5)

    if abs(ballrect.centerx - 429) < 100 and abs(ballrect.centery - 181) < 100:
        if numPressed == 15:
            numPressed += 1
            time.sleep(0.5)
        if keys[pygame.K_c] and numPressed == 16:
            numPressed += 1
            sexualHarassment = 1
            time.sleep(0.5)

    if sexualHarassment == 1 and looped == 0:
        if keys[pygame.K_r]:
            sexualHarassment = 0
            numPressed += 1
            # nothing happens loop back to the start of day 3
            screen.blit(wall, (-cameraOff_X, -cameraOff_Y))
            if numPressed >= 4 and numPressed < 10:
                screen.blit(pygame.transform.rotate(ernest, 180), (width + 200 - cameraOff_X, 50 - cameraOff_Y))
            if numPressed >= 11 and numPressed < 15:
                screen.blit(ernest, (bound_X + 175 - cameraOff_X, height - 50 - cameraOff_Y))
            if numPressed >= 16 and numPressed <= 20:
                screen.blit(pygame.transform.rotate(ernest, 90), (450 - cameraOff_X, 100 - cameraOff_Y))
            screen.blit(ball, ballrect)
            dialogue()
            pygame.display.flip()
            time.sleep(5)
            numPressed = 15
            ball = pygame.image.load("girl2.png").convert()
            ballrect = ball.get_rect()
            ballrect.move_ip(cameraBorder, cameraBorder)
            cameraOff_X = 0
            cameraOff_Y = 0
            looped = 1
        if keys[pygame.K_i]:
            # nothing happens loop back to the start of day 3
            sexualHarassment = 0
            numPressed = 15
            ball = pygame.image.load("girl2.png").convert()
            ballrect = ball.get_rect()
            ballrect.move_ip(cameraBorder, cameraBorder)
            cameraOff_X = 0
            cameraOff_Y = 0
            looped = 1


    if looped == 1 and numPressed == 20:
        if keys[pygame.K_c] or keys[pygame.K_r]:
            wall = pygame.image.load("ulost.png").convert()

    screen.blit(wall, (-cameraOff_X, -cameraOff_Y))
    if numPressed >= 4 and numPressed < 10:
        screen.blit(pygame.transform.rotate(ernest, 180), (width + 200 - cameraOff_X, 50 - cameraOff_Y))
    if numPressed >= 11 and numPressed < 15:
        screen.blit(ernest, (bound_X + 175 - cameraOff_X, height - 50 - cameraOff_Y))
    if numPressed >= 16 and numPressed <= 20:
        screen.blit(pygame.transform.rotate(ernest, 90), (450 - cameraOff_X, 100 - cameraOff_Y))
    screen.blit(ball, ballrect)
    dialogue()
    pygame.display.flip()

    """
    # after the sexual harassment occurs on the third day, press R to report to HR and press I to ignore
    while sexualHarassment = 1:
        if keys[pygame.K_r]:
            # nothing happens loop back to the start of day 3
            sexualHarassment = 0
        if keys[pygame.K_i]:
            # nothing happens loop back to the start of day 3
            sexualHarassment = 0
    """
    """
    while loop to be fixed 
        if keys[pygame.K_c]:
            jobless = 1 
            if jobless = 1:
                # switch to a display that says game over 
        if keys[pygame.K_r]:
            jobless = 1
            if jobless = 1:
                # switch to a display that says game over 
    """