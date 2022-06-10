# Internal settings and variables:
from app.settings import (BOARD_TILE_SIDE_SIZE_PX, BOARD_HEIGHT, BOARD_WIDTH,
                          BOARD_CENTER_POSITION_X, BOARD_CENTER_POSITION_Y,
                          BOARD_MARGIN_INNER_WIDTH, BOARD_MARGIN_INNER_COLOR,
                          BOARD_MARGIN_OUTER_WIDTH, BOARD_MARGIN_OUTER_COLOR,
                          BOARD_TILE_COLOR_BLACK, BOARD_TILE_COLOR_WHITE,
                          GRID_ALPHABETIC_INDEX_STRING, GRID_NUMERIC_INDEX_STRING,
                          GRID_ROW_COUNT, GRID_COLUMN_COUNT)
                          
from app.variables import (VAR_BOARD_TILE_COLOR_BLACK, VAR_BOARD_TILE_COLOR_WHITE, 
                           VAR_CHECKER_COLOR_BLACK, VAR_CHECKER_COLOR_WHITE, VAR_CHECKER_COLOR_NOT_SET, VAR_CHECKER_TYPE_ORDINARY, 
                           VAR_SESSION_RENDER_MODE_OPENGL, VAR_SESSION_RENDER_MODE_TEXTURE)

# Internal modules:
from app.checker import Checker     # Checker class object

# External libraries:
import arcade


class Board:
    
    def __init__(self):
        self.grid = {}

    def grid_create_new(self):
        new_grid = {}
        for row in range(GRID_ROW_COUNT):
            new_grid[row] = {}
            for column in range(GRID_COLUMN_COUNT):
                new_grid[row][column] = None
        self.grid = new_grid
    
    def grid_clean(self):
        for row in self.grid:
            for column in self.grid[row]:
                self.grid[row][column] = None
    
    def grid_delete(self):
        self.grid = {}

    def grid_reset(self):
        self.grid_delete()
        self.grid_create_new()

    def grid_populate(self):
        for row in self.grid:
            for column in self.grid[row]:
                if row in (0, 1, 2, 5, 6, 7):
                    spawn_color = str(VAR_CHECKER_COLOR_WHITE if row in (0, 1, 2) else
                                      VAR_CHECKER_COLOR_BLACK if row in (5, 6, 7) else
                                      VAR_CHECKER_COLOR_NOT_SET)
                    if row % 2 != 0 and column % 2 != 0 or row % 2 == 0 and column % 2 == 0:
                        spawn_type = VAR_CHECKER_TYPE_ORDINARY
                        spawn_position = [row, column]
                        new_checker = Checker(set_color=spawn_color,
                                              set_type=spawn_type,
                                              set_position=spawn_position)
                        self.grid[row][column] = new_checker

    def render_board_surface(self):

        import app.session as SESSION
        if SESSION.SESSION_RENDER_MODE == VAR_SESSION_RENDER_MODE_OPENGL:

            # Rendering outer border margins:
            arcade.draw_rectangle_filled(
                center_x=BOARD_CENTER_POSITION_X,
                center_y=BOARD_CENTER_POSITION_Y,
                width=BOARD_WIDTH,
                height=BOARD_HEIGHT,
                color=BOARD_MARGIN_OUTER_COLOR,
                tilt_angle=0)
            arcade.draw_rectangle_filled(
                center_x=BOARD_CENTER_POSITION_X,
                center_y=BOARD_CENTER_POSITION_Y,
                width=int(BOARD_WIDTH - BOARD_MARGIN_OUTER_WIDTH * 2),
                height=int(BOARD_HEIGHT - BOARD_MARGIN_OUTER_WIDTH * 2),
                color=BOARD_MARGIN_INNER_COLOR,
                tilt_angle=0)
            
            # Rendering tiles:
            tile_color_var = VAR_BOARD_TILE_COLOR_BLACK
            tile_center_coordinate_x = int(BOARD_MARGIN_OUTER_WIDTH + BOARD_MARGIN_INNER_WIDTH + BOARD_TILE_SIDE_SIZE_PX / 2)
            tile_center_coordinate_y = int(BOARD_MARGIN_OUTER_WIDTH + BOARD_MARGIN_INNER_WIDTH + BOARD_TILE_SIDE_SIZE_PX / 2)
            for row in range(GRID_ROW_COUNT):
                for column in range(GRID_COLUMN_COUNT):
                    arcade.draw_rectangle_filled(
                        center_x=tile_center_coordinate_x,
                        center_y=tile_center_coordinate_y,
                        width=BOARD_TILE_SIDE_SIZE_PX,
                        height=BOARD_TILE_SIDE_SIZE_PX,
                        color=BOARD_TILE_COLOR_BLACK if tile_color_var == VAR_BOARD_TILE_COLOR_BLACK else BOARD_TILE_COLOR_WHITE,
                        tilt_angle=0)
                    if tile_color_var == VAR_BOARD_TILE_COLOR_BLACK:
                        tile_color_var = VAR_BOARD_TILE_COLOR_WHITE
                    else:
                        tile_color_var = VAR_BOARD_TILE_COLOR_BLACK
                    tile_center_coordinate_x += BOARD_TILE_SIDE_SIZE_PX
                tile_center_coordinate_x = int(BOARD_MARGIN_OUTER_WIDTH + BOARD_MARGIN_INNER_WIDTH + BOARD_TILE_SIDE_SIZE_PX / 2)
                tile_center_coordinate_y += BOARD_TILE_SIDE_SIZE_PX
                if tile_color_var == VAR_BOARD_TILE_COLOR_BLACK:
                    tile_color_var = VAR_BOARD_TILE_COLOR_WHITE
                else:
                    tile_color_var = VAR_BOARD_TILE_COLOR_BLACK
            
            # Rendering alphanumeric index:
            for text_rotation_angle in (0, 180):

                # Rendering alphabetic index:
                letter_coordinate_x = int(BOARD_MARGIN_INNER_WIDTH + BOARD_MARGIN_OUTER_WIDTH + BOARD_TILE_SIDE_SIZE_PX / 2)
                letter_coordinate_y = int(BOARD_MARGIN_OUTER_WIDTH / 2)
                if text_rotation_angle == 180:
                    letter_coordinate_y = int(BOARD_HEIGHT - BOARD_MARGIN_OUTER_WIDTH / 2)
                for letter in GRID_ALPHABETIC_INDEX_STRING:
                    arcade.draw_text(
                        text=letter,
                        start_x=letter_coordinate_x,
                        start_y=letter_coordinate_y,
                        color=BOARD_TILE_COLOR_WHITE,
                        font_size=10,
                        font_name='tahoma',
                        anchor_x='center',
                        anchor_y='center',
                        rotation=text_rotation_angle)
                    letter_coordinate_x += BOARD_TILE_SIDE_SIZE_PX
                
                # Rendering numeric index:
                number_coordinate_x = int(BOARD_MARGIN_OUTER_WIDTH / 2)
                number_coordinate_y = int(BOARD_MARGIN_INNER_WIDTH + BOARD_MARGIN_OUTER_WIDTH + BOARD_TILE_SIDE_SIZE_PX / 2)
                if text_rotation_angle == 180:
                    number_coordinate_x = int(BOARD_WIDTH - BOARD_MARGIN_OUTER_WIDTH / 2)
                for number in GRID_NUMERIC_INDEX_STRING:
                    arcade.draw_text(
                        text=number,
                        start_x=number_coordinate_x,
                        start_y=number_coordinate_y,
                        color=BOARD_TILE_COLOR_WHITE,
                        font_size=10,
                        font_name='tahoma',
                        anchor_x='center',
                        anchor_y='center',
                        rotation=text_rotation_angle)
                    number_coordinate_y += BOARD_TILE_SIDE_SIZE_PX

        elif SESSION.SESSION_RENDER_MODE == VAR_SESSION_RENDER_MODE_TEXTURE:
            pass

    def render_checkers(self):
        for row in self.grid:
            for column in self.grid[row]:
                checker_object: Checker = self.grid[row][column]
                if checker_object is not None:
                    checker_object.render()
