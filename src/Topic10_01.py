import pygame
import sys
import random
window_height = 680
window_width = 1360
pygame.init()
screen = pygame.display.set_mode([window_width, window_height])
pygame.display.set_caption("Smiley Explosion")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
pic = pygame.image.load("ferderta2.png")
# pic = colors
colorkey = pic.get_at((0, 0))
pic.set_colorkey(colorkey)
# backround1 = ["black", "gray", "dark gray"]
timer = pygame.time.Clock()
keepGoing = True
BLACK = (0, 0, 0)
picx = 0
picy = 0
WHITE = (255, 255, 255)
speedx = 5
speedy = 5
paddlew = 200
paddleh = 25
paddlex = 300
paddley = 500
picw = pic.get_width()-20
pich = pic.get_height()-20
points = 0
lives = 5
font = pygame.font.SysFont('Times', 24)

while keepGoing:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            keepGoing = False

    picx += speedx
    picy += speedy
    if picx <= 0 or picx + pic.get_width() >= window_width:
        speedx = -speedx
    if picy <= 0:
        speedy = -speedy
    if picy >= 500:
        lives -= 1
        speedy = -speedy
    if lives <= 0:
        exit()
    # coolor1 = random.choice(backround1)
    screen.fill(BLACK)
    screen.blit(pic, (picx, picy))
    paddlex = pygame.mouse.get_pos() [0]
    paddlex -= paddlew
    pygame.draw.rect(screen, WHITE, (paddlex, paddley, paddlew, paddleh))
    if picy + pich >= paddley and picy + pich <=paddley + paddleh and speedy > 0:
        if picx + picw / 2 >= paddlex and picx + picw / 2 <= paddlex + paddlew and speedy > 0:
            points += 1
            # circleColor = random.choice(colors)
            # pic = circleColor
            speedy = -speedy
    draw_string = "live: " + str(lives) + "point" + str(points)
    text = font.render(draw_string, True, WHITE)
    text_rect = text.get_rect()
    text_rect.centerx = screen.get_rect().centerx
    text_rect.y = 10
    screen.blit(text, text_rect)
    pygame.display.update()
    timer.tick(60)

pygame.quit()