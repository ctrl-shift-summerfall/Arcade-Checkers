# Internal scripts and modules:
from app.settings import (GAME_SCREEN_WIDTH, GAME_SCREEN_HEIGHT, GAME_SCREEN_TITLE,
                          GAME_SCREEN_FULLSCREEN, GAME_SCREEN_RESIZABLE, GAME_SCREEN_UPDATE_RATE, GAME_SCREEN_ANTIALIASING)

from app.board import Board

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
        arcade.run()
    
    def on_draw(self):
        self.board_controller.render()
        return super().on_draw()
    
    def on_update(self, delta_time: float):
        return super().on_update(delta_time)
