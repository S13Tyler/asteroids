#
#
#

import pygame
import random
from pygame import Vector2
from circleshape import *
from constants import *



class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.__velocity = int(random.uniform(ASTEROID_MIN_VELOCITY, ASTEROID_MAX_VELOCITY))
        self.__direction = self.calculate_direction()

    def draw(self, screen):
        pygame.draw.circle(screen, "red", self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.__direction * self.__velocity * dt

    def calculate_direction(self):
        pos = self.position
        origin = Vector2(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
        rotation_limits : Vector2

        # Find quadrant from position normalized to center of screen
        # Set rotation limits so the asteroid travels in a conventional direction based on where it spawned
        if pos.x > origin.x and pos.y > origin.y:   # quadrant 1
            rotation_limits = Vector2(0, 90)
        elif pos.x < origin.x and pos.y > origin.y: # quadrant 2
            rotation_limits = Vector2(270, 360)
        elif pos.x < origin.x and pos.y < origin.y: # quadrant 3
            rotation_limits = Vector2(180, 270)
        elif pos.x > origin.x and pos.y < origin.y: # quadrant 4
            rotation_limits = Vector2(90, 180)

        # Create a offset to add some extra randomness to the rotation limits
        rot_offset = random.uniform(-ASTEROID_ROTATION_MAX_OFFSET, ASTEROID_ROTATION_MAX_OFFSET)

        # Determine randomized rotation and add the offset amount
        rotation = random.uniform(rotation_limits.x, rotation_limits.y) + rot_offset

        # Set the direction vector based on the normalized rotation value
        return Vector2(0, 1).rotate(self.normalize_rotation(rotation))
