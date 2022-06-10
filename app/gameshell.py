# Internal settings and variables:
from app.settings import (GAME_SCREEN_WIDTH, GAME_SCREEN_HEIGHT, GAME_SCREEN_TITLE,
                          GAME_SCREEN_FULLSCREEN, GAME_SCREEN_RESIZABLE, GAME_SCREEN_UPDATE_RATE, GAME_SCREEN_ANTIALIASING)

# Internal scripts:
from app.scripts import (convert_coordinates_to_grid_position,              # [coord_x, coord_y] --> [row, column]
                         convert_grid_position_to_coordinates,              # [row, column] --> [coord_x, coord_y]
                         convert_grid_position_to_alphanumeric_position,    # [row, column] --> "A1"
                         convert_alphanumeric_position_to_grid_position)    # "A1" --> [row, column]

# Controllers:
from app.board import Board         # Board controller
from app.checker import Checker     # Checker class object

# External libraries:
import arcade


class Gameshell(arcade.Window):

    def __init__(self, 
                 width: int = GAME_SCREEN_WIDTH, 
                 height: int = GAME_SCREEN_HEIGHT, 
                 title: str = GAME_SCREEN_TITLE, 
                 fullscreen: bool = GAME_SCREEN_FULLSCREEN, 
                 resizable: bool = GAME_SCREEN_RESIZABLE, 
                 update_rate: float = GAME_SCREEN_UPDATE_RATE, 
                 antialiasing: bool = GAME_SCREEN_ANTIALIASING):
        
        super().__init__(width, height, title, fullscreen, resizable, update_rate, antialiasing)
        self.board_controller = Board()
        self.board_controller.grid_create_new()
        self.board_controller.grid_populate()
        arcade.run()
    
    def on_draw(self):

        def render_board_surface():
            self.board_controller.render_board_surface()

        def render_checkers():
            for row in self.board_controller.grid:
                for column in self.board_controller.grid[row]:
                    if self.board_controller.grid[row][column] is not None:
                        checker_object: Checker = self.board_controller.grid[row][column]
                        checker_object.render()
                        
        render_board_surface()
        render_checkers()
        return super().on_draw()
    
    def on_update(self, delta_time: float):
        return super().on_update(delta_time)
