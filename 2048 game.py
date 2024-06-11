import pygame
import random

# Constants
WIDTH = 400
HEIGHT = 500  # Increased to accommodate the score display and new game button
GRID_SIZE = 4
TILE_SIZE = WIDTH // GRID_SIZE
BACKGROUND_COLOR = (187, 173, 160)
GRID_COLOR = (205, 193, 180)
FONT_COLOR = (255, 255, 255)
FONT_SIZE = 36

# Tile colors
TILE_COLORS = {
    2: (238, 228, 218),
    4: (237, 224, 200),
    8: (242, 177, 121),
    16: (245, 149, 99),
    32: (246, 124, 95),
    64: (246, 94, 59),
    128: (237, 207, 114),
    256: (237, 204, 97),
    512: (237, 200, 80),
    1024: (237, 197, 63),
    2048: (237, 194, 46)
}

# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("2048 Game")
clock = pygame.time.Clock()

# Function to display "New Game" button
def display_new_game_button():
    pygame.draw.rect(screen, (119, 110, 101), (10, HEIGHT - 80, 120, 40))
    font = pygame.font.Font(None, 24)
    new_game_text = font.render("New Game", True, FONT_COLOR)
    screen.blit(new_game_text, (20, HEIGHT - 70))

# Function to handle "New Game" button click
def handle_new_game_click(mouse_pos):
    if 10 <= mouse_pos[0] <= 130 and HEIGHT - 80 <= mouse_pos[1] <= HEIGHT - 40:
        reset_game()

# Function to reset the game
def reset_game():
    global grid, score, high_score
    grid = [[0] * GRID_SIZE for _ in range(GRID_SIZE)]
    generate_tile()
    generate_tile()
    score = 0

# Function to draw the grid
def draw_grid():
    for i in range(GRID_SIZE):
        for j in range(GRID_SIZE):
            pygame.draw.rect(screen, GRID_COLOR, (i * TILE_SIZE, j * TILE_SIZE + 50, TILE_SIZE, TILE_SIZE), 0)
            value = grid[j][i]
            if value != 0:
                draw_tile(i, j, value)

# Function to draw a tile
def draw_tile(x, y, value):
    font = pygame.font.Font(None, FONT_SIZE)
    text = font.render(str(value), True, FONT_COLOR)
    text_rect = text.get_rect(center=(x * TILE_SIZE + TILE_SIZE / 2, y * TILE_SIZE + TILE_SIZE / 2 + 50))
    pygame.draw.rect(screen, TILE_COLORS.get(value, (0, 0, 0)), (x * TILE_SIZE, y * TILE_SIZE + 50, TILE_SIZE, TILE_SIZE), 0)
    screen.blit(text, text_rect)

# Function to generate a new tile
def generate_tile():
    empty_cells = [(i, j) for i in range(GRID_SIZE) for j in range(GRID_SIZE) if grid[i][j] == 0]
    if empty_cells:
        x, y = random.choice(empty_cells)
        grid[x][y] = 2 if random.random() < 0.9 else 4

# Function to move tiles left
def move_left():
    global grid
    for row in grid:
        row[:] = merge(row)

# Function to move tiles right
def move_right():
    global grid
    for row in grid:
        row[:] = merge(row[::-1])[::-1]

# Function to move tiles up
def move_up():
    global grid
    grid = [list(row) for row in zip(*grid)]  # Transpose the grid
    for row in grid:
        row[:] = merge(row)  # Merge tiles in each row
    grid = [list(row) for row in zip(*grid)]  # Transpose the grid back to its original orientation

# Function to move tiles down
def move_down():
    global grid
    grid = [list(row) for row in zip(*grid)]  # Transpose the grid
    for row in grid:
        row[:] = merge(row[::-1])[::-1]  # Merge tiles in each row, then reverse back to original order
    grid = [list(row) for row in zip(*grid)]  # Transpose the grid back to its original orientation

# Function to merge tiles in a row
def merge(row):
    new_row = [i for i in row if i != 0]  # Remove zeros from the row
    for i in range(len(new_row) - 1):
        if new_row[i] == new_row[i + 1]:  # If adjacent tiles have the same value
            new_row[i] *= 2  # Merge them by doubling the value of the first tile
            new_row[i + 1] = 0  # Set the value of the second tile to zero
    new_row = [i for i in new_row if i != 0]  # Remove zeros again
    return new_row + [0] * (GRID_SIZE - len(new_row))  # Pad with zeros to maintain row length

# Main game loop
running = True
grid = [[0] * GRID_SIZE for _ in range(GRID_SIZE)]
generate_tile()
generate_tile()
score = 0
high_score = 0

while running:
    screen.fill(BACKGROUND_COLOR)
    
    # Display "2048" at the top
    font = pygame.font.Font(None, 72)
    text = font.render("2048", True, FONT_COLOR)
    text_rect = text.get_rect(center=(WIDTH // 2, 30))
    screen.blit(text, text_rect)
    
    # Draw the grid and new game button
    draw_grid()
    display_new_game_button()
    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            handle_new_game_click(pygame.mouse.get_pos())
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                move_left()
                generate_tile()
            elif event.key == pygame.K_RIGHT:
                move_right()
                generate_tile()
            elif event.key == pygame.K_UP:
                move_up()
                generate_tile()
            elif event.key == pygame.K_DOWN:
                move_down()
                generate_tile()

pygame.quit()
