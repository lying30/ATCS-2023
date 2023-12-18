import pygame
from fsm import FSM

class Ball:
    def __init__(self, x, y):
        # Ball properties
        self.x = x
        self.y = y
        self.velocity_x = 0
        self.velocity_y = 0
        self.speed = 5
        self.ball_radius = 10

        self.screen_width = 450
        self.screen_height = 750

        self.ball_started_moving = False

        # FSM states
        self.SPAWN, self.MOVE_UP, self.MOVE_DOWN, self.HIT_PLAYER, self.HIT_AI, self.GAME_OVER = range(6)

        self.fsm = FSM(self.SPAWN)
        self.init_fsm()

        # Time variables to track how long keys are held down
        self.key_up_pressed_time = 0
        self.key_down_pressed_time = 0
        self.key_left_pressed_time = 0
        self.key_right_pressed_time = 0

    # Start ChatGPT Code: Factors to adjust speed based on key press duration
        self.speed_multiplier = 1.5  # Modify this value to suit your game
    # End ChatGPT Code

    def init_fsm(self):
        # Spawned with player, move up + direction
        self.fsm.add_transition("move_left", self.SPAWN, self.move_1, self.MOVE_UP)
        self.fsm.add_transition("move_left_middle", self.SPAWN, self.move_2, self.MOVE_UP)
        self.fsm.add_transition("move_right_middle", self.SPAWN, self.move_3, self.MOVE_UP)
        self.fsm.add_transition("move_right", self.SPAWN, self.move_4, self.MOVE_UP)

        # Moving up, keep moving
        self.fsm.add_transition("move_left", self.MOVE_UP, self.move_1, self.MOVE_UP)
        self.fsm.add_transition("move_left_middle", self.MOVE_UP, self.move_2, self.MOVE_UP)
        self.fsm.add_transition("move_right_middle", self.MOVE_UP, self.move_3, self.MOVE_UP)
        self.fsm.add_transition("move_right", self.MOVE_UP, self.move_4, self.MOVE_UP)
        
        # Moving up, keep moving
        self.fsm.add_transition("move_left", self.MOVE_DOWN, self.move_1, self.MOVE_DOWN)
        self.fsm.add_transition("move_left_middle", self.MOVE_DOWN, self.move_2, self.MOVE_DOWN)
        self.fsm.add_transition("move_right_middle", self.MOVE_DOWN, self.move_3, self.MOVE_DOWN)
        self.fsm.add_transition("move_right", self.MOVE_DOWN, self.move_4, self.MOVE_DOWN)

        # Contact with AI, move down + direction
        self.fsm.add_transition("move_left", self.HIT_AI, self.move_1, self.MOVE_DOWN)
        self.fsm.add_transition("move_left_middle", self.HIT_AI, self.move_2, self.MOVE_DOWN)
        self.fsm.add_transition("move_right_middle", self.HIT_AI, self.move_3, self.MOVE_DOWN)
        self.fsm.add_transition("move_right", self.HIT_AI, self.move_4, self.MOVE_DOWN)    
        
        # Contact with PLayer, move up + direction
        self.fsm.add_transition("move_left", self.HIT_PLAYER, self.move_1, self.MOVE_UP)
        self.fsm.add_transition("move_left_middle", self.HIT_PLAYER, self.move_2, self.MOVE_UP)
        self.fsm.add_transition("move_right_middle", self.HIT_PLAYER, self.move_3, self.MOVE_UP)
        self.fsm.add_transition("move_right", self.HIT_PLAYER, self.move_4, self.MOVE_UP)

    def get_state(self):
        return self.fsm.current_state

