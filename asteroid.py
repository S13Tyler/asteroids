#
#
#

import pygame
import random
from constants import *
from circleshape import *


# Asteroid class
class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.velocity = Vector2(x, y)

    def draw(self, screen):
        pygame.draw.circle(screen, "red", self.position, self.radius, 2)

    def update(self, dt):
        self.position += (self.velocity * dt)

    def split(self):
        if self.radius > ASTEROID_MIN_RADIUS:
            pos = self.position
            radius = (self.radius - ASTEROID_MIN_RADIUS)
            asteroid_1 = Asteroid(pos.x, pos.y, radius)
            asteroid_1.velocity = self.velocity.rotate(random.uniform(20, 50)) * ASTEROID_SPLIT_SPEED_MODIFIER
            asteroid_2 = Asteroid(pos.x, pos.y, radius)
            asteroid_2.velocity = self.velocity.rotate(-random.uniform(20, 50)) * ASTEROID_SPLIT_SPEED_MODIFIER
        self.kill()
