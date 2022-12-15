import pygame

# initialize pygame
pygame.init()

# create screen
screen = pygame.display.set_mode((300, 500))

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

# game loop
running = True
while running:
    # handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # handle arrow keys to move the piece
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                current_position = (current_position[0] - 1, current_position[1])
            elif event.key == pygame.K_RIGHT:
                current_position = (current_position[0] + 1, current_position[1])
            elif event.key == pygame.K_DOWN:
                current_position = (current_position[0], current_position[1] + 1)

            # handle space key to rotate the piece
            elif event.key == pygame.K_SPACE:
                current_piece = list(zip(*current_piece[::-1]))

    # draw the screen
    screen.fill(BLACK)

    # draw the current piece
    for y, row in enumerate(current_piece):
        for x, cell in enumerate(row):
            if cell != 0:
                rect = pygame.Rect(current_position[0] + x, current_position[1] + y, 1, 1)
                pygame.draw.rect(screen, WHITE, rect)

    # draw the score
    score_text = font.render("Score: 0", True, WHITE)
    screen.blit(score_text, (5, 5))

    # update the screen
    pygame.display.flip()

    # control the game speed
    clock.tick(10)

# quit pygame
pygame.quit()
