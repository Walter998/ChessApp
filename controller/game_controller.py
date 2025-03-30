import chess
from model.board import Board
from model.game_state import GameState

class GameController:
    """Main controller for the chess game"""
    
    def __init__(self, board_view, piece_view, gui):
        """
        Initialize the game controller
        
        Args:
            board_view: BoardView instance
            piece_view: PieceView instance
            gui: ChessGUI instance
        """
        self.board = Board()
        self.game_state = GameState()
        self.board_view = board_view
        self.piece_view = piece_view
        self.gui = gui
    
    def reset_game(self):
        """Reset the game to initial state"""
        self.board.reset()
        self.game_state.reset()
    
    def handle_square_click(self, mouse_pos):
        """
        Handle click on a board square
        
        Args:
            mouse_pos: Tuple (x, y) of mouse position
        """
        if self.game_state.game_over:
            return
        
        board_pos = self.gui.get_clicked_position(mouse_pos)
        if not board_pos:
            return
        
        row, col = board_pos
        move_complete, start_pos, end_pos = self.game_state.select_square(row, col)
        
        if move_complete and start_pos and end_pos:
            # Attempt to make a move
            move_made = self.board.make_move(start_pos, end_pos)
            
            if move_made:
                # Check for game over conditions
                if self.board.is_game_over():
                    self._handle_game_over()
    
    def _handle_game_over(self):
        """Handle game over conditions"""
        message = ""
        
        if self.board.is_checkmate():
            winner = "Black" if self.board.get_current_player() else "White"
            message = f"Checkmate! {winner} wins!"
        elif self.board.is_stalemate():
            message = "Stalemate! Draw!"
        else:
            # Other draw conditions
            message = "Game over! Draw!"
        
        self.game_state.set_game_over(True, message)
    
    def update_display(self):
        """Update the game display"""
        # Draw the board
        self.board_view.draw_squares()
        
        # Get legal moves from selected square
        legal_moves = []
        if self.game_state.selected_square:
            row, col = self.game_state.selected_square
            legal_moves = self.board.get_legal_moves_from(row, col)
        
        # Highlight selected square and legal moves
        self.board_view.highlight_selected_and_moves(
            self.game_state.selected_square, 
            legal_moves
        )
        
        # Draw pieces
        for row in range(8):
            for col in range(8):
                piece = self.board.get_piece_at(row, col)
                if piece:
                    self.piece_view.draw_piece(self.gui.screen, piece, row, col)
        
        # Draw game over message if applicable
        self.gui.draw_game_over_message(self.game_state.get_result_message())
        
        # Update display
        self.gui.update_display()