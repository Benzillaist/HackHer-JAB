from threading import Timer
import pygame
pygame.init()
screen = pygame.display.set_mode((900,600))

# NAME AND BACKGROUND
pygame.display.set_caption('Workplace Sim')
bg = pygame.image.load("office2000.png")

# DIALOGUE BOXES
pygame.font.init()
font = pygame.font.SysFont('Arial',30)

d1 = font.render('Press the spacebar to cycle through dialogue.', True, (0,0,0))
textRect = d1.get_rect()
textRect.center = (450,550)

d2 = font.render("Welcome to your new office!", True, (0,0,0))
textRect2 = d2.get_rect()
textRect2.center = (450,550)

d3 = font.render("My name is Cathy.", True, (0,0,0))
textRect3 = d3.get_rect()
textRect3.center = (450,550)

d4 = font.render("You have certain tasks to complete in each work day.", True, (0,0,0))
textRect4 = d4.get_rect()
textRect4.center = (450,550)

d5 = font.render("Your first task is printing documents using the printer at the top right of the map.", True, (0,0,0))
textRect5 = d5.get_rect()
textRect5.center = (450,550)

numPressed = 0

def dialogue():
    screen.blit(bg,(0,0))
    if numPressed == 0:
        screen.blit(d1, (textRect))
    elif numPressed == 1:
        screen.blit(d2, (textRect2))
    elif numPressed == 2:
        screen.blit(d3, (textRect3))
    elif numPressed == 3:
        screen.blit(d4, (textRect4))
    elif numPressed == 4:
        screen.blit(d5, (textRect5))


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