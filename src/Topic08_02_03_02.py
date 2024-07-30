import pygame

colors = [0] * 100
locations = [0] * 100
sizes = [0] * 100


import random
for n in range(100):
    colors[n] = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    locations[n] = (random.randint(0,800),random.randint(0,600))
    sizes[n] = (random.randint(10, 100))
for n in range(100):
    pygame.draw.circle(screen, colors[n], locations[n], sizes[n])
