import pygame
import os
import chess

class PieceView:
    """Handles rendering of chess pieces"""
    
    def __init__(self, square_size):
        """
        Initialize the piece view
        
        Args:
            square_size: Size of a square on the board in pixels
        """
        self.square_size = square_size
        self.images = {}
        self.load_images()
    
    def load_images(self):
        """Load images for all chess pieces"""
        piece_symbols = ['wp', 'wR', 'wN', 'wB', 'wK', 'wQ', 'bp', 'bR', 'bN', 'bB', 'bK', 'bQ']
        
        for symbol in piece_symbols:
            try:
                image_path = os.path.join("images", f"{symbol}.png")
                self.images[symbol] = pygame.transform.scale(
                    pygame.image.load(image_path),
                    (self.square_size, self.square_size)
                )
            except pygame.error as e:
                print(f"Could not load image for {symbol}: {e}")
                # Create a placeholder if image is missing
                surface = pygame.Surface((self.square_size, self.square_size))
                surface.fill((200, 200, 200))
                pygame.draw.rect(surface, (0, 0, 0), pygame.Rect(0, 0, self.square_size, self.square_size), 2)
                self.images[symbol] = surface
    
    def draw_piece(self, screen, piece, row, col):
        """
        Draw a piece on the screen
        
        Args:
            screen: Pygame screen to draw on
            piece: Piece object to draw
            row: Board row (0-7)
            col: Board column (0-7)
        """
        if piece:
            screen.blit(
                self.images[piece.symbol],
                pygame.Rect(
                    col * self.square_size,
                    row * self.square_size,
                    self.square_size,
                    self.square_size
                )
            )