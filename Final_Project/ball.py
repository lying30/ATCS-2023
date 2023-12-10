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

        # FSM states
        self.SPAWN, self.MOVE_UP, self.MOVE_DOWN, self.HIT_PLAYER, self.HIT_AI, self.GAME_OVER = range(8)

        self.fsm = FSM(self.SPAWN)
        self.init_fsm()

        # Time variables to track how long keys are held down
        self.key_up_pressed_time = 0
        self.key_down_pressed_time = 0
        self.key_left_pressed_time = 0
        self.key_right_pressed_time = 0

        # Factors to adjust speed based on key press duration
        self.speed_multiplier = 1.5  # Modify this value to suit your game

    def init_fsm(self):
        # I did this
        # Spawned with player, move up + direction
        self.fsm.add_transition("move_left", self.SPAWN, self.move_1, self.MOVE_UP)
        self.fsm.add_transition("move_left_middle", self.SPAWN, self.move_2, self.MOVE_UP)
        self.fsm.add_transition("move_right_middle", self.SPAWN, self.move_3, self.MOVE_UP)
        self.fsm.add_transition("move_right", self.SPAWN, self.move_4, self.MOVE_UP)

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


        # ... Add other transitions as per ball's behavior in the game

    def get_state(self):
        return self.fsm.current_state

    # Methods for ball movement based on transitions
    def move_1(self):
        self.velocity_y = -self.speed

    def move_2(self):
        self.velocity_y = self.speed

    def move_3(self):
        self.velocity_x = -self.speed

    def move_4(self):
        self.velocity_x = self.speed

    def stop_vertical_movement(self):
        self.velocity_y = 0

    def stop_horizontal_movement(self):
        self.velocity_x = 0

    def update(self):
        # Update ball's position based on its velocity
        self.x += self.velocity_x
        self.y += self.velocity_y

        # Process input and adjust ball's direction and speed based on key press duration
        self.handle_input()

    def handle_input(self):
        # Reset velocities
        self.velocity_x = 0
        self.velocity_y = 0

        # Check keyboard input for arrow keys or any other keys you want to use
        keys = pygame.key.get_pressed()

        # Calculate time key is held down
        if keys[pygame.K_UP]:
            self.key_up_pressed_time += 1
        else:
            self.key_up_pressed_time = 0

        if keys[pygame.K_DOWN]:
            self.key_down_pressed_time += 1
        else:
            self.key_down_pressed_time = 0

        if keys[pygame.K_LEFT]:
            self.key_left_pressed_time += 1
        else:
            self.key_left_pressed_time = 0

        if keys[pygame.K_RIGHT]:
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

    def check_collision_with_player(self, player):
        # Implement collision detection logic with the player paddle
        pass

    def check_collision_with_ai(self, ai):
        # Implement collision detection logic with the AI paddle
        pass

    def draw(self, screen):
        # Draw the ball on the screen (implement drawing logic here)
        pass
