import pygame
import random
import time
import numpy as np
import sys


class GameSettings:
    def __init__(self, ticks, snakeHeadSize, scoreInc, appleSize):
        self.ticks = ticks
        self.snakeHeadSize = snakeHeadSize
        self.scoreInc = scoreInc
        self.appleSize = appleSize

gameSettings = [
    GameSettings(10, 10, 0.9, 1),
    GameSettings(18, 10, 0.9, 2),
    GameSettings(20, 15, 1.0, 3),
    GameSettings(20, 15, 1.1, 3),
    GameSettings(30, 20, 1.3, 3),
    GameSettings(30, 25, 1.6, 4),
    GameSettings(32, 25, 1.7, 4),
    GameSettings(20, 20, 2.3, 4),
    GameSettings(20, 20, 4, 4)
]


def drawString(x, y, color, str):
    text = font.render(str, True, color)
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



def startCountdown(delay):
    time.sleep(delay)
class Coord:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Size:
    def __init__(self, width, height):
        self.width = width
        self.height = height


class GameField:
    def __init__(self, size):
        self.size = size
        # self.field = np.array([], ndmin=2)
        self.field = np.zeros((size.width, size.height))


    def addApple(self, coord, size):
        if self.field[coord.x][coord.y] == 0:
            self.field[coord.x][coord.y] = size + 10
            return True
        return False



class Snake:
    def __init__(self, coord, appleSize):
        self.coord = coord
        self.body = [coord]
        self.direction = Coord(1, 0)
        self.appleSize = appleSize


    def setDirection(self, keyPressed):
        newDirection = self.direction
        if key_pressed[pygame.K_a] or key_pressed[pygame.K_LEFT]:
            newDirection = Coord(-1, 0)
        if key_pressed[pygame.K_d] or key_pressed[pygame.K_RIGHT]:
            newDirection = Coord(+1, 0)
        if key_pressed[pygame.K_w] or key_pressed[pygame.K_UP]:
            newDirection = Coord(0, -1)
        if key_pressed[pygame.K_s] or key_pressed[pygame.K_DOWN]:
            newDirection = Coord(0, +1)
        if newDirection.x != 0 and self.direction.x != 0 or newDirection.y != 0 and self.direction.y != 0:
            return
        else:
            self.direction = newDirection


    def step(self, gameField) -> Coord:
        nextCoord = Coord(int(self.body[0].x + self.direction.x),
                          int(self.body[0].y + self.direction.y))
        self.body.insert(0, nextCoord)
        global apples
        if gameField.field[nextCoord.x][nextCoord.y] == 1:
            print("=============")
            print("game over")
            print("=============")
            print("=============")
            print("snake length: {}".format(snakeLength))
            print("Scores: {}".format(int(scores)))
            print("Apples: {}".format(apples))
            print("=============")
            exit()
        if gameField.field[nextCoord.x][nextCoord.y] > 10:
            self.appleSize = self.appleSize + gameField.field[nextCoord.x][nextCoord.y] - 10
            apples = apples + 1
            isAppleAdded = False
            while isAppleAdded == False:
                newAppleCoord = Coord(random.randint(10, gameField.size.width - 10),
                                      random.randint(10, gameField.size.height - 10))
                isAppleAdded = gameField.addApple(newAppleCoord, gameSettings[level].appleSize)

            pygame.draw.circle(screen, RED,
                               (newAppleCoord.x * cellSize + cellSize / 2, newAppleCoord.y * cellSize + cellSize / 2),
                               cellSize / 2)

        gameField.field[nextCoord.x][nextCoord.y] = 1
        if self.appleSize > 0:
            self.appleSize = self.appleSize - 1
            return None
        else:
            tail = self.body[-1]
            gameField.field[int(self.body[-1].x)][int(self.body[-1].y)] = 0
            self.body.pop(-1)
            return tail



