import sys

import pygame

from settings import Settings
from ship import Ship

class AlienInvasion:
    # Parent class for game assets and behavior

    def __init__(self):
        # Create the game resources
        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Alien Invasion")

        self.ship = Ship(self)

        # Set the background color
        self.bg_color = (230, 230, 230)

    def run_game(self):
        # Start the main loop for the game.
        while True:
            self._check_events()
            self._update_screen()

            # Make the most recently drawn screen visible.
            pygame.display.flip()

    # Two helper functions
    def _check_events(self):
        # The loop watches for keyboard and mouse events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

    def _update_screen(self):
        # Redraw the screen during each pass through the loop
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()


if __name__ == '__main__':
    # Make an instance of the game then runs the it
    ai = AlienInvasion()
    ai.run_game()

