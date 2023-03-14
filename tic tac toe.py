import pygame

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Set the width and height of the screen
WIDTH = 300
HEIGHT = 300

# Initialize Pygame
pygame.init()

# Set the size of the screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# Set the caption of the window
pygame.display.set_caption("Tic Tac Toe")

# Set the font for the text
font = pygame.font.Font(None, 50)

# Create a 2D array to represent the Tic Tac Toe board
board = [[' ', ' ', ' '],
         [' ', ' ', ' '],
         [' ', ' ', ' ']]

# Set the starting player
player = 'X'

# Function to draw the Tic Tac Toe board
def draw_board():
    # Clear the screen
    screen.fill(WHITE)
    
    # Draw the horizontal lines
    pygame.draw.line(screen, BLACK, (0, 100), (300, 100), 2)
    pygame.draw.line(screen, BLACK, (0, 200), (300, 200), 2)
    
    # Draw the vertical lines
    pygame.draw.line(screen, BLACK, (100, 0), (100, 300), 2)
    pygame.draw.line(screen, BLACK, (200, 0), (200, 300), 2)
    
    # Draw the X's and O's
    for row in range(3):
        for col in range(3):
            if board[row][col] == 'X':
                x = col * 100 + 50
                y = row * 100 + 50
                pygame.draw.line(screen, BLACK, (x - 25, y - 25), (x + 25, y + 25), 2)
                pygame.draw.line(screen, BLACK, (x + 25, y - 25), (x - 25, y + 25), 2)
            elif board[row][col] == 'O':
                x = col * 100 + 50
                y = row * 100 + 50
                pygame.draw.circle(screen, BLACK, (x, y), 25, 2)
    
    # Update the screen
    pygame.display.flip()

# Function to check if the game is over
def game_over():
    # Check for horizontal wins
    for row in range(3):
        if board[row][0] == board[row][1] == board[row][2] != ' ':
            return True
    
    # Check for vertical wins
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] != ' ':
            return True
    
    # Check for diagonal wins
    if board[0][0] == board[1][1] == board[2][2] != ' ':
        return True
    if board[0][2] == board[1][1] == board[2][0] != ' ':
        return True
    
    # Check for tie game
    for row in range(3):
        for col in range(3):
            if board[row][col] == ' ':
                return False
    return True

# Main game loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # Get the position of the mouse click
            pos = pygame.mouse.get_pos()
            
            # Calculate which square was clicked
            col = pos[0] // 100
            row = pos[1] // 100
            
            # If the square is empty, place the player's piece there
            if board[row][col] == ' ':
                board[row][col] = player
                
                # Switch players
                if player == 'X':
                    player = 'O'
                else:
                    player = 'X'
    
    # Draw the board
    draw_board()
    
    # Check for game over
    if game_over():
        # Create a message for the winner or tie game
        if player == 'X':
            message = "O wins!"
        elif player == 'O':
            message = "X wins!"
        else:
            message = "Tie game!"
        
        # Render the message
        text = font.render(message, True, BLACK)
        
        # Draw the message on the screen
        screen.blit(text, (WIDTH // 2 - text.get_width() // 2, HEIGHT // 2 - text.get_height() // 2))
        
        # Update the screen
        pygame.display.flip()
        
        # Wait for a few seconds before quitting
        pygame.time.wait(3000)
        running = False
    
# Quit Pygame
pygame.quit()
