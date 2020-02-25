import pygame
import time

class JarvisMarch:
    def __init__(self, points, color, screen, convex_hull, yellow, Red, Grey):
        self.points = points
        self.screen = screen
        self.color = color
        self.convex_hull = convex_hull
        self.yellow = yellow
        self.Red = Red
        self.Grey = Grey
    def left_most(self):
        min = 0
        for i in range(1,len(self.points)):
            if self.points[i].x < self.points[min].x:
                min = i
            elif self.points[i].x == self.points[min].x:
                if self.points[i].y > self.points[min].y:
                    min = i

        pygame.draw.circle(self.screen, self.color, (self.points[min].x, self.points[min].y), 10)
        pygame.display.update()
        return min

    def direction(self, a, b, c):
        orientation = (b.y - a.y) * (c.x - b.x) - (b.x - a.x) * (c.y - b.y)

        if orientation == 0:
            return 0
        elif orientation > 0:
            return 1
        else:
            return 2

    def convex(self):
        if len(self.points) < 3:
            return
        current_point = self.left_most()
        hull = []
        a = current_point
        b = 0
        while(True):
            hull.append(a)
            b = (a + 1) % len(self.points)

            for i in range(len(self.points)):
                pygame.draw.line(self.screen, self.Grey, (self.points[a].x, self.points[a].y),(self.points[i].x, self.points[i].y), 1)
                time.sleep(0.1)
                pygame.display.update()
                if(self.direction(self.points[a], self.points[i], self.points[b]) == 2):
                    b = i
            a = b
            if a == current_point:

                break
        for n in hull:
            pygame.draw.circle(self.screen, self.Red, (self.points[n].x, self.points[n].y), 10)
            pygame.display.update()
            self.convex_hull.append((self.points[n].x, self.points[n].y))
            time.sleep(0.1)
