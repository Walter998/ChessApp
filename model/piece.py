import chess

class Piece:
    """Represents a chess piece and its properties"""
    
    def __init__(self, chess_piece):
        """
        Initialize a piece
        
        Args:
            chess_piece: A python-chess Piece object
        """
        self.chess_piece = chess_piece
        
    @property
    def color(self):
        """Get the color of the piece (True for white, False for black)"""
        return self.chess_piece.color
    
    @property
    def piece_type(self):
        """Get the type of the piece (PAWN, KNIGHT, etc.)"""
        return self.chess_piece.piece_type
    
    @property
    def symbol(self):
        """Get the symbol for this piece for image loading"""
        color_char = 'w' if self.color == chess.WHITE else 'b'
        type_char = {
            chess.PAWN: 'p',
            chess.ROOK: 'R',
            chess.KNIGHT: 'N',
            chess.BISHOP: 'B',
            chess.QUEEN: 'Q',
            chess.KING: 'K'
        }[self.piece_type]
        
        return color_char + type_char