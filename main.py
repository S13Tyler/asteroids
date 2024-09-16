#
#
#

import pygame
import random
from pygame import Vector2
from constants import *
from player import *
from asteroid import *



def init_player(screen, groups):
    initial_pos = Vector2(screen.get_width() / 2, screen.get_height() / 2)
    player = Player(initial_pos.x, initial_pos.y)
    for group in groups:
        group.add(player)
    return player

def init_asteroids(count, screen, groups):
    asteroids = list()
    for i in range(count):
        pos = Vector2(int(random.uniform(0, SCREEN_WIDTH)), int(random.uniform(0, SCREEN_HEIGHT)))
        radius = int(random.uniform(ASTEROID_MIN_RADIUS, ASTEROID_MAX_RADIUS))
        asteroid = Asteroid(pos.x, pos.y, radius)
        asteroids.append(asteroid)
    for group in groups:
        for a in asteroids:
            group.add(a)
    return asteroids

def main():
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    # Setup pygame display
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0 # delta-time

    # Create groups
    grp_updatable = pygame.sprite.Group()
    grp_drawable = pygame.sprite.Group()
    grp_asteroids = pygame.sprite.Group()

    # Create player object
    player = init_player(screen, [grp_updatable, grp_drawable])

    # Create asteroid objects
    asteroids = init_asteroids(5, screen, [grp_updatable, grp_drawable, grp_asteroids])

    # Game loop
    running = True
    while running:
        # pygame.QUIT event means the user clicked X to close your window
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Add update logic here
        # ...
        grp_updatable.update(dt)

        # Fill the screen with a color to wipe away anything from last frame
        screen.fill("black")

        # Add render logic here
        # ...
        for sp in grp_drawable.sprites():
            sp.draw(screen)

        # Refresh and calculate delta-time
        pygame.display.flip()
        dt = clock.tick(60) / 1000

    pygame.quit()


if __name__ == "__main__":
    main()
