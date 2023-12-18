import pygame
# START ChatGPT Code
class Player:
    def __init__(self, screen_width, screen_height):
        self.width = 20
        self.height = 80
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.x = (screen_width - self.width) // 2
        self.y = screen_height - self.height - 10
        self.speed = 5
        self.speed_lateral = 3

    def update(self, keys):
        if keys[pygame.K_LEFT] and self.x > 0:
            self.x -= self.speed_lateral
        if keys[pygame.K_RIGHT] and self.x < self.screen_width - self.width:
            self.x += self.speed_lateral
        if keys[pygame.K_UP] and self.y > self.screen_height // 2:
            self.y -= self.speed
        if keys[pygame.K_DOWN] and self.y < self.screen_height - self.height:
            self.y += self.speed

    def draw(self, screen):
        pygame.draw.rect(screen, (0, 0, 255), (self.x, self.y, self.width, self.height))
# END ChatGPT Code
