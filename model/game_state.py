class GameState:
    """Represents the state of the chess game"""
    
    def __init__(self):
        """Initialize a new game state"""
        self.active_player_clicks = []
        self.selected_square = None
        self.game_over = False
        self.result_message = ""
        
    def reset(self):
        """Reset the game state"""
        self.active_player_clicks = []
        self.selected_square = None
        self.game_over = False
        self.result_message = ""
    
    def select_square(self, row, col):
        """
        Select a square on the board
        
        Args:
            row: Board row (0-7)
            col: Board column (0-7)
            
        Returns:
            Tuple containing:
            - Whether the selection was just completed (True/False)
            - Start position (row, col) or None
            - End position (row, col) or None
        """
        pos = (row, col)
        
        # If clicking on the same square twice, deselect it
        if self.selected_square == pos:
            self.selected_square = None
            self.active_player_clicks = []
            return False, None, None
        
        # If no square is selected yet or changing selection
        if not self.active_player_clicks or len(self.active_player_clicks) == 2:
            self.active_player_clicks = [pos]
            self.selected_square = pos
            return False, pos, None
        
        # If a square is already selected, this is the target square
        self.active_player_clicks.append(pos)
        start_pos = self.active_player_clicks[0]
        end_pos = self.active_player_clicks[1]
        
        # Reset for next move
        selection_complete = True
        self.selected_square = None
        self.active_player_clicks = []
        
        return selection_complete, start_pos, end_pos
    
    def set_game_over(self, is_over, message=""):
        """
        Set game over state with optional message
        
        Args:
            is_over: Boolean indicating if game is over
            message: Result message to display
        """
        self.game_over = is_over
        self.result_message = message
    
    def get_result_message(self):
        """Get the game result message"""
        return self.result_message