import pygame


class Ship:
    def __init__(self, ai_game):
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()
        self.settings = ai_game.settings

        self.image = pygame.image.load("alien_invasion/images/ship.bmp")
        self.rect = self.image.get_rect()

        # Start each new ship at the bottom center of the screen
        self.rect.midbottom = self.screen_rect.midbottom
        # Movement flag; start with a ship that's not moving
        self.prev_key = -1

    def blitme(self):
        self.screen.blit(self.image, self.rect)

    def update(self):
        if (
            self.prev_key == pygame.K_RIGHT
            or self.prev_key == pygame.K_LEFT
            or self.prev_key == pygame.K_UP
            or self.prev_key == pygame.K_DOWN
        ):
            self.move(self.prev_key)

    def move(self, key):
        self.prev_key = key
        move = self.settings.step * self.settings.speed
        if key == pygame.K_RIGHT:
            if (
                self.rect.x + self.settings.step + self.image.get_width()
                < self.settings.screen_width
            ):
                # Move the ship to the right
                self.rect.x += move
            else:
                self.rect.x = self.settings.screen_width - self.image.get_width()
        elif key == pygame.K_LEFT:
            if self.rect.x - self.settings.step - self.image.get_width() > 0:
                self.rect.x -= move
            else:
                self.rect.x = 0
        elif key == pygame.K_UP:
            if self.rect.y - self.settings.step > 0:
                # Move the ship up
                self.rect.y -= move
            else:
                self.rect.y = 0
        elif key == pygame.K_DOWN:
            if (
                self.rect.y + self.settings.step + self.image.get_height()
                < self.settings.screen_height
            ):
                # Move the ship down
                self.rect.y += move
            else:
                self.rect.y = self.settings.screen_height - self.image.get_height()
