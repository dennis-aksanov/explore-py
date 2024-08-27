import pygame
import numpy as np


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
        self.field = np.zeros((size.width, size.height))


def drawString(x, y, color, str):
    text = font.render(str, True, color)
    text_rect = text.get_rect()
    text_rect.x = x
    text_rect.y = y
    screen.blit(text, text_rect)



timer = pygame.time.Clock()
cellSize = 99
window_height = 680
window_width = 1360
fed = 0
RED = (255, 0, 0)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
gameFieldSize = Size(60, 30)
gameField = GameField(size=gameFieldSize)
screen = pygame.display.set_mode([gameField.size.width * cellSize,
                                  gameFieldSize.height * cellSize])
background = pygame.image.load("feto1.jpg")
background = pygame.transform.scale(background, (window_width, window_height))
screen.blit(background, (0, 0))
pygame.init()
font = pygame.font.SysFont('Times', 24)
mouseDown = False
keepGoing = True
pygame.draw.line(screen, WHITE, (cellSize*5, cellSize*2), (cellSize*5, cellSize*5), 5)
pygame.draw.line(screen, WHITE, (cellSize*8, cellSize*2), (cellSize*8, cellSize*5), 5)
pygame.draw.line(screen, WHITE, (cellSize*5, cellSize*2), (cellSize*8, cellSize*2), 5)
pygame.draw.line(screen, WHITE, (cellSize*5, cellSize*5), (cellSize*8, cellSize*5), 5)


def drawX(x, y):
    pygame.draw.line(screen, RED, (x * cellSize + 5, y * cellSize + 5), ((x+1) * cellSize - 5, (y+1) * cellSize - 5), 4)
    pygame.draw.line(screen, RED, (x * cellSize + 5, (y+1) * cellSize - 5), ((x+1) * cellSize - 5, y * cellSize + 5), 4)


def drawO(x, y):
    pygame.draw.circle(screen, BLUE, (x * cellSize + cellSize / 2, y * cellSize + cellSize / 2), cellSize / 2 - 5, 4)

while keepGoing:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            keepGoing = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            coord = pygame.mouse.get_pos()
            mouseX = coord[0]
            mouseY = coord[1]
            if (mouseX < cellSize * 5
                    or mouseX > cellSize * 8
                    or mouseY < cellSize * 2
                    or mouseY > cellSize * 5):
                mouseDown = False
            else:
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
