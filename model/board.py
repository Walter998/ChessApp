import chess
from model.piece import Piece

class Board:
    """Represents the chess board and its state"""
    
    def __init__(self):
        """Initialize a new chess board"""
        self.chess_board = chess.Board()
        
    def reset(self):
        """Reset the board to the starting position"""
        self.chess_board = chess.Board()
        
    def get_piece_at(self, row, col):
        """
        Get the piece at a specific position
        
        Args:
            row: Board row (0-7)
            col: Board column (0-7)
            
        Returns:
            Piece object or None if empty
        """
        square = chess.square(col, 7 - row)
        chess_piece = self.chess_board.piece_at(square)
        return Piece(chess_piece) if chess_piece else None
    
    def get_legal_moves_from(self, row, col):
        """
        Get all legal moves from the given position
        
        Args:
            row: Board row (0-7)
            col: Board column (0-7)
            
        Returns:
            List of tuples (row, col) for legal destination squares
        """
        square = chess.square(col, 7 - row)
        legal_moves = []
        
        for move in self.chess_board.legal_moves:
            if move.from_square == square:
                dest_row = 7 - chess.square_rank(move.to_square)
                dest_col = chess.square_file(move.to_square)
                legal_moves.append((dest_row, dest_col))
                
        return legal_moves
    
    def make_move(self, start_pos, end_pos, promotion_piece=chess.QUEEN):
        """
        Make a move on the board
        
        Args:
            start_pos: Tuple (row, col) of starting position
            end_pos: Tuple (row, col) of ending position
            promotion_piece: Piece type for promotion (default: Queen)
            
        Returns:
            True if move was made, False if invalid
        """
        start_row, start_col = start_pos
        end_row, end_col = end_pos
        
        start_square = chess.square(start_col, 7 - start_row)
        end_square = chess.square(end_col, 7 - end_row)
        
        # Check if this is a promotion move
        piece = self.chess_board.piece_at(start_square)
        move = None
        
        if piece and piece.piece_type == chess.PAWN:
            if (end_row == 0 and piece.color == chess.WHITE) or \
               (end_row == 7 and piece.color == chess.BLACK):
                move = chess.Move(start_square, end_square, promotion=promotion_piece)
            else:
                move = chess.Move(start_square, end_square)
        else:
            move = chess.Move(start_square, end_square)
        
        # Make move if legal
        if move in self.chess_board.legal_moves:
            self.chess_board.push(move)
            return True
        return False
    
    def is_checkmate(self):
        """Check if the current position is checkmate"""
        return self.chess_board.is_checkmate()
    
    def is_stalemate(self):
        """Check if the current position is stalemate"""
        return self.chess_board.is_stalemate()
    
    def is_check(self):
        """Check if the current position is check"""
        return self.chess_board.is_check()
    
    def is_game_over(self):
        """Check if the game is over"""
        return self.chess_board.is_game_over()
    
    def get_current_player(self):
        """Get the current player (True for white, False for black)"""
        return self.chess_board.turn
    
    def get_move_history(self):
        """Get the history of moves in standard algebraic notation"""
        return [self.chess_board.san(move) for move in self.chess_board.move_stack]