import pygame
import random

# Initialize pygame
pygame.init()

# create the screen
screen = pygame.display.set_mode((800, 600))

# Caption and Icon
pygame.display.set_caption(" 🚀 Space Invaders 👾")
icon = pygame.image.load('spaceship.png')
pygame.display.set_icon(icon)

# Player
playerImg = pygame.image.load('space-invaders.png')
playerX = 370
playerY = 480
playerX_change = 0


# Enemy
enemyImg = pygame.image.load('enemy.png')
enemyX = random.randint(0, 800)
enemyY = random.randint(50, 150)
enemyX_change = 0.8
enemyY_change = 40



def player(x, y): 
    screen.blit(playerImg, (x, y))


def enemy(x, y): 
    screen.blit(enemyImg, (x, y))

# Game Loop

running = True
while running:

    # RGB parameters
    screen.fill((255, 0, 255))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


        # if keystroke is pressed, check if it's right or left
        if event.type == pygame.KEYDOWN:
            print ("A keystroke is pressed")
            if event.key == pygame.K_LEFT:
                playerX_change = -1
            if event.key == pygame.K_RIGHT:
                playerX_change = 1
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0


    # set player boundaries
    playerX += playerX_change

    if playerX <= 0:
        playerX = 0
    elif playerX >= 736:
        playerX = 736


    # set enemy boundaries
    enemyX += enemyX_change

    if enemyX <= 0:
        enemyX_change = 0.8
        enemyY += enemyY_change
    elif enemyX >= 736:
        enemyX_change = -0.8
        enemyY += enemyY_change

    player(playerX, playerY)
    enemy(enemyX, enemyY)
    pygame.display.update()

pygame.quit()