import sys
import pygame
from model.board import Board
from model.game_state import GameState
from view.piece_view import PieceView
from view.board_view import BoardView
from view.gui import ChessGUI
from controller.game_controller import GameController
from controller.input_handler import InputHandler


def main():
    # Configuration
    WIDTH, HEIGHT = 512, 512
    DIMENSION = 8
    MAX_FPS = 15
    
    # Initialize components
    gui = ChessGUI(WIDTH, HEIGHT, DIMENSION)
    board_view = BoardView(gui.screen, gui.square_size, DIMENSION)
    piece_view = PieceView(gui.square_size)
    
    # Initialize controller
    game_controller = GameController(board_view, piece_view, gui)
    input_handler = InputHandler(game_controller)
    
    # Game loop
    running = True
    while running:
        # Handle events
        running = input_handler.handle_events()
        
        # Update display
        game_controller.update_display()
        
        # Control frame rate
        gui.tick(MAX_FPS)
    
    # Clean up
    gui.quit()
    sys.exit()

if __name__ == "__main__":
    main()