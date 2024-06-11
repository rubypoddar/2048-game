# 2048 Game in Pygame

![2048 Game](https://i.pinimg.com/736x/b0/94/de/b094de96f5c2fd59e1ef0128b87f5052.jpg)

[![GitHub issues](https://img.shields.io/github/issues/rubypoddar/2048-game)](https://github.com/rubypoddar/2048-game/issues)
[![GitHub forks](https://img.shields.io/github/forks/rubypoddar/2048-game)](https://github.com/rubypoddar/2048-game/network)
[![GitHub stars](https://img.shields.io/github/stars/rubypoddar/2048-game)](https://github.com/rubypoddar/2048-game/stargazers)
[![GitHub license](https://img.shields.io/github/license/rubypoddar/2048-game)](https://github.com/rubypoddar/2048-game/blob/main/LICENSE)

This repository contains an implementation of the classic puzzle game "2048" using the Pygame library. The objective of the game is to slide numbered tiles on a grid to combine them and create a tile with the number 2048.

## Features

- **4x4 Grid**: A simple 4x4 grid where tiles are moved and combined.
- **Tile Colors**: Distinct colors for different tile values.
- **Score Tracking**: Displays the current score.
- **New Game Button**: Allows the player to start a new game at any time.
- **Keyboard Controls**: Use arrow keys to move tiles in the desired direction.

## Installation

1. **Clone the repository**:
   ```sh
   git clone https://github.com/rubypoddar/2048-game.git
   cd 2048-game
   ```

2. **Install Pygame**:
   Make sure you have Python installed, then install Pygame using pip:
   ```sh
   pip install pygame
   ```

3. **Run the game**:
   ```sh
   python game.py
   ```

## Controls

- **Arrow Keys**: Use the arrow keys to move the tiles left, right, up, or down.
- **New Game Button**: Click the "New Game" button to reset and start a new game.

## Code Overview

- **Constants and Initialization**: Sets up game dimensions, colors, and initializes Pygame.
- **UI Elements**: Functions to draw the grid, tiles, and "New Game" button.
- **Game Functions**: Logic for generating new tiles, moving and merging tiles, and resetting the game.
- **Main Game Loop**: Handles user input, updates the game state, and redraws the screen.

## Future Improvements

- **High Score**: Save and display the highest score achieved.
- **Animations**: Add smooth animations for tile movements and merges.
- **Game Over Detection**: Implement game over logic when no more moves are possible.

## Contributing

Contributions are welcome! Please fork the repository and submit pull requests for any features, enhancements, or bug fixes.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Repository Stats

![GitHub repo size](https://img.shields.io/github/repo-size/rubypoddar/2048-game)
![GitHub language count](https://img.shields.io/github/languages/count/rubypoddar/2048-game)
![GitHub top language](https://img.shields.io/github/languages/top/rubypoddar/2048-game)

