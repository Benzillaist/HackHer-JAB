from threading import Timer
import pygame
pygame.init()
screen = pygame.display.set_mode((900,600))

# NAME AND BACKGROUND
pygame.display.set_caption('Workplace Sim')
bg = pygame.image.load("office2000.png")

# DIALOGUE - D1S1
pygame.font.init()
font = pygame.font.SysFont('Arial',30)

d1 = font.render('Press the spacebar to cycle through dialogue.', True, (0,0,0))
textRect = d1.get_rect()
textRect.center = (0.5*screen_X, 0.85*screen_Y)

d2 = font.render("Welcome to your new office!", True, (0,0,0))
textRect2 = d2.get_rect()
textRect2.center = (0.5*screen_X, 0.85*screen_Y)

d3 = font.render("You have certain tasks to complete in each work day.", True, (0,0,0))
textRect3 = d3.get_rect()
textRect3.center = (0.5*screen_X, 0.85*screen_Y)

d4 = font.render("Your first task is printing documents using the printer at the top right of the map.", True, (0,0,0))
textRect4 = d4.get_rect()
textRect4.center = (0.5*screen_X, 0.85*screen_Y)

# DIALOGUE D1S2

#In proximity of printer

e1 = font.render("Press P to print your documents", True, (0,0,0))
rect = e1.get_rect()
rect.center = (0.5*width, 0.85*screen_Y)

#After a delay of 2 seconds - maybe loading bar?
e2 = font.render("And you're done!", True, (0,0,0))
rect2 = e2.get_rect()
rect2.center = (0.5*screen_X, 0.85*screen_Y)

#Ernest walks up and starts talking

e3 = font.render("Ernest: Hey there! Are you the newbie?", True, (0,0,0))
rect3 = e3.get_rect()
rect3.center = (0.5*screen_X, 0.85*screen_Y)

e4 = font.render("Ernest: I'm the branch manager and your boss, Ernest", True, (0,0,0))
rect4 = e4.get_rect()
rect4.center = (0.5*screen_X, 0.85*screen_Y)

e5 = font.render("Ernest: Woah, you have the prettiest eyes I've ever seen.", True, (0,0,0))
rect5 = e5.get_rect()
rect5.center = (0.5*screen_X, 0.85*screen_Y)

e6 = font.render("You: Um... thank you?", True, (0,0,0))
rect6 = e6.get_rect()
rect6.center = (0.5*screen_X, 0.85*screen_Y)

# DIALOGUE - D2 Computer Task
f1 = font.render("Day 2: Head over to the top-most desk in the right column and finish your computer task", True, (0,0,0))
rectangle1 = f1.get_rect()
rectangle1.center = (0.5*screen_X, 0.85*screen_Y)

f2 = font.render("Press C to work on your computer.", True, (0,0,0))
rectangle2 = f2.get_rect()
rectangle2.center = (0.5*screen_X, 0.85*screen_Y)

#Ernest walks over what a bitch

f3 = font.render("Ernest: Are you sure you can handle that task?", True, (0,0,0))
rectangle3 = f3.get_rect()
rectangle3.center = (0.5*screen_X, 0.85*screen_Y)

f4 = font.render("Ernest: Here, let me take a look.", True, (0,0,0))
rectangle4 = f4.get_rect()
rectangle4.center = (0.5*screen_X, 0.85*screen_Y)

f5 = font.render("Ernest: You know, you should smile more.", True, (0,0,0))
rectangle5 = f5.get_rect()
rectangle5.center = (0.5*screen_X, 0.85*screen_Y)

# DIALOGUE - D3 Coffee Machine

g1 = font.render("Day 3: Head over to the coffee machine and brew some coffee.", True, (0,0,0))
rectang1 = g1.get_rect()
rectang1.center = (0.5*width, 0.85*height)

g2 = font.render("[Ernest places his hand on your shoulder.]", True, (0,0,0))
rectang2 = g2.get_rect()
rectang2.center = (0.5*width, 0.85*height)

g3 = font.render("Ernest: You look nice today.", True, (0,0,0))
rectang3 = g3.get_rect()
rectang3.center = (0.5*width, 0.85*height)

g4 = font.render("Ernest: We could go out sometime.", True, (0,0,0))
rectang4 = g4.get_rect()
rectang4.center = (0.5*width, 0.85*height)

g5 = font.render("You feel that this has gone too far. Press R to report Ernest to HR OR Press I to ignore him.", True, (0,0,0))
rectang5 = g5.get_rect()
rectang5.center = (0.5*width, 0.85*height)


numPressed = 0
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
        screen.blit(e2, (rect2))
    elif numPressed == 5:
        screen.blit(e3, (rect3))
    elif numPressed == 6:
        screen.blit(e4, (rect4))
    elif numPressed == 7:
        screen.blit(e5, (rect5))
    elif numPressed == 8:
        screen.blit(e6, (rect6))

# THE GAME LOOP
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                dialogue()
                numPressed += 1

    pygame.display.flip()