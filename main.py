# Metal Slug Game

## Features
- **Login and Signup Screens**: Users can create an account or log in to play the game.
- **Level Selection**: Players can choose from levels 1 to 5, each with varying difficulty.
- **Shooting Mechanics**: Players can shoot enemies and interact with the game world.
- **Enemy Spawning System**: Enemies spawn at various points and provide challenges to players.
- **Health and Score Tracking**: The game tracks player health and score throughout gameplay.
- **Improved UI Design**: Enhanced user interface for easier navigation and an engaging player experience.

## Code Structure

```python
import pygame

class Game:
    def __init__(self):
        self.score = 0
        self.health = 100
        self.level = 1
        self.login_screen()

    def login_screen(self):
        # Code for login screen
        pass
    
    def signup_screen(self):
        # Code for signup screen
        pass
    
    def start_game(self):
        # Code to initialize the game
        pass
    
    def spawn_enemies(self):
        # Code to handle enemy spawning
        pass
    
    def update_score(self):
        # Code to update score
        pass
    
    def draw_ui(self):
        # Code to draw the user interface
        pass

if __name__ == "__main__":
    Game() 
```

## Instructions
1. Ensure you have Python and Pygame installed.
2. Run the game by executing `python main.py`.
3. Follow instructions on the screen for login and gameplay.

## Future Improvements
- Add multiplayer functionality
- Implement additional levels and enemies
- Optimize performance for smoother gameplay