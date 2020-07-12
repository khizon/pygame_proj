import pygame
import math

# Setup Screen
pygame.init()

WIDTH, HEIGHT = 800, 500

win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Hangman Game!")
#


# Button variables
RADIUS = 20
GAP = 15
letters = []
startx = round((WIDTH - (RADIUS * 2 + GAP) * 13) / 2)
starty = 400
A = 65

for i in range(26):
    x = startx + GAP * 2 + ((2 * RADIUS + GAP) * (i % 13))
    y = starty + ((i // 13) * (GAP + RADIUS * 2))

    letters.append([x, y, chr(A + i), True])


# Load Images
images = []
for i in range(7):
    filename = "images/hangman" + str(i) + ".png"
    image = pygame.image.load(filename)
    images.append(image)

print(images)

# fonts
LETTER_FONT = pygame.font.SysFont("comicsans", 40)

# colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# game variables
hangman_status = 0

# Game Loop
FPS = 60
clock = pygame.time.Clock()
run = True


def draw():
    win.fill(WHITE)
    # draw buttons
    for letter in letters:
        x, y, ltr, visible = letter
        if visible:
            pygame.draw.circle(win, BLACK, (x, y), RADIUS, 3)
            text = LETTER_FONT.render(ltr, 1, BLACK)
            win.blit(text, (x - RADIUS / 2, y - RADIUS / 2))
    win.blit(images[hangman_status], (150, 100))
    pygame.display.update()


while run:
    clock.tick(FPS)
    draw()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            mx, my = pygame.mouse.get_pos()
            for letter in letters:
                x, y, ltr, visible = letter
                if visible:
                    dis = math.sqrt((x - mx) ** 2 + (y - my) ** 2)
                    if dis < RADIUS:
                        print(ltr)
                        letter[3] = False


pygame.quit()
print("Game Closed")
