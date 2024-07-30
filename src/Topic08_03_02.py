import pygame
import sys

window_height = 710
window_width = 1366
def main():
    pygame.init()
    screen = pygame.display.set_mode([window_width, window_height])
    keepGoing = True
    pic = pygame.image.load("ferderta2.png")
    colorkey = pic.get_at((0, 0))
    pic.set_colorkey(colorkey)
    picx = 0
    picy = 0
    BLACK = (0, 0, 0)
    timer = pygame.time.Clock()
    speedx = 5
    speedy = 2.5

    # screen.fill(BLACK)
    while keepGoing:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                screen.fill((255, 0, 0))
                # pygame.display.update()
                keepGoing = False
                continue

        picx += speedx
        picy += speedy
        if picx <= 0 or picx + pic.get_width() >= window_width:
            speedx = -speedx
        if picy <= 0 or picy + pic.get_height() >= window_height:
            speedy = -speedy
        # screen.blit(pic, (picx, picy))
        # screen.fill(BLACK)
        screen.blit(pic, (picx, picy))
        pygame.display.update()
        timer.tick(90)


    pygame.quit()


if __name__ == "__main__":
    main()
    sys.exit()