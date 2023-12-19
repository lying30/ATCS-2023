# Lucas Ying - 12/18
# Note: Any code that was not shown to be coded by ChatGPT was coded by myself
 
import pygame
from fsm import FSM
import random
import math
# CONTENT STANDARDS: Using a FSM throughout the whole ball class.

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
        
        # Moving up, start moving down
        self.fsm.add_transition("move_left", self.MOVE_DOWN, self.move_1, self.MOVE_DOWN)
        self.fsm.add_transition("move_left_middle", self.MOVE_DOWN, self.move_2, self.MOVE_DOWN)
        self.fsm.add_transition("move_right_middle", self.MOVE_DOWN, self.move_3, self.MOVE_DOWN)
        self.fsm.add_transition("move_right", self.MOVE_DOWN, self.move_4, self.MOVE_DOWN)

        # Contact with AI, move down + direction
        self.fsm.add_transition("move_left_ai", self.HIT_AI, self.move_1_ai, self.MOVE_DOWN)
        self.fsm.add_transition("move_left_middle_ai", self.HIT_AI, self.move_2_ai, self.MOVE_DOWN)
        self.fsm.add_transition("move_right_middle_ai", self.HIT_AI, self.move_3_ai, self.MOVE_DOWN)
        self.fsm.add_transition("move_right_ai", self.HIT_AI, self.move_4_ai, self.MOVE_DOWN)    
        
        # Contact with AI, keep moving
        self.fsm.add_transition("move_left_ai", self.MOVE_DOWN, self.move_1_ai, self.MOVE_DOWN)
        self.fsm.add_transition("move_left_middle_ai", self.MOVE_DOWN, self.move_2_ai, self.MOVE_DOWN)
        self.fsm.add_transition("move_right_middle_ai", self.MOVE_DOWN, self.move_3_ai, self.MOVE_DOWN)
        self.fsm.add_transition("move_right_ai", self.MOVE_DOWN, self.move_4_ai, self.MOVE_DOWN)    

        # Contact with Player, move up + direction
        self.fsm.add_transition("move_left", self.HIT_PLAYER, self.move_1, self.MOVE_UP)
        self.fsm.add_transition("move_left_middle", self.HIT_PLAYER, self.move_2, self.MOVE_UP)
        self.fsm.add_transition("move_right_middle", self.HIT_PLAYER, self.move_3, self.MOVE_UP)
        self.fsm.add_transition("move_right", self.HIT_PLAYER, self.move_4, self.MOVE_UP)

    # Contact with Player, keep moving
        self.fsm.add_transition("move_left", self.MOVE_UP, self.move_1, self.MOVE_UP)
        self.fsm.add_transition("move_left_middle", self.MOVE_UP, self.move_2, self.MOVE_UP)
        self.fsm.add_transition("move_right_middle", self.MOVE_UP, self.move_3, self.MOVE_UP)
        self.fsm.add_transition("move_right", self.MOVE_UP, self.move_4, self.MOVE_UP)

        # New transitions for collisions
        self.fsm.add_transition("hit_player", self.MOVE_UP, None, self.HIT_PLAYER)
        self.fsm.add_transition("hit_player", self.MOVE_DOWN, None, self.HIT_PLAYER)
        self.fsm.add_transition("hit_player", self.SPAWN, None, self.HIT_PLAYER)
        self.fsm.add_transition("hit_player", self.HIT_PLAYER, None, self.HIT_PLAYER)

        self.fsm.add_transition("hit_ai", self.MOVE_UP, None, self.HIT_AI)
        self.fsm.add_transition("hit_ai", self.MOVE_DOWN, None, self.HIT_AI)
        self.fsm.add_transition("hit_ai", self.SPAWN, None, self.HIT_AI)
        self.fsm.add_transition("hit_ai", self.HIT_AI, None, self.HIT_AI)

    def get_state(self):
        return self.fsm.current_state

# Start ChatGPT Code: Methods for ball movement based on transitions
    # Note: Couldn't figure out direction so that the balls would go back and forth, right now the ball 
    # goes up but then the AI doesn't send the ball back down.
    def move_1(self):
        self.ball_started_moving = True
        # Calculate the angle in radians (60 degrees = pi / 3 radians)
        angle_radians = math.radians(100)

        # Calculate velocity components based on the angle
        self.velocity_x = self.speed * math.cos(angle_radians)
        self.velocity_y = -self.speed * math.sin(angle_radians)

    def move_2(self):
        self.ball_started_moving = True
        # Calculate the angle in radians (60 degrees = pi / 3 radians)
        angle_radians = math.radians(93)

        # Calculate velocity components based on the angle
        self.velocity_x = self.speed * math.cos(angle_radians)
        self.velocity_y = -self.speed * math.sin(angle_radians)

    def move_3(self):
        self.ball_started_moving = True
        # Calculate the angle in radians (60 degrees = pi / 3 radians)
        angle_radians = math.radians(88)

        # Calculate velocity components based on the angle
        self.velocity_x = self.speed * math.cos(angle_radians)
        self.velocity_y = -self.speed * math.sin(angle_radians)

    def move_4(self):
        self.ball_started_moving = True
        # Calculate the angle in radians (60 degrees = pi / 3 radians)
        angle_radians = math.radians(80)

        # Calculate velocity components based on the angle
        self.velocity_x = self.speed * math.cos(angle_radians)
        self.velocity_y = -self.speed * math.sin(angle_radians)

    def move_1_ai(self):
        self.ball_started_moving = True
        # Calculate the angle in radians (60 degrees = pi / 3 radians) for downward movement
        angle_radians = math.radians(262)

        # Calculate velocity components based on the angle
        self.velocity_x = self.speed * math.cos(angle_radians)
        self.velocity_y = self.speed * math.sin(angle_radians)

    def move_2_ai(self):
        self.ball_started_moving = True
        # Calculate the angle in radians (60 degrees = pi / 3 radians) for downward movement
        angle_radians = math.radians(267)

        # Calculate velocity components based on the angle
        self.velocity_x = self.speed * math.cos(angle_radians)
        self.velocity_y = self.speed * math.sin(angle_radians)

    def move_3_ai(self):
        self.ball_started_moving = True
        # Calculate the angle in radians (60 degrees = pi / 3 radians) for downward movement
        angle_radians = math.radians(273)

        # Calculate velocity components based on the angle
        self.velocity_x = self.speed * math.cos(angle_radians)
        self.velocity_y = self.speed * math.sin(angle_radians)

    def move_4_ai(self):
        self.ball_started_moving = True
        # Calculate the angle in radians (60 degrees = pi / 3 radians) for downward movement
        angle_radians = math.radians(278)

        # Calculate velocity components based on the angle
        self.velocity_x = self.speed * math.cos(angle_radians)
        self.velocity_y = self.speed * math.sin(angle_radians)
    

    def stop_vertical_movement(self):
        self.velocity_y = 0

    def stop_horizontal_movement(self):
        self.velocity_x = 0
# End ChatGPT Code

    def update(self, boolean_player, boolean_ai):
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
        self.handle_input(boolean_player, boolean_ai)

# Start ChatGPT Code:
    def handle_input(self, boolean_player, boolean_ai):
        # Reset velocities
        self.velocity_x = 0
        self.velocity_y = 0

        # Check keyboard input for arrow keys or any other keys you want to use
        keys = pygame.key.get_pressed()

        if boolean_player:
            # Calculate time key is held down
            if keys[pygame.K_1]:
                self.fsm.process("move_left")  # Corresponding to move1 method in FSM transitions
                self.key_up_pressed_time += 5
            else:
                self.key_up_pressed_time = 0

            if keys[pygame.K_2]:
                self.fsm.process("move_left_middle")  # Corresponding to move1 method in FSM transitions
                self.key_down_pressed_time += 5
            else:
                self.key_down_pressed_time = 0

            if keys[pygame.K_3]:
                self.fsm.process("move_right_middle")  # Corresponding to move1 method in FSM transitions
                self.key_left_pressed_time += 5
            else:
                self.key_left_pressed_time = 0

            if keys[pygame.K_4]:
                self.fsm.process("move_right")  # Corresponding to move1 method in FSM transitions
                self.key_right_pressed_time += 5
                
            else:
                self.key_right_pressed_time = 0


        if boolean_ai:
            # Random choice of direction
            random_direction = random.randint(1, 4)

            if random_direction:
                self.fsm.process("move_left_ai")  # Corresponding to move1 method in FSM transitions
                self.key_up_pressed_time += 5
            else:
                self.key_up_pressed_time = 0

            if random_direction:
                self.fsm.process("move_left_middle_ai")  # Corresponding to move2 method in FSM transitions
                self.key_down_pressed_time += 5
            else:
                self.key_down_pressed_time = 0

            if random_direction:
                self.fsm.process("move_right_middle_ai")  # Corresponding to move3 method in FSM transitions
                self.key_left_pressed_time += 5
            else:
                self.key_left_pressed_time = 0

            if random_direction:
                self.fsm.process("move_right_ai")  # Corresponding to move4 method in FSM transitions
                self.key_right_pressed_time += 5
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



    def check_collision_with_player(self, player):
        # Define a collision threshold of 50 units around the player's paddle
        collision_threshold = 50

        # Implement collision detection logic with the player paddle
        if (self.x < player.x + player.width + collision_threshold and
            self.x + self.ball_radius > player.x - collision_threshold and
            self.y < player.y + player.height + collision_threshold and
            self.y + self.ball_radius > player.y - collision_threshold):
            # Collision detected with player within 50 units
            # Adjust the ball's direction upon collision with the player
            self.fsm.process("hit_player")
            return True
            # Adjust other aspects of the ball's behavior upon collision with the player if needed


    def check_collision_with_ai(self, ai):
        # Define a collision threshold of 50 units around the AI paddle
        collision_threshold = 50

        # Implement collision detection logic with the AI paddle
        if (self.x < ai.x + ai.width + collision_threshold and
            self.x + self.ball_radius > ai.x - collision_threshold and
            self.y < ai.y + ai.height + collision_threshold and
            self.y + self.ball_radius > ai.y - collision_threshold):
            # Collision detected with AI paddle within 50 units
            # Adjust the ball's direction upon collision with the AI paddle
            self.fsm.process("hit_ai")
            return True  # Reverse ball's x-direction
            # Adjust other aspects of the ball's behavior upon collision with the AI paddle if needed

# End ChatGPT Code

    def draw(self, screen):
        # Draw the ball on the screen
        pygame.draw.circle(screen, (255, 255, 0), (self.x, self.y), self.ball_radius)
