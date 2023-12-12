import pygame
from fsm import FSM

class Ai_opponent:
    def __init__(self, screen_width, screen_height):
        # Initialize AI attributes, such as paddle position, speed, etc.
        self.width = 20
        self.height = 80
        self.screen_height = screen_height
        self.screen_width = screen_width
        self.x = (screen_width - self.width) // 2
        self.y = 10
        self.speed_forward = 5  # Speed for forward and backward movement
        self.speed_sideways = 2  # Speed for left and right movement

    def update(self, ball, ball_has_moved):
        # Implement AI logic to move the paddle in response to the ball's position
        if ball_has_moved:
            if ball.y < self.y:
                self.y -= self.speed_forward
            elif ball.y > self.y + self.height:
                self.y += self.speed_forward
            
            # Ensure AI cross net or move off screen
            # made by me
            if self.y >= self.screen_height/2 - self.height:  # Adjust the value according to the net position
                self.y = self.screen_height/2 - self.height
            if self.y <= 0:  # Adjust the value according to the net position
                self.y = 0
            if self.x <= 0:
                self.x = 0
            if self.x >= self.screen_width - self.width:
                self.x = self.screen_width - self.width

            
            # Move sideways (left and right)
            if ball.x < self.x:
                self.x -= self.speed_sideways
            elif ball.x > self.x + self.width:
                self.x += self.speed_sideways

            # # Move towards the spawn point if the ball is in the opponent's half
            # if ball.y > self.screen_height / 2:
            #     if self.x < self.screen_width / 2:
            #         self.x += self.speed_sideways
            #     elif self.x > self.screen_width / 2:
            #         self.x -= self.speed_sideways


            

    def draw(self, screen):
        # Draw the AI paddle
        pygame.draw.rect(screen, (255, 0, 0), (self.x, self.y, self.width, self.height))