#
#
#

import pygame
from pygame import Vector2
from constants import *
from circleshape import CircleShape
from shot import Shot


# Player class
class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0
        self.shot_cooldown_timer = 0
        self.can_shoot = True

    # Returns a list of 2d points to render as a triangle
    def triangle(self):
        forward = Vector2(0, 1).rotate(self.rotation)
        right = (Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5)
        a = (self.position + forward * self.radius)
        b = (self.position - forward * self.radius - right)
        c = (self.position - forward * self.radius + right)
        return [a, b, c]

    def draw(self, screen):
        pygame.draw.polygon(screen, "white", self.triangle(), 2)

    def update(self, dt):
        if not self.can_shoot:
            if self.shot_cooldown_timer > 0.0:
                self.shot_cooldown_timer -= dt
            else:
                self.shot_cooldown_timer = 0.0
                self.can_shoot = True

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

        # Handle shoot inputs
        if keys[pygame.K_SPACE]:
            self.shoot()

    def move(self, dt):
        forward_vect = Vector2(0, 1).rotate(self.rotation)
        self.position += (forward_vect * PLAYER_VELOCITY * dt)

    def rotate(self, dt):
        rotation_amount = (PLAYER_ROTATION_SPEED * dt)
        self.rotation = self.normalize_rotation(self.rotation + rotation_amount)

    def shoot(self):
        if self.can_shoot:
            self.start_shot_timer()
            shot = Shot(self.position.x, self.position.y, SHOT_RADIUS, self.rotation)
            shot.velocity = (Vector2(0, 1).rotate(self.rotation) * PLAYER_SHOOT_SPEED)

    def start_shot_timer(self):
        self.can_shoot = False
        self.shot_cooldown_timer = PLAYER_SHOOT_COOLDOWN
