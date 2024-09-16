#
#
#

import pygame
from pygame import Vector2
from constants import *
from circleshape import CircleShape


# Shot projectile class
class Shot(CircleShape):
    def __init__(self, x, y, radius, angle):
        super().__init__(x, y, radius)
        self.angle = angle
        self.initial_pos = Vector2(x, y)
        self.velocity = self.initial_pos

    def draw(self, screen):
        if Vector2.distance_to(self.initial_pos, self.position) > (PLAYER_RADIUS / 2 + 10):
            pygame.draw.circle(screen, "blue", self.position, self.radius, 2)
        else:
            pygame.draw.circle(screen, "black", self.position, self.radius, 2)

    def update(self, dt):
        self.position += (self.velocity * dt)
