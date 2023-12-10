import pygame
from fsm import FSM

class AI:
    def __init__(self, screen_width, screen_height):
        # Initialize AI attributes, such as paddle position, speed, etc.
        self.width = 20
        self.height = 80
        self.x = (screen_width - self.width) // 2
        self.y = 10
        self.speed = 5

    def update(self, ball):
        # Implement AI logic to move the paddle in response to the ball's position
        if ball.y < self.y:
            self.y -= self.speed
        elif ball.y > self.y + self.height:
            self.y += self.speed

    def draw(self, screen):
        # Draw the AI paddle
        pygame.draw.rect(screen, (255, 0, 0), (self.x, self.y, self.width, self.height))
