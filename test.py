import pygame
import os

# Setup Screen
pygame.init()

WIDTH, HEIGHT = 800, 500

win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Hangman Game!")
#

# Load Images
images = []
for i in range(7):
    filename = "images/hangman" + str(i) + ".png"
    image = pygame.image.load(filename)
    images.append(image)
#
print(images)
# colors
WHITE = (255, 255, 255)
# game variables
hangman_status = 0
# Game Loop
FPS = 60
clock = pygame.time.Clock()
run = True
while run:
    clock.tick(FPS)

    win.fill(WHITE)
    win.blit(images[hangman_status], (150, 100))
    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            print(pos)


pygame.quit()
print("Game Closed")
