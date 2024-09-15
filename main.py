#
#
#

import pygame
from pygame import Vector2
from constants import *
from player import *


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
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()

    # Create player object
    spawn_pos = Vector2(screen.get_width() / 2, screen.get_height() / 2)
    player = Player(spawn_pos.x, spawn_pos.y)
    updatable.add(player)
    drawable.add(player)

    # Game loop
    running = True
    while running:
        # pygame.QUIT event means the user clicked X to close your window
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Add update logic here
        # ...
        updatable.update(dt)

        # Fill the screen with a color to wipe away anything from last frame
        screen.fill("black")

        # Add render logic here
        # ...
        for sp in drawable.sprites():
            sp.draw(screen)

        pygame.display.flip()       # Refresh
        dt = clock.tick(60) / 1000  # Calculate delta-time

    pygame.quit()


if __name__ == "__main__":
    main()
