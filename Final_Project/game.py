import pygame
import sys
from ball import Ball
from Ai_opponent import Ai_opponent
from player import Player

# START ChatGPT Code:
class Game:
    def __init__(self):

        pygame.init()
        self.screen_width = 450
        self.screen_height = 750
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        pygame.display.set_caption("Tennis Game")
        self.clock = pygame.time.Clock()
        self.game_running = True
        self.net_width = 5
        self.net_color = (255, 255, 255)
        self.net_position = self.screen_height // 2 - self.net_width // 2

        self.player = Player(self.screen_width, self.screen_height)
        self.ball = Ball(self.player.x, self.player.y)
        self.ai_opponent = Ai_opponent(self.screen_width, self.screen_height)

    def run_game(self):

        while self.game_running:
            self.screen.fill((0, 128, 0))  # Fill the screen with green color

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.game_running = False

            # Update AI and ball based on game logic
            self.ai_opponent.update(self.ball, self.ball.ball_started_moving)

            # Update ball's position and behavior
            self.ball.update()

            keys = pygame.key.get_pressed()
            self.player.update(keys)    
                    
            # self.ball.check_collision_with_player(self.player)
            # self.ball.check_collision_with_ai(self.ai_opponent)


            # Restrict the player to the bottom half of the court
            if self.player.y < self.screen_height // 2:
                self.player.y = self.screen_height // 2
            if self.player.y > self.screen_height - self.player.height:
                self.player.y = self.screen_height - self.player.height

            # Draw the tennis court
            pygame.draw.rect(self.screen, (255, 255, 255), (0, 0, self.screen_width, self.screen_height))  # White background
            pygame.draw.rect(self.screen, (34, 139, 34), (50, 50, self.screen_width - 100, self.screen_height // 2 - 50))  # Green court (top)
            pygame.draw.rect(self.screen, (34, 139, 34), (50, self.screen_height // 2, self.screen_width - 100, self.screen_height // 2 - 50))  # Green court (bottom)
            pygame.draw.rect(self.screen, self.net_color, (0, self.screen_height // 2 - self.net_width // 2, self.screen_width, self.net_width))  # Net

            # Draw the player paddle
            self.player.draw(self.screen)
            
            # Draw the ball
            self.ball.draw(self.screen)

            # Draw the AI opponent
            self.ai_opponent.draw(self.screen)

            pygame.display.flip()
            self.clock.tick(60)

        pygame.quit()

if __name__ == "__main__":
    game = Game()
    game.run_game()

# END ChatGPT Code: