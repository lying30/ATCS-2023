# Lucas Ying - 12/18
# Note: Any code that was not shown to be coded by ChatGPT was coded by myself
 
import pygame
from fsm import FSM

class Ai_opponent:
    def __init__(self, screen_width, screen_height):
        # Initialize AI attributes, such as paddle position, speed, etc.
        self.width = 20
        self.height = 80
        self.screen_height = screen_height
        self.screen_width = screen_width
        self.XSTART = (screen_width - self.width) // 2
        self.YSTART = 10
        self.x = self.XSTART
        self.y = self.YSTART
        self.speed_forward = 4.7  # Speed for forward movement
        self.speed_sideways = 3  # Speed for left and right movement
        self.speed_backwards = 2.6 # Speed for backward movement

    def update(self, ball, ball_has_moved):
        # Implement AI logic to move the paddle in response to the ball's position
        if ball_has_moved:
            if ball.y < self.screen_height / 2:
                if ball.y < self.y:
                    self.y -= self.speed_backwards
                elif ball.y > self.y + self.height:
                    self.y += self.speed_forward
            # Recovers the y to the center of court after ball crosses the net
            elif self.y < self.YSTART:
                self.y += self.speed_forward
            elif self.y > self.YSTART:
                self.y -= self.speed_backwards
            elif self.y == self.YSTART:
                self.y += 0

            
            # Ensure AI cross net or move off screen
            if self.y >= self.screen_height/2 - self.height:
                self.y = self.screen_height/2 - self.height
            if self.y <= 0: 
                self.y = 0
            if self.x <= 0:
                self.x = 0
            if self.x >= self.screen_width - self.width:
                self.x = self.screen_width - self.width

            # If ball is on AI side of court
            # Move sideways (left and right)
            if ball.y < self.screen_height / 2:
                if ball.x < self.x:
                    self.x -= self.speed_sideways
                elif ball.x > self.x + self.width:
                    self.x += self.speed_sideways
            elif self.x < self.XSTART:
                self.x += self.speed_sideways
            elif self.x > self.XSTART:
                self.x -= self.speed_sideways
            elif self.x == self.XSTART:
                self.x += 0


            

    def draw(self, screen):
        # Draw the AI paddle
        pygame.draw.rect(screen, (255, 0, 0), (self.x, self.y, self.width, self.height))