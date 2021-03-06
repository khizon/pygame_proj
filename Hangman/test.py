import pygame
import math
import random

# Setup Screen
TITLE = "PYGAME HANGMAN"
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


# Load Images
images = []
for i in range(7):
    filename = (
        "C:/Users/kielh/Documents/Python_Projects/pygame_proj/Hangman/images/hangman"
        + str(i)
        + ".png"
    )
    image = pygame.image.load(filename)
    images.append(image)

# fonts
LETTER_FONT = pygame.font.SysFont("comicsans", 40)
WORD_FONT = pygame.font.SysFont("comicsans", 60)
TITLE_FONT = pygame.font.SysFont("comicsans", 70)

# colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)


def draw(hangman_status):
    win.fill(WHITE)
    # draw title
    text = TITLE_FONT.render(TITLE, 1, BLACK)
    win.blit(text, (WIDTH / 2 - text.get_width() / 2, 30))
    # draw word
    display_word = ""
    for letter in word:
        if letter in guessed:
            display_word += letter + " "
        else:
            display_word += "_ "
    text = WORD_FONT.render(display_word, 1, BLACK)
    win.blit(text, (400, 200))
    # draw buttons
    for letter in letters:
        x, y, ltr, visible = letter
        if visible:
            pygame.draw.circle(win, BLACK, (x, y), RADIUS, 3)
            text = LETTER_FONT.render(ltr, 1, BLACK)
            win.blit(text, (x - RADIUS / 2, y - RADIUS / 2))
    # draw hangman
    win.blit(images[hangman_status], (150, 100))
    pygame.display.update()


def display_message(message):
    pygame.time.delay(1000)
    win.fill(WHITE)
    text = WORD_FONT.render(message, 1, BLACK)
    win.blit(
        text, (WIDTH / 2 - text.get_width() / 2, HEIGHT / 2 - text.get_height() / 2)
    )
    pygame.display.update()
    pygame.time.delay(3000)


def main(hangman_status, word, guessed):

    # Game Loop
    FPS = 60
    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            if event.type == pygame.MOUSEBUTTONDOWN:
                mx, my = pygame.mouse.get_pos()
                pygame.event.clear()
                pygame.time.delay(500)

                for letter in letters:
                    x, y, ltr, visible = letter
                    if visible:
                        dis = math.sqrt((x - mx) ** 2 + (y - my) ** 2)
                        if dis < RADIUS:
                            print(ltr)
                            letter[3] = False
                            guessed.append(ltr)
                            if ltr not in word:
                                hangman_status += 1
                break
        draw(hangman_status)
        won = True
        for letter in word:
            if letter not in guessed:
                won = False
                break

        if won:
            print("won")
            display_message("You Won!")
            pygame.event.clear()
            break

        if hangman_status == 6:
            print("lost")
            display_message("You Lost!")
            pygame.event.clear()
            break

    return True


def choice_screen():
    run = True
    while run:
        win.fill(WHITE)
        text = WORD_FONT.render("CLICK TO PLAY AGAIN", 1, BLACK)
        win.blit(
            text, (WIDTH / 2 - text.get_width() / 2, HEIGHT / 2 - text.get_height() / 2)
        )
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            if event.type == pygame.MOUSEBUTTONDOWN:
                mx, my = pygame.mouse.get_pos()
                pygame.time.delay(500)
                if mx > WIDTH / 2:
                    return True
                else:
                    return False


while True:
    # game variables
    hangman_status = 0
    words = ["DEVELOPER", "SNAKE", "SHIP", "BROWN", "LITTLE"]
    word = random.choice(words)
    guessed = []
    # INITIALIZE LETTERS
    for i in range(26):
        x = startx + GAP * 2 + ((2 * RADIUS + GAP) * (i % 13))
        y = starty + ((i // 13) * (GAP + RADIUS * 2))

        letters.append([x, y, chr(A + i), True])

    if not main(hangman_status, word, guessed):
        break
    if not choice_screen():
        break
pygame.quit()
print("Game Closed")