print("1000 - normal,\n10000 - really good,\n50000 - great,\n100000 - fantastic,\n1000000 - god\n")
print("=============\n")
difficultLevel = input("difficulty: easy - 1,\nnormal - 2,\nhard - 3,\ndemon - 4,\nextra-demon - 5,\nsuper extra-demon - 6,\nnightmare - 7,\nimpossible - 8,\ngod - 9\n")
level = int(difficultLevel) - 1
print("difficulte for game was set")
print("\n=============\n")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
timer = pygame.time.Clock()
RED = (255, 0, 0)
BLACK = (0, 0, 0)
cellSize = 20
gameFieldSize = Size(60, 30)
gameField = GameField(size=gameFieldSize)
newAppleCoord = Coord(random.randint(10, gameField.size.width - 10), random.randint(10, gameField.size.height - 10))
gameField.addApple(newAppleCoord, level + 2)
snake = Snake(Coord(gameField.size.width / 2, gameField.size.height / 2), 1)

# window_height = 680
# window_width = 1360
screen = pygame.display.set_mode([gameField.size.width * cellSize,
                                  gameFieldSize.height * cellSize])
pygame.init()

font = pygame.font.SysFont('Times', 24)
snakeColor = colors[random.randint(0, 5)]
# snakeColor = (255, 0, 0)
snakeCoord = Coord(10, 10)
snakeCoordChanege = Coord(1, 0)
snakeHeadSize = Size(cellSize, cellSize)
snakeLength = 0
scores = 0
apples = 0
strScores = ""
strSnakeLength = ""
strApplesEaten = ""
directionChanged = True
keepGoing = True

pygame.draw.circle(screen, RED, (newAppleCoord.x * cellSize + cellSize / 2, newAppleCoord.y * cellSize + cellSize / 2), cellSize / 2)
print("({},{}) = {}".format(newAppleCoord.x, newAppleCoord.y, gameField.field[newAppleCoord.x][newAppleCoord.y]))

while keepGoing:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            keepGoing = False
        if event.type == pygame.KEYDOWN:
            directionChanged = True
            key_pressed = pygame.key.get_pressed()
            snake.setDirection(key_pressed)
    if level != 8 and level != 7:
        snakeColor = colors[random.randint(0, 5)]
    else:
        if level == 7:
            snakeColor = BLACK
            if (directionChanged):
                snakeColor = RED
                directionChanged = False
            else:
                snakeColor = BLACK
        else:
           snakeColor = BLACK

    drawString(1, 60, BLACK, strApplesEaten)
    tail = snake.step(gameField)

    if (snake.body[0].x > gameField.size.width
            or snake.body[0].x < 0
            or snake.body[0].y > gameField.size.height
            or snake.body[0].y < 0):
        print("=============")
        print("game over")
        print("=============")
        print("=============")
        print("snake length: {}".format(snakeLength))
        print("Scores: {}".format(int(scores)))
        print("Apples: {}".format(apples))
        print("=============")
        exit()
    if tail != None:
        pygame.draw.rect(screen, BLACK, (tail.x * cellSize,
                                              tail.y * cellSize,
                                              cellSize,
                                              cellSize))
    pygame.draw.rect(screen, snakeColor, (snake.body[0].x * cellSize,
                                          snake.body[0].y * cellSize,
                                          cellSize,
                                          cellSize))

    drawString(1, 10, BLACK, strSnakeLength)
    drawString(1, 35, BLACK, strScores)
    scores = scores + gameSettings[level].scoreInc
    strScores = "Scores: {}".format(int(scores))
    strSnakeLength = "Snake length: {}".format(len(snake.body))
    strApplesEaten ="Apples: {}".format(apples)
    drawString(1, 10, RED, strSnakeLength)
    drawString(1, 35, RED, strScores)
    drawString(1, 60, RED, strApplesEaten)
    pygame.display.update()
    timer.tick(gameSettings[level].ticks)
pygame.quit()
