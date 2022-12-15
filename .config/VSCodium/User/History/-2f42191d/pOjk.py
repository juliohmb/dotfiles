# Import the necessary modules
import pygame
import random

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Define the shape of the tetrominoes
tetrominoes = [
    [[1, 1, 1],
     [0, 1, 0]],

    [[0, 2, 2],
     [2, 2, 0]],

    [[3, 3, 0],
     [0, 3, 3]],

    [[4, 0, 0],
     [4, 4, 4]],

    [[0, 0, 5],
     [5, 5, 5]],

    [[6, 6, 6, 6]],

    [[7, 7],
     [7, 7]]
]

# Define the dimensions of the grid
GRID_WIDTH = 10
GRID_HEIGHT = 20

# Define the dimensions of each tetromino block
BLOCK_SIZE = 20

# Define the dimensions of the window
WINDOW_WIDTH = GRID_WIDTH * BLOCK_SIZE
WINDOW_HEIGHT = GRID_HEIGHT * BLOCK_SIZE


def create_grid():
    # Create a grid of zeros to represent the playing field
    grid = [[0 for x in range(GRID_WIDTH)] for y in range(GRID_HEIGHT)]

    # Populate the grid with existing blocks
    for i in range(GRID_HEIGHT):
        for j in range(GRID_WIDTH):
            if grid[i][j] != 0:
                grid[i][j] = random.randint(1, len(tetrominoes))

    return grid


def draw_grid(surface, grid):
    # Draw each block in the grid
    for i in range(GRID_HEIGHT):
        for j in range(GRID_WIDTH):
            if grid[i][j] != 0:
                pygame.draw.rect(surface, WHITE, (j * BLOCK_SIZE, i * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE))


def rotate_tetromino(tetromino):
    # Rotate the tetromino by 90 degrees
    rotated_tetromino = []
    for i in range(len(tetromino)):
        rotated_tetromino.append([tetromino[i][j] for j in range(len(tetromino[i]) - 1, -1, -1)])

    return rotated_tetromino


def check_collision(grid, tetromino, x_offset=0, y_offset=0):
    # Check if the tetromino collides with any existing blocks in the grid
    for i in range(len(tetromino)):
        for j in range(len(tetromino[i])):
            if tetromino[i][j] != 0:
                if i + y_offset >= 0 and i + y_offset < len(grid) and j + x_offset >= 0 and j + x_offset < len(grid[i + y_offset]):
                    if grid[i + y_offset][j + x_offset] != 0:
                        return True

    return False



def remove_complete_rows(grid):
    # Remove any rows that are complete
    num_rows_removed = 0
    for i in range(GRID_HEIGHT):
        if 0 not in grid[i]:
            grid.pop(i)
            grid.insert(0, [0 for j in range(GRID_WIDTH)])
            num_rows_removed += 1

    return num_rows_removed


def main():
    # Initialize the game
    pygame.init()
    screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    pygame.display.set_caption("Tetris")
    clock = pygame.time.Clock()

    # Create the grid and the current tetromino
    grid = create_grid()
    current_tetromino = tetrominoes[random.randint(0, len(tetrominoes) - 1)]

    # Define some game parameters
    tetromino_x = GRID_WIDTH // 2
    tetromino_y = 0
    gravity = 1
    score = 0

    # Main game loop
    while True:
        # Check for user input
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    # Rotate the tetromino
                    rotated_tetromino = rotate_tetromino(current_tetromino)

                    # Check if the rotation is possible
                    if not check_collision(grid, rotated_tetromino, tetromino_x, tetromino_y):
                        current_tetromino = rotated_tetromino

                elif event.key == pygame.K_DOWN:
                    # Move the tetromino down
                    if not check_collision(grid, current_tetromino, tetromino_x, tetromino_y + 1):
                        tetromino_y += 1

                elif event.key == pygame.K_LEFT:
                    # Move the tetromino left
                    if not check_collision(grid, current_tetromino, tetromino_x - 1, tetromino_y):
                        tetromino_x -= 1

                elif event.key == pygame.K_RIGHT:
                    # Move the tetromino right
                    if not check_collision(grid, current_tetromino, tetromino_x + 1, tetromino_y):
                        tetromino_x += 1

        # Apply gravity to the tetromino
        if not check_collision(grid, current_tetromino, tetromino_x, tetromino_y + 1):
            tetromino_y += 1
        else:
            # The tetromino has landed, add it to the grid
            for i in range(len(current_tetromino)):
                for j in range(len(current_tetromino[i])):
                    if current_tetromino[i][j] != 0:
                        grid[i + tetromino_y][j + tetromino_x] = current_tetromino[i][j]

            # Generate a new tetromino
            current_tetromino = tetrominoes[random.randint(0, len(tetrominoes) - 1)]
            tetromino_x = GRID_WIDTH // 2
            tetromino_y = 0

            # Check if the game is over
            if check_collision(grid, current_tetromino, tetromino_x, tetromino_y):
                pygame.quit()
                sys.exit()

        # Remove any complete rows
        num_rows_removed = remove_complete_rows(grid)
        score += num_rows_removed

        # Draw the grid and the current tetromino
        screen.fill(BLACK)
        draw_grid(screen, grid)
        pygame.display.flip()
        clock.tick(10)

    pygame.quit()
    sys.exit()
main()