# Start ChatGPT Code: Methods for ball movement based on transitions
    def move_1(self):
        self.ball_started_moving = True
        # Calculate rise and run for moving to the left side of the court
        rise = -self.y  # Move upwards to reach the left side (negative y-coordinate)
        run = -self.x  # Move leftwards to reach the left side (negative x-coordinate)

        # Calculate the slope (rise over run)
        if run != 0:  # Avoid division by zero
            slope = rise / run
            # Set the velocity based on slope
            self.velocity_y = -self.speed * slope
            self.velocity_x = -self.speed

    def move_2(self):
        self.ball_started_moving = True
        # Calculate rise and run for moving to the left-middle side of the court
        # Assuming left-middle is at 1/4th of the x-coordinate range
        run = -self.x / 2  # Move leftwards to reach the left-middle side (negative x-coordinate)
        rise = -self.y  # Move upwards to reach the left-middle side (negative y-coordinate)

        # Calculate the slope (rise over run)
        if run != 0:  # Avoid division by zero
            slope = rise / run
            # Set the velocity based on slope
            self.velocity_y = -self.speed * slope
            self.velocity_x = -self.speed

    def move_3(self):
        self.ball_started_moving = True
        # Calculate rise and run for moving to the right-middle side of the court
        # Assuming right-middle is at 3/4th of the x-coordinate range
        run = self.screen_width - self.x  # Move rightwards to reach the right-middle side (positive x-coordinate)
        rise = -self.y  # Move upwards to reach the right-middle side (negative y-coordinate)

        # Calculate the slope (rise over run)
        if run != 0:  # Avoid division by zero
            slope = rise / run
            # Set the velocity based on slope
            self.velocity_y = -self.speed * slope
            self.velocity_x = self.speed

    def move_4(self):
        self.ball_started_moving = True
        # Calculate rise and run for moving to the right side of the court
        rise = self.screen_height - self.y  # Move downwards to reach the right side (positive y-coordinate)
        run = self.screen_width - self.x  # Move rightwards to reach the right side (positive x-coordinate)

        # Calculate the slope (rise over run)
        if run != 0:  # Avoid division by zero
            slope = rise / run
            # Set the velocity based on slope
            self.velocity_y = -self.speed * slope
            self.velocity_x = self.speed

    def stop_vertical_movement(self):
        self.velocity_y = 0

    def stop_horizontal_movement(self):
        self.velocity_x = 0
# End ChatGPT Code

    def update(self):
        # Update ball's position based on its velocity
        self.x += self.velocity_x
        self.y += self.velocity_y

        # Restrict ball boundaries
        if self.y >= self.screen_height:  
            self.y = self.screen_height
        if self.y <= 0: 
            self.y = 0
        if self.x <= 0:
            self.x = 0
        if self.x >= self.screen_width:
            self.x = self.screen_width

        # Process input and adjust ball's direction and speed based on key press duration
        self.handle_input()

# Start ChatGPT Code:
    def handle_input(self):
        # Reset velocities
        self.velocity_x = 0
        self.velocity_y = 0

        # Check keyboard input for arrow keys or any other keys you want to use
        keys = pygame.key.get_pressed()

        # Calculate time key is held down
        if keys[pygame.K_1]:
            self.fsm.process("move_left")  # Corresponding to move1 method in FSM transitions
            self.key_up_pressed_time += 1
        else:
            self.key_up_pressed_time = 0

        if keys[pygame.K_2]:
            self.fsm.process("move_left_middle")  # Corresponding to move1 method in FSM transitions
            self.key_down_pressed_time += 1
        else:
            self.key_down_pressed_time = 0

        if keys[pygame.K_3]:
            self.fsm.process("move_right_middle")  # Corresponding to move1 method in FSM transitions
            self.key_left_pressed_time += 1
        else:
            self.key_left_pressed_time = 0

        if keys[pygame.K_4]:
            self.fsm.process("move_right")  # Corresponding to move1 method in FSM transitions
            self.key_right_pressed_time += 1
        else:
            self.key_right_pressed_time = 0

        # Adjust ball's direction and speed based on key press duration
        if self.key_up_pressed_time > 0:
            self.velocity_y -= self.speed * self.speed_multiplier * self.key_up_pressed_time / 100
        if self.key_down_pressed_time > 0:
            self.velocity_y += self.speed * self.speed_multiplier * self.key_down_pressed_time / 100
        if self.key_left_pressed_time > 0:
            self.velocity_x -= self.speed * self.speed_multiplier * self.key_left_pressed_time / 100
        if self.key_right_pressed_time > 0:
            self.velocity_x += self.speed * self.speed_multiplier * self.key_right_pressed_time / 100
# End ChatGPT Code


    # def check_collision_with_player(self, player):
    #     # Implement collision detection logic with the player paddle
    #     if (self.x < player.x + player.width and
    #             self.x + self.ball_radius > player.x and
    #             self.y < player.y + player.height and
    #             self.y + self.ball_radius > player.y):
    #         # Collision detected with player
    #         # Adjust the ball's direction upon collision with the player
    #         self.velocity_x *= -1  # Reverse ball's x-direction
    #         # Adjust other aspects of the ball's behavior upon collision with the player if needed


    # def check_collision_with_ai(self, ai):
    #     # Implement collision detection logic with the AI paddle
    #     if (self.x < ai.x + ai.width and
    #             self.x + self.ball_radius > ai.x and
    #             self.y < ai.y + ai.height and
    #             self.y + self.ball_radius > ai.y):
    #         # Collision detected with AI paddle
    #         # Adjust the ball's direction upon collision with the AI paddle
    #         self.velocity_x *= -1  # Reverse ball's x-direction
    #         # Adjust other aspects of the ball's behavior upon collision with the AI paddle if needed

    def draw(self, screen):
        # Draw the ball on the screen
        pygame.draw.circle(screen, (255, 255, 0), (self.x, self.y), self.ball_radius)
