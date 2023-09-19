import pygame

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


def player(x, y): 
    screen.blit(playerImg, (x, y))

# Game Loop

running = True
while running:

    # RGB parameters
    screen.fill((255, 0, 255))
    playerX -= 0.1
    print(playerX)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


    player(playerX, playerY)
    pygame.display.update()

pygame.quit()