# Author : Joseph Bakulikira
# youtube channel : https://www.youtube.com/channel/UCjPk9YDheKst1FlAf_KSpyA
# please subscribe to my channel
# thanks

import pygame
import random
import time
import os

from points import Points
from JarvisMarch import JarvisMarch

WIDTH, HEIGHT = 1920, 1080
SCREEN = (WIDTH, HEIGHT)
# for full screen enable the line bellow
os.environ['SDL_VIDEO_CENTERED'] = '1'
# configurations
fps = 30
pygame.init()
clock =pygame.time.Clock()
pygame.display.set_caption("Convex Hull ( Gift Wrapper)")
win = pygame.display.set_mode(SCREEN)

#colors
White = (255, 255, 255)
Black = (30, 30, 30)
Grey = (180, 180, 180)
Blue = (0, 183, 255)
Yellow = (255, 230, 0, 128)
Red = (255, 15, 79)
Green = (41, 255, 123)

#background color
win.fill(Black)

# variables
point_number = 20
offset = 50
points = []
convex_hull = []
# Generate Points Points(number of points , offset number of the screen, ......)
for n in range(point_number):
    point = Points(random.randint(offset , WIDTH - offset), random.randint(offset , HEIGHT - offset))
    pygame.draw.circle(win, White, (point.x, point.y), 4)
    points.append(point)
pygame.display.update()

# jarvis March algorithm
jarvis = JarvisMarch(points, Green, win, convex_hull, Yellow, Red, Grey)
jarvis.left_most()
jarvis.convex()

# draw border lines
index = 0
for t in range(len(convex_hull)):
    if index != len(convex_hull)-1:
        time.sleep(0.5)
        pygame.draw.line(win, Blue, convex_hull[index], convex_hull[index + 1], 4)
        index = index + 1
        pygame.display.update()
    else:
        time.sleep(0.5)
        pygame.draw.line(win, Blue, convex_hull[len(convex_hull)-1], convex_hull[0], 4)
        pygame.display.update()


run = True
while run:
    clock.tick(fps)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        pygame.display.update()

pygame.quit()
