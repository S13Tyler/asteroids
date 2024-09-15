#
#
#

import pygame
from pygame import Vector2
from circleshape import CircleShape
from constants import *


class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0

    # Returns a list of 2d points to render as a triangle
    def triangle(self):
        forward = Vector2(0, 1).rotate(self.rotation)
        right = Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]

    def draw(self, screen):
        pygame.draw.polygon(screen, "white", self.triangle(), 2)

    def update(self, dt):
        keys = pygame.key.get_pressed()

        # Handle movement inputs
        if keys[pygame.K_UP]:
            self.move(dt)
        elif keys[pygame.K_DOWN]:
            self.move(-dt)

        # Handle rotation inputs
        if keys[pygame.K_LEFT]:
            self.rotate(-dt)
        elif keys[pygame.K_RIGHT]:
            self.rotate(dt)

    def move(self, dt):
        forward_vect = Vector2(0, 1).rotate(self.rotation)
        self.position += forward_vect * PLAYER_VELOCITY * dt

    def rotate(self, dt):
        rotation_amount = PLAYER_ROTATION_SPEED * dt
        # Normalize the rotation angle to stay between [0, 360]
        self.rotation = (self.rotation + rotation_amount) % 360
        if self.rotation < 0:
            self.rotation += 360
