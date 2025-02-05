import sys
import pygame

# Initialize Pygame
pygame.init()

# Game configurations
WIDTH, HEIGHT = 500, 500
LINE_WIDTH = 5
BOARD_ROWS, BOARD_COLS = 3, 3
SQUARE_SIZE = WIDTH // BOARD_COLS
CIRCLE_RADIUS = SQUARE_SIZE // 3
CIRCLE_WIDTH = 5
CROSS_WIDTH = 5
SPACE = 25

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (200, 0, 0)
GREEN = (0, 255, 0)

window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tic Tac Toe")
window.fill(WHITE)

#Font object
font = pygame.font.Font(None, 100)

current_player = "X"
running = True

#Board
grid = [[None, None, None],
         [None, None, None],
         [None, None, None]]

# Draw lines of the board
for i in range(1, BOARD_ROWS):
    pygame.draw.line(window, BLACK, (0, i * SQUARE_SIZE), (WIDTH, i * SQUARE_SIZE), LINE_WIDTH) # Horizontal lines
    pygame.draw.line(window, BLACK, (i * SQUARE_SIZE, 0), (i * SQUARE_SIZE, HEIGHT), LINE_WIDTH) # Vertical lines
    
def draw_symbol(row, col, player):
    if player == "X":
        pygame.draw.line(window, BLACK, (col * SQUARE_SIZE + SPACE, row * SQUARE_SIZE + SQUARE_SIZE - SPACE), 
                         (col * SQUARE_SIZE + SQUARE_SIZE - SPACE, row * SQUARE_SIZE + SPACE), CROSS_WIDTH)
        pygame.draw.line(window, BLACK, (col * SQUARE_SIZE + SPACE, row * SQUARE_SIZE + SPACE), 
                         (col * SQUARE_SIZE + SQUARE_SIZE - SPACE, row * SQUARE_SIZE + SQUARE_SIZE - SPACE), CROSS_WIDTH)
    else:
        pygame.draw.circle(window, RED, (col * SQUARE_SIZE + SQUARE_SIZE // 2, row * SQUARE_SIZE + SQUARE_SIZE // 2), CIRCLE_RADIUS, CIRCLE_WIDTH)

def check_winner(player):
    # Check rows, columns and diagonals
    for row in range(BOARD_ROWS):
        if grid[row][0] == player and grid[row][1] == player and grid[row][2] == player:
            return True
    for col in range(BOARD_COLS):
        if grid[0][col] == player and grid[1][col] == player and grid[2][col] == player:
            return True
    if grid[0][0] == player and grid[1][1] == player and grid[2][2] == player:
        return True
    if grid[0][2] == player and grid[1][1] == player and grid[2][0] == player:
        return True
    return False

def board_is_full():
    for row in range(BOARD_ROWS):
        for col in range(BOARD_COLS):
            if grid[row][col] == None:
                return False
    return True

def restart_game():
    window.fill(WHITE)
    for i in range(1, BOARD_ROWS):
        pygame.draw.line(window, BLACK, (0, i * SQUARE_SIZE), (WIDTH, i * SQUARE_SIZE), LINE_WIDTH) # Horizontal lines
        pygame.draw.line(window, BLACK, (i * SQUARE_SIZE, 0), (i * SQUARE_SIZE, HEIGHT), LINE_WIDTH) # Vertical lines
    for row in range(BOARD_ROWS):
        for col in range(BOARD_COLS):
            grid[row][col] = None
    
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1: #Left click
            mouseX = event.pos[0]
            mouseY = event.pos[1]
            
            #print(f"Mouse clicked at ({mouseX}, {mouseY})")
            clicked_row = mouseY // SQUARE_SIZE
            clicked_col = mouseX // SQUARE_SIZE
            #print(f"Row: {clicked_row}, Col: {clicked_col}")
            
            if grid[clicked_row][clicked_col] == None:
                grid[clicked_row][clicked_col] = current_player
                draw_symbol(clicked_row, clicked_col, current_player)
                if check_winner(current_player):
                    #print(f"{current_player} wins!")
                    if current_player == "X":
                        text = font.render("X wins!", True, GREEN, BLACK)
                        text_rectangle = text.get_rect()
                        text_rectangle.center = (WIDTH // 2, HEIGHT // 2)
                        window.blit(text, text_rectangle)
                    else:
                        text = font.render("O wins!", True, GREEN, BLACK)
                        text_rectangle = text.get_rect()
                        text_rectangle.center = (WIDTH // 2, HEIGHT // 2)
                        window.blit(text, text_rectangle)
                    pygame.display.update()
                    pygame.time.delay(3000)
                    restart_game()
                elif board_is_full():
                    text = font.render("It's a tie!", True, GREEN, BLACK)
                    text_rectangle = text.get_rect()
                    text_rectangle.center = (WIDTH // 2, HEIGHT // 2)
                    window.blit(text, text_rectangle)
                    pygame.display.update()
                    pygame.time.delay(3000)
                    restart_game()
                
                current_player = "X" if current_player == "O" else "O"

    pygame.display.update()
    
pygame.quit()
sys.exit()