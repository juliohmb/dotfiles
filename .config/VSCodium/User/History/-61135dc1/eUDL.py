import pygame

# initialize pygame
pygame.init()

# create screen
SCREEN_WIDTH = 300
SCREEN_HEIGHT = 500
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# create a clock to control game speed
clock = pygame.time.Clock()

# create a font for rendering text on the screen
font = pygame.font.SysFont("Arial", 20)

# create colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# tetris pieces
tetris_pieces = [
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

# current piece and its position on the screen
current_piece = tetris_pieces[0]
current_position = (5, 0)

# speed of tetris pieces in pixels per second
SPEED = 20

# scale factor for tetris pieces
SCALE = 30

# game loop
running = True
while running:
    # handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # handle arrow keys to move the piece
        if event.type == pygame.KEYDOWN or event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                current_position = (current_position[0] - 1, current_position[1])
            elif event.key == pygame.K_RIGHT:
                current_position = (current_position[0] + 1, current_position[1])
            elif event.key == pygame.K_DOWN:
                current_position = (current_position[0], current_position[1] + 1)

            # handle space key to rotate the piece
            elif event.key == pygame.K_SPACE:
                current_piece = list(zip(*current_piece[::-1]))

    # calculate the time elapsed since the last frame
    time_elapsed = clock.tick(60) / 1000.0

    # calculate the distance the tetris piece should move in each frame
    distance = SPEED * time_elapsed

    # update the position of the tetris piece
    current_position = (current_position[0], current_position[1] + distance)

    # check if the tetris piece has reached the bottom of the screen or another piece
    if current_position[1] + len(current_piece) >= SCREEN_HEIGHT or \
        any(screen.get_at((current_position[0] + int(x), current_position[1] + int(y))) != BLACK
            for y, row in enumerate(current_piece)
            for x, cell in enumerate(row) if cell != 0):

        # move the piece back up
        current_position = (current_position[0], current_position[1] - distance)

        # add the current piece to the screen
        for y, row in enumerate(current_piece):
            for x, cell in enumerate(row):
                if cell != 0:
                    screen.set_at((current_position[0] + x, current_position[1] + y), cell)

        # generate a new piece
        current_piece = tetris_pieces[0]
        current_position = (5, 0)

    # clear the screen
    screen.fill(BLACK)

    # draw the current piece
    for y, row in enumerate(current_piece):
        for x, cell in enumerate(row):
            if cell != 0:
                rect = pygame.Rect(current_position[0] + x * SCALE, current_position[1] + y * SCALE, SCALE, SCALE)
                pygame.draw.rect(screen, WHITE, rect)

    # draw the score
    score_text = font.render("Score: 0", True, WHITE)
    screen.blit(score_text, (5, 5))

    # update the screen
    pygame.display.flip()

    # control the game speed
    clock.tick(60)

# quit pygame
pygame.quit()
