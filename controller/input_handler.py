import pygame

class InputHandler:
    """Handles user input events"""
    
    def __init__(self, game_controller):
        """
        Initialize the input handler
        
        Args:
            game_controller: GameController instance to process inputs
        """
        self.game_controller = game_controller
    
    def handle_events(self):
        """
        Process all pygame events
        
        Returns:
            False if the application should quit, True otherwise
        """
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            
            # Mouse input
            elif event.type == pygame.MOUSEBUTTONDOWN:
                self._handle_mouse_click(event.pos)
            
            # Keyboard input
            elif event.type == pygame.KEYDOWN:
                self._handle_key_press(event.key)
        
        return True
    
    def _handle_mouse_click(self, pos):
        """
        Handle mouse click events
        
        Args:
            pos: Tuple (x, y) of mouse position
        """
        self.game_controller.handle_square_click(pos)
    
    def _handle_key_press(self, key):
        """
        Handle keyboard press events
        
        Args:
            key: Pygame key constant
        """
        if key == pygame.K_r:  # Reset game
            self.game_controller.reset_game()
        # Add more keyboard controls as needed