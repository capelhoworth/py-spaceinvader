import pygame

# Initialize pygame
pygame.init()

# create the screen
screen = pygame.display.set_mode((800, 600))

# Title and Icon
pygame.display.set_caption(" 🚀 Space Invaders 👾")
icon = pygame.image.load('spaceship.png')
pygame.display.set_icon(icon)

# Player
playerImg = pygame.image.load('space-invaders.png')
playerX = 370
playerY = 480


def player(): 
    screen.blit(playerImg, (playerX, playerY))

# Game Loop
running = True
while running:
    # screen as RGB
    screen.fill((128, 0, 128))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


player()
pygame.display.update()