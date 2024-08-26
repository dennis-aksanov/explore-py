import pygame
import time
import random
import numpy


lines = 0
while lines < 1 or lines > 30:
    lines = input("Count of levels 1 - 30: \n")
    lines = int(lines)
pygame.init()
window_height = 680
window_width = 1360
y = 10
x = window_width / 2
RED = (255, 0, 0)
screen = pygame.display.set_mode([window_width, window_height])
lines1 = lines
level = 0
font = pygame.font.SysFont('Times', 15)


def drawString(x, y, str):
    text = font.render(str, True, RED)
    text_rect = text.get_rect()
    text_rect.x = x
    text_rect.y = y
    screen.blit(text, text_rect)


# lineN0 = numpy.array([1])
# lineN1 = numpy.array([1, 1])
lineN0 = numpy.ones((1,), dtype=int)
lineN1 = numpy.ones((2,), dtype=int)
while level <= lines:
    y = level * 24 + 10
    countElem = 0
    while countElem < level:
        x = countElem * 24 + window_width / 2 - level * 12
        # numbers = random.randint(1, 40)
        # strNumbers = "{}".format(numbers)
        # drawString(x, y, strNumbers)
        if countElem > 1:
            if countElem == 0:
                lineN1[countElem] = 1
                lineN1[level - 1] = 1
            else:
                if countElem <= level / 2:
                    lineN1[countElem] = lineN0[countElem-1] + lineN0[countElem]
                    lineN1[level - countElem] = lineN1[countElem]

        drawString(x, y, "{}".format(lineN1[countElem]))

        countElem = countElem + 1

    # lineN0 = lineN1
    level = level + 1
    if level > 1:
        lineN0 = lineN1
        lineN1 = numpy.ones((level,), dtype=int)
    pygame.display.update()
time.sleep(5)
pygame.quit()
