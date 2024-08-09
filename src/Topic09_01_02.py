import pygame
import random
window_height = 680
window_width = 1360
pygame.init()
screen = pygame.display.set_mode([window_width, window_height])
pygame.display.set_caption("Smiley Explosion")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
mouseDown = False
keepGoing = True
# YELLOW = (255, 255, 0)
# radius = 15
BLACK = (0, 0, 0)
lastCoord = (-1, -1)

while keepGoing:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            keepGoing = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouseDown = True
        if event.type == pygame.MOUSEBUTTONUP:
            mouseDown = False
            lastCoord = (-1, -1)
        if event.type == pygame.KEYDOWN:
            if pygame.key.get_pressed()[pygame.K_SPACE]:
                screen.fill(BLACK)
            if pygame.key.get_pressed()[pygame.K_ESCAPE]:
                exit()
        if mouseDown:
            spot = pygame.mouse.get_pos()
            if lastCoord == (-1, -1):
                lastCoord = spot
            coolor = random.choice(colors)
            pygame.draw.line(screen, coolor, lastCoord, spot, 10)
            lastCoord = spot
        pygame.display.update()
