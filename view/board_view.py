import pygame

class BoardView:
    """Handles rendering of the chess board"""
    
    # Color constants
    WHITE = (255, 255, 255)
    GRAY = (128, 128, 128)
    YELLOW = (204, 204, 0)
    BLUE = (50, 255, 255)
    BLACK = (0, 0, 0)
    
    def __init__(self, screen, square_size, dimension=8):
        """
        Initialize the board view
        
        Args:
            screen: Pygame screen to draw on
            square_size: Size of a square on the board in pixels
            dimension: Board dimension (default: 8x8)
        """
        self.screen = screen
        self.square_size = square_size
        self.dimension = dimension
    
    def draw_squares(self):
        """Draw the chess board squares"""
        colors = [self.WHITE, self.GRAY]
        for row in range(self.dimension):
            for col in range(self.dimension):
                color = colors[(row + col) % 2]
                pygame.draw.rect(
                    self.screen,
                    color,
                    pygame.Rect(
                        col * self.square_size,
                        row * self.square_size,
                        self.square_size,
                        self.square_size
                    )
                )
    
    def highlight_square(self, row, col, color=YELLOW, border_width=2):
        """
        Highlight a specific square
        
        Args:
            row: Board row (0-7)
            col: Board column (0-7)
            color: RGB color tuple for highlighting (default: yellow)
            border_width: Width of the highlight border
        """
        pygame.draw.rect(
            self.screen,
            color,
            pygame.Rect(
                col * self.square_size,
                row * self.square_size,
                self.square_size,
                self.square_size
            ),
            border_width
        )
    
    def highlight_selected_and_moves(self, selected_square, legal_moves):
        """
        Highlight the selected square and legal moves
        
        Args:
            selected_square: Tuple (row, col) of selected square or None
            legal_moves: List of tuples (row, col) for legal moves
        """
        if selected_square:
            row, col = selected_square
            self.highlight_square(row, col, self.YELLOW)
            
            for move_row, move_col in legal_moves:
                self.highlight_square(move_row, move_col, self.BLUE)