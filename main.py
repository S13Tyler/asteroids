#
#
#

import pygame
from pygame import Vector2
from pygame.font import Font
from constants import *
from gamestate import *
from player import *
from shot import Shot
from asteroid import Asteroid
from asteroidfield import AsteroidField


# Initialize pygame
pygame.init()
pygame.display.set_caption("Asteroids by S13Tyler")
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
background = pygame.image.load("images/backgrounds/Starfield_01.png").convert_alpha()

# Create game state object
gamestate = GameState()


def init_player():
    spawn_pos = Vector2(screen.get_width() / 2, screen.get_height() / 2)
    return Player(spawn_pos.x, spawn_pos.y)


def main():
    # Setup game ticks
    clock = pygame.time.Clock()
    dt = 0

    # Create groups
    grp_updatable = pygame.sprite.Group()
    grp_drawable = pygame.sprite.Group()
    grp_asteroids = pygame.sprite.Group()
    grp_shots = pygame.sprite.Group()

    # Add groups to object static containers
    Player.containers = (grp_updatable, grp_drawable)
    Shot.containers = (grp_updatable, grp_shots)
    Asteroid.containers = (grp_updatable, grp_drawable, grp_asteroids)
    AsteroidField.containers = (grp_updatable)

    # Create player object
    player = init_player()
    asteroid_field = AsteroidField()

    # Game loop
    running = True
    while running:
        # Check if we need to break out of the game loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Fill the screen with a color to wipe away anything from last frame
        screen.fill("black")
        for x in range(0, SCREEN_WIDTH, background.get_size()[0]):
            for y in range(0, SCREEN_HEIGHT, background.get_size()[1]):
                screen.blit(background, (x, y))

        # Group logic
        for obj in grp_updatable:
            obj.update(dt)
        for obj in grp_shots:
            obj.draw(screen)
        for obj in grp_drawable:
            obj.draw(screen)
        for obj in grp_asteroids:
            if obj.collision_check(player):
                gamestate.on_player_hit()
            for shot in grp_shots:
                if shot.collision_check(obj):
                    shot.kill()
                    obj.split()

        # Refresh and calculate delta-time
        pygame.display.flip()
        dt = clock.tick(60) / 1000
    pygame.quit()


if __name__ == "__main__":
    main()
