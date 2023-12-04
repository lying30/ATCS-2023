# import pygame
# import sys

# class Game:
#     def __init__(self):
#         pygame.init()
#         self.screen_width = 450
#         self.screen_height = 750
#         self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
#         pygame.display.set_caption("Tennis Game")
#         self.clock = pygame.time.Clock()
#         self.player_width = 20
#         self.player_height = 80
#         self.player_x = (self.screen_width - self.player_width) // 2
#         self.player_y = self.screen_height - self.player_height - 10
#         self.player_speed = 5
#         self.game_running = True
#         self.net_width = 5
#         self.net_color = (255, 255, 255)
#         self.net_position = self.screen_height // 2 - self.net_width // 2

#     def run_game(self):
#         while self.game_running:
#             self.screen.fill((0, 128, 0))  # Fill the screen with green color

#             for event in pygame.event.get():
#                 if event.type == pygame.QUIT:
#                     self.game_running = False

#             keys = pygame.key.get_pressed()
#             if keys[pygame.K_LEFT] and self.player_x > 0:
#                 self.player_x -= self.player_speed
#             if keys[pygame.K_RIGHT] and self.player_x < self.screen_width - self.player_width:
#                 self.player_x += self.player_speed
#             if keys[pygame.K_UP] and self.player_y > self.screen_height // 2:
#                 self.player_y -= self.player_speed
#             if keys[pygame.K_DOWN] and self.player_y < self.screen_height - self.player_height:
#                 self.player_y += self.player_speed

#             # Restrict the player to the bottom half of the court
#             if self.player_y < self.screen_height // 2:
#                 self.player_y = self.screen_height // 2
#             if self.player_y > self.screen_height - self.player_height:
#                 self.player_y = self.screen_height - self.player_height

#             # Draw the tennis court
#             pygame.draw.rect(self.screen, (255, 255, 255), (0, 0, self.screen_width, self.screen_height))  # White background
#             pygame.draw.rect(self.screen, (34, 139, 34), (50, 50, self.screen_width - 100, self.screen_height // 2 - 50))  # Green court (top)
#             pygame.draw.rect(self.screen, (34, 139, 34), (50, self.screen_height // 2, self.screen_width - 100, self.screen_height // 2 - 50))  # Green court (bottom)
#             pygame.draw.rect(self.screen, self.net_color, (0, self.screen_height // 2 - self.net_width // 2, self.screen_width, self.net_width))  # Net

#             # Draw the player paddle
#             pygame.draw.rect(self.screen, (0, 0, 255), (self.player_x, self.player_y, self.player_width, self.player_height))

#             pygame.display.flip()
#             self.clock.tick(60)

#         pygame.quit()

# if __name__ == "__main__":
#     game = Game()
#     game.run_game()
