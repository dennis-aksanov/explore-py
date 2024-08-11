import pygame
import sys
import random


class Limits:
    def __init__(self, min, max):
        self.min = min
        self.max = max


class GameSettings:
    def __init__(self, speedXLimit, speedYLimit, lives, pointsInc):
        self.speedXLimit = speedXLimit
        self.speedYLimit = speedYLimit
        self.lives = lives
        self.pointsInc = pointsInc


def genXSpeed(level, limit):
    speedX = 0
    while speedX > limit.min * ((level+1)/20) and speedX < limit.max * ((level+1)/20):
        speedX = random.randint(limit.min, limit.max)
    return speedX


gameSettings = [
    GameSettings(Limits(-6, 6), Limits(2, 5), 5, 1),
    GameSettings(Limits(-7, 7), Limits(3, 6), 4, 2),
    GameSettings(Limits(-9, 9), Limits(5, 8), 3, 3),
    GameSettings(Limits(-15, 15), Limits(9, 12), 2, 4),
    GameSettings(Limits(-17, 17), Limits(13, 15), 1, 5),
    GameSettings(Limits(-25, 25), Limits(14, 18), 1, 7)
]

difficultLevel = input("difficulty: easy-1, normal-2, hard-3, demon-4, nightmare-5, impossible-6:\n")
level = int(difficultLevel) - 1
pygame.init()
window_height = 680
window_width = 1360
screen = pygame.display.set_mode([window_width, window_height])
background = pygame.image.load("feto1.jpg")
background = pygame.transform.scale(background, (window_width, window_height))
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
paddleColor = random.randint(0, 5)
pygame.display.set_caption("Smiley Explosion")
bubbles = [pygame.image.load("bubble.png"),
           pygame.image.load("bubble1.png"),
           pygame.image.load("bubble2.png"),
           pygame.image.load("bubble3.png"),
           pygame.image.load("bubble4.png")]
idxBubble = random.randint(0, 4)
bubble = bubbles[idxBubble]
colorkey = bubble.get_at((0, 0))
bubble.set_colorkey(colorkey)
timer = pygame.time.Clock()
keepGoing = True
BLACK = (0, 0, 0)
picx = window_width / 2
picy = 0
WHITE = (255, 255, 255)
PURPLE = (219, 15, 158)
paddlew = 280
paddleh = 25
paddlex = 300
paddley = window_height - 90
picw = bubble.get_width()-20
pich = bubble.get_height()-20
points = 0
lives = gameSettings[level].lives
font = pygame.font.SysFont('Times', 24)


# speedx = random.randint(gameSettings[level].speedXLimit.min, gameSettings[level].speedXLimit.max)
speedx = genXSpeed(level, gameSettings[level].speedXLimit)
speedy = random.randint(gameSettings[level].speedYLimit.min, gameSettings[level].speedYLimit.max)
def drawString(x, y, str):
    text = font.render(str, True, PURPLE)
    text_rect = text.get_rect()
    text_rect.x = x
    text_rect.y = y
    screen.blit(text, text_rect)


while keepGoing:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            keepGoing = False

    picx += speedx
    picy += speedy

    if picx <= 0 or picx + bubble.get_width() >= window_width:
        speedx = -speedx

    if picy <= 0:
        speedy = -speedy

    if lives <= 0:
        print("points {}".format(points))
        exit()

    screen.blit(background, (0, 0))
    screen.blit(bubble, (picx, picy))
    paddlex = pygame.mouse.get_pos() [0]
    paddlex -= paddlew
    pygame.draw.rect(screen, colors[paddleColor], (paddlex, paddley, paddlew, paddleh))

    if picy + pich >= paddley and picy + pich <= paddley + paddleh and speedy > 0:

        speedy = 0
        speedx = 0
        while speedx == 0 and speedy == 0:
            # speedx = random.randint(gameSettings[level].speedXLimit.min, gameSettings[level].speedXLimit.max)
            speedx = genXSpeed(level, gameSettings[level].speedXLimit)
            speedy = random.randint(gameSettings[level].speedYLimit.min, gameSettings[level].speedYLimit.max)
        newIdxBubble = idxBubble
        while newIdxBubble == idxBubble:
            newIdxBubble = random.randint(0, 3)
        idxBubble = newIdxBubble
        bubble = bubbles[idxBubble]
        bubble.set_colorkey(colorkey)
        picw = bubble.get_width() - 20
        pich = bubble.get_height() - 20

        if picx + picw / 2 >= paddlex and picx + picw / 2 <= paddlex + paddlew and speedy > 0:
            points += gameSettings[level].pointsInc
            paddleColor = random.randint(0, 5)
            speedy = -speedy
        else:
            picy = 0
            picx = window_width / 2
            lives -= 1

    strLives = "Lives: {}".format(lives)
    strPoints = "Points: {}".format(points)
    x = window_width/2 - 50;
    drawString(x, 10, strLives)
    drawString(x, 30, strPoints)
    pygame.display.update()
    timer.tick(60)

pygame.quit()
