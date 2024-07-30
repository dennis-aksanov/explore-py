import pygame
import sys

speedRate = 0.3

def main():
    keepGoing = True
    pygame.init()
    # screen = pygame.display.set_mode((800, 600))
    screen = pygame.display.set_mode([800, 600])
    # screen.fill(0)
    # pygame.display.set_caption("window")
    pic = pygame.image.load("ferderta2.png")
    colorkey = pic.get_at((0, 0))
    pic.set_colorkey(colorkey)
    picx = 0
    picy = 0

    while keepGoing:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                screen.fill((255, 0, 0))
                pygame.display.update()
                keepGoing = False
                # continue

        picx += 1 * speedRate
        picy += 1 * speedRate
        screen.blit(pic, (picx, picy))
        pygame.display.update()

    pygame.quit()


if __name__ == "__main__":
    main()
    sys.exit()
