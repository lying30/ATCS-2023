class Ball:
    def __init__(self, x, y):
        self.x = x  # x-coordinate of the ball
        self.y = y  # y-coordinate of the ball
        self.velocity_x = 0  # horizontal velocity of the ball
        self.velocity_y = 0  # vertical velocity of the ball
        self.state = "spawn"  # initial state of the ball

    def move_up(self):
        # Change the vertical velocity to move the ball upwards
        self.velocity_y = -1

    def move_down(self):
        # Change the vertical velocity to move the ball downwards
        self.velocity_y = 1

    def stop_vertical_movement(self):
        # Stop the vertical movement of the ball
        self.velocity_y = 0

    def spawn(self, x, y):
        # Spawn the ball at the specified coordinates
        self.x = x
        self.y = y
        self.state = "spawn"
        # Additional logic for initialization if needed

    def update(self):
        # Update the ball's position based on its velocity
        self.x += self.velocity_x
        self.y += self.velocity_y

        # FSM to control the states of the ball
        if self.state == "spawn":
            # Additional logic for spawn state
            pass
        # Add other states and corresponding logic here

    def check_collision_with_player(self, player):
        # Check collision with the player paddle
        # Perform collision detection logic here
        pass

    def check_collision_with_ai(self, ai):
        # Check collision with the AI paddle
        # Perform collision detection logic here
        pass

# Example usage:
# Create a ball object
ball = Ball(100, 100)

# Update the ball's state and position in the game loop
while True:
    # Update ball's position
    ball.update()

    # Check collisions with player and AI
    ball.check_collision_with_player(player)  # Assuming 'player' is the user's paddle object
    ball.check_collision_with_ai(ai)  # Assuming 'ai' is the AI's paddle object
