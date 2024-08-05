import pygame
import random

window_height = 710
window_width = 1366
pygame.init()
screen = pygame.display.set_mode([window_width, window_height])
background = pygame.image.load("foto.jpeg")
background = pygame.transform.scale(background, (window_width, window_height))
pygame.display.set_caption("Smiley Explosion")
sprite_list = pygame.sprite.Group()
clock = pygame.time.Clock()

class Smiley(pygame.sprite.Sprite):
    pos = (0, 0)
    xvel = 1
    yvel = 1
    scale = 100

    def __init__(self, pos, xvel, yvel):
        pygame.sprite.Sprite.__init__(self)
        bubbles = [pygame.image.load("bubble.png"),
                   pygame.image.load("bubble1.png"),
                   pygame.image.load("bubble2.png"),
                   pygame.image.load("bubble3.png"),
                   pygame.image.load("bubble4.png")]
        idxBubble = random.randint(0, 3)
        bubble = bubbles[idxBubble]
        colorkey = bubble.get_at((0, 0))
        bubble.set_colorkey(colorkey)
        self.image = bubble
        self.scale = random.randrange(10, 100)
        self.image = pygame.transform.scale(self.image, (self.scale, self.scale))
        self.rect = self.image.get_rect()
        self.pos = pos
        self.rect.x = pos[0] - self.scale / 2
        self.rect.y = pos[1] - self.scale / 2
        self.xvel = xvel
        self.yvel = yvel

    def update(self):
        self.rect.x += self.xvel
        self.rect.y += self.yvel
        if self.rect.x <= 0 or self.rect.x > screen.get_width() - self.scale:
            self.xvel = -self.xvel
        if self.rect.y <= 0 or self.rect.y > screen.get_width() - self.scale:
            self.yvel = -self.yvel


def main():
    mouseDown = False
    keepGoing = True
    while keepGoing:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                keepGoing = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouseDown = True
            if event.type == pygame.MOUSEBUTTONUP:
                mouseDown = False
        screen.blit(background, (0, 0))
        sprite_list.update()
        sprite_list.draw(screen)
        clock.tick(60)
        pygame.display.update()
        if mouseDown:
            speedx = 1
            speedy = 1
            while speedx != 0 or speedy != 0:
                speedx = random.randint(-0, 0)
                speedy = random.randint(-0, 0)
            newSmiley = Smiley(pygame.mouse.get_pos(), speedx, speedy)
            sprite_list.add(newSmiley)
    pygame.quit()


if __name__ == "__main__":
    main()
