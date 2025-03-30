import pygame

class ChessGUI:
    """Main GUI handler for the chess application"""
    
    def __init__(self, width, height, dimension=8):
        """
        Initialize the GUI
        
        Args:
            width: Window width in pixels
            height: Window height in pixels
            dimension: Board dimension (default: 8x8)
        """
        self.width = width
        self.height = height
        self.dimension = dimension
        self.square_size = min(width, height) // dimension
        
        # Initialize pygame
        pygame.init()
        self.screen = pygame.display.set_mode((width, height))
        pygame.display.set_caption("Chess")
        self.font = pygame.font.SysFont("Arial", 32)
        self.small_font = pygame.font.SysFont("Arial", 16)
        self.clock = pygame.time.Clock()
    
    def get_clicked_position(self, mouse_pos):
        """
        Convert mouse position to board position
        
        Args:
            mouse_pos: Tuple (x, y) of mouse position
            
        Returns:
            Tuple (row, col) of board position
        """
        x, y = mouse_pos
        row = y // self.square_size
        col = x // self.square_size
        
        # Ensure coordinates are within the board
        if 0 <= row < self.dimension and 0 <= col < self.dimension:
            return row, col
        return None
    
    def draw_game_over_message(self, message):
        """
        Draw game over message on the screen
        
        Args:
            message: Result message to display
        """
        if message:
            # Create a semi-transparent overlay
            overlay = pygame.Surface((self.width, self.height), pygame.SRCALPHA)
            overlay.fill((0, 0, 0, 128))
            self.screen.blit(overlay, (0, 0))
            
            # Render message
            text_surface = self.font.render(message, True, (255, 255, 255))
            text_rect = text_surface.get_rect(center=(self.width//2, self.height//2))
            self.screen.blit(text_surface, text_rect)
            
            # Render restart instruction
            restart_text = self.small_font.render("Press 'R' to restart", True, (255, 255, 255))
            restart_rect = restart_text.get_rect(center=(self.width//2, self.height//2 + 40))
            self.screen.blit(restart_text, restart_rect)
    
    def update_display(self):
        """Update the display"""
        pygame.display.flip()
    
    def tick(self, fps):
        """Control the frame rate"""
        self.clock.tick(fps)
    
    def quit(self):
        """Clean up pygame resources"""
        pygame.quit()