import pygame
import sys
import random


def main():
    keepGoing = True
    pygame.init()
    screen = pygame.display.set_mode([800, 600])

    colors = [0] * 100
    locations = [0] * 100
    sizes = [0] * 100

    for n in range(100):
        colors[n] = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        locations[n] = (random.randint(0, 800), random.randint(0, 600))
        sizes[n] = (random.randint(10, 100))

    for n in range(100):
        pygame.draw.circle(screen, colors[n], locations[n], sizes[n])

    while keepGoing:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                screen.fill((255, 0, 0))
                pygame.display.update()
                keepGoing = False
                # continue

        pygame.display.update()

    pygame.quit()


if __name__ == "__main__":
    main()
    sys.exit()