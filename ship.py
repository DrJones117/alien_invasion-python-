import pygame

class Ship:
    # The Ship class
    def __init__(self, ai_game):
        # Intialize the ship and set its starting position.
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()

        # Load the ship image and get its rect.
        self.image = pygame.image.load('images/rocket-2442125_640.bmp')
        self.rect = self.image.get_rect()

        # Start the ship at the bottom center of the screen.
        self.rect.midbottom = self.screen_rect.midbottom

        # Store a value that represents the ship's position
        self.x = float(self.rect.x)

        # Movement flag
        self.moving_right = False
        self.moving_left = False

    def update(self):
        # Update the ship's position based on the movement flag
        if self.moving_right:
            self.x += self.settings.ship_speed
        if self.moving_left:
            self.x -= self.settings.ship_speed

        # Update rect object from self.x
        self.rect.x = self.x


    def blitme(self):
        # Draw the ship at its surrent location.
        self.screen.blit(self.image, self.rect)