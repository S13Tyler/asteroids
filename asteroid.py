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
