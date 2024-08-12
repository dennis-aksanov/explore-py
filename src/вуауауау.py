import pygame
import random
import time
import sys


class GameSettings:
    def __init__(self, ticks, snakeHeadSize):
        self.ticks = ticks
        self.snakeHeadSize = snakeHeadSize

gameSettings = [
    GameSettings(19, 15),
    GameSettings(27, 20),
    GameSettings(35, 20),
    GameSettings(45, 20),
    GameSettings(60, 30),
    GameSettings(65, 35),
    GameSettings(70, 30),
    GameSettings(85, 35)
]


def drawString(x, y, str):
    text = font.render(str, True, RED)
    text_rect = text.get_rect()
    text_rect.x = x
    text_rect.y = y
    screen.blit(text, text_rect)


def getColorByKey(keys):
    colors = {
        pygame.K_1: "red",
        pygame.K_2: "orange",
        pygame.K_3: "yellow",
        pygame.K_4: "green",
        pygame.K_5: "blue",
        pygame.K_6: "purple"
    }

    for key in colors.keys():
        if keys[key]:
            return colors[key]
    return ""
class Coord:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Size:
    def __init__(self, width, height):
        self.width = width
        self.height = height
difficultLevel = input("difficulty: easy - 1,\nnormal - 2,\nhard - 3,\ndemon - 4,\nextra-demon - 5,\nsuper extra-demon - 6,\nnightmare - 7,\nimpossible - 8\n")
level = int(difficultLevel) - 1
print("difficulte for game was set")
# snakeHeadSize = input("выберите размер змейки от 0 до 40: \n")
# snakeHeadSize = int(snakeHeadSize)
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
timer = pygame.time.Clock()
cellSize = gameSettings[level].snakeHeadSize
window_height = 680
window_width = 1360
screen = pygame.display.set_mode([window_width, window_height])
pygame.init()
font = pygame.font.SysFont('Times', 24)
RED = (255, 0, 0)
BLACK = (0, 0, 0)
snakeColor = colors[random.randint(0, 5)]
# snakeColor = (255, 0, 0)
snakeCoord = Coord(10, 10)
snakeCoordChanege = Coord(1, 0)
snakeHeadSize = Size(cellSize, cellSize)
snakeLength = 0
keepGoing = True
while keepGoing:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            keepGoing = False

        if event.type == pygame.KEYDOWN:
            key_pressed = pygame.key.get_pressed()
            # newSnakeColor = getColorByKey(key_pressed)
            # if newSnakeColor != "":
            #     snakeColor = newSnakeColor
            if key_pressed[pygame.K_a] or key_pressed[pygame.K_LEFT]:
                snakeCoordChanege = Coord(-1, 0)
            if key_pressed[pygame.K_d] or key_pressed[pygame.K_RIGHT]:
                snakeCoordChanege = Coord(+1, 0)
            if key_pressed[pygame.K_w] or key_pressed[pygame.K_UP]:
                snakeCoordChanege = Coord(0, -1)
            if key_pressed[pygame.K_s] or key_pressed[pygame.K_DOWN]:
                snakeCoordChanege = Coord(0, +1)
    snakeColor = colors[random.randint(0, 5)]
    snakeCoord.x = snakeCoord.x + snakeCoordChanege.x
    snakeCoord.y = snakeCoord.y + snakeCoordChanege.y
    if (snakeCoord.x * cellSize >= window_width
            or snakeCoord.x * cellSize < 0
            or snakeCoord.y * cellSize >= window_height
            or snakeCoord.y * cellSize < 0):
        print("snake length: {}".format(snakeLength))
        exit()
    pygame.draw.rect(screen, snakeColor, (snakeCoord.x * cellSize,
                                          snakeCoord.y * cellSize,
                                          snakeHeadSize.width,
                                          snakeHeadSize.height))
    pygame.display.update()
    screen.fill(BLACK)
    snakeLength = snakeLength + 1
    strSnakeLength = "snake length: {}".format(snakeLength)
    drawString(1, 10, strSnakeLength)
    timer.tick(gameSettings[level].ticks)
pygame.quit()
