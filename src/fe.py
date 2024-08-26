import pygame
import random
import time
import numpy as np
import matplotlib.pyplot as plt

# class GameSettings:
#     def __init__(self, size):
#         self.size = size
#         # self.field = np.array([], ndmin=2)
#         self.field = np.zeros((size.width, size.height))
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


def drawString(x, y, color, str):
    text = font.render(str, True, color)
    text_rect = text.get_rect()
    text_rect.x = x
    text_rect.y = y
    screen.blit(text, text_rect)



timer = pygame.time.Clock()
fed = 0
RED = (255, 0, 0)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)
gameFieldSize = Size(60, 30)
gameField = GameField(size=gameFieldSize)
cellSize = 99
screen = pygame.display.set_mode([gameField.size.width * cellSize,
                                  gameFieldSize.height * cellSize])
pygame.init()

font = pygame.font.SysFont('Times', 24)
mouseDown = False
keepGoing = True
x = 0
def drawX(x, y):
    pygame.draw.line(screen, RED, (x * cellSize + 5, y * cellSize + 5), ((x+1) * cellSize - 5, (y+1) * cellSize - 5), 2)
    pygame.draw.line(screen, RED, (x * cellSize + 5, (y+1) * cellSize - 5), ((x+1) * cellSize - 5, y * cellSize + 5), 2)


def drawO(x, y):
    pygame.draw.circle(screen, BLUE, (x * cellSize + cellSize / 2, y * cellSize + cellSize / 2), cellSize / 2 - 5, 2)

while keepGoing:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            keepGoing = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            coord = pygame.mouse.get_pos()
            mouseX = coord[0]
            mouseY = coord[1]
            mouseDown = True

        if mouseDown:
            if fed == 0:
                drawX(int(mouseX / cellSize), int(mouseY / cellSize))
                fed = 1
            else:
                drawO(int(mouseX / cellSize), int(mouseY / cellSize))
                fed = 0
            mouseDown = False
    pygame.display.update()
pygame.quit()
