#
#
#

import pygame
from pygame import Vector2


# Base class for game objects
class CircleShape(pygame.sprite.Sprite):
    def __init__(self, x, y, radius):
        super().__init__(self.containers)
        self.position = Vector2(x, y)
        self.velocity = Vector2(0, 0)
        self.radius = radius

    def draw(self, screen):
        pass

    def update(self, dt):
        pass

    def collision_check(self, other):
        if isinstance(other, CircleShape):
            distance = Vector2.distance_to(self.position, other.position)
            if distance < (self.radius + other.radius):
                return True
        return False

    def normalize_rotation(self, rotation):
        # Normalize the rotation angle to stay between [0, 360]
        result = rotation % 360
        if result < 0:
            result += 360
        return int(result)
