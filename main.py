import pygame
import random

# Initialize Pygame
pygame.init()

# Game Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
BALL_SIZE = 20

# User data storage
users = {}  # Dictionary to store username and password pairs

# Function for user signup
def signup(username, password):
    if username in users:
        return "Username already exists."
    users[username] = password
    return "Signup successful!"

# Function for user login
def login(username, password):
    if users.get(username) == password:
        return "Login successful!"
    return "Invalid username or password."

# Difficulty levels
levels = {1: 5, 2: 8, 3: 12, 4: 15, 5: 20}

# Ball class for the bouncing ball
class Ball:
    def __init__(self):
        self.x = SCREEN_WIDTH // 2
        self.y = SCREEN_HEIGHT // 2
        self.x_speed = random.choice([-1, 1]) * random.randint(5, 10)
        self.y_speed = random.choice([-1, 1]) * random.randint(5, 10)

    def move(self):
        self.x += self.x_speed
        self.y += self.y_speed

        # Bounce off the walls
        if self.x <= 0 or self.x >= SCREEN_WIDTH:
            self.x_speed *= -1
        if self.y <= 0 or self.y >= SCREEN_HEIGHT:
            self.y_speed *= -1

# Main game function
def play_game(difficulty):
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Bouncing Ball Game")
    clock = pygame.time.Clock()
    ball = Ball()
    game_running = True

    while game_running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_running = False

        screen.fill((0, 0, 0))  # Clear screen with black
        ball.move()
        pygame.draw.circle(screen, (255, 0, 0), (ball.x, ball.y), BALL_SIZE)

        pygame.display.flip()  # Update the screen
        clock.tick(levels[difficulty])  # Control the speed based on difficulty

    pygame.quit()

# Example usage of signup and login functions
print(signup('player1', 'password123'))  # Example to signup
print(login('player1', 'password123'))  # Example to login

# Start the game - adjust difficulty level as needed
play_game(3)  # Start the game with difficulty level 3