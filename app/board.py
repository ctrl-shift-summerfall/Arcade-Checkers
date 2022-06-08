# Internal settings and variables:
from app.settings import (BOARD_TILE_SIZE_PX, BOARD_HEIGHT, BOARD_WIDTH,
                          BOARD_CENTER_POSITION_X, BOARD_CENTER_POSITION_Y,
                          BOARD_MARGIN_INNER_WIDTH, BOARD_MARGIN_INNER_COLOR,
                          BOARD_MARGIN_OUTER_WIDTH, BOARD_MARGIN_OUTER_COLOR,
                          BOARD_TILE_COLOR_BLACK, BOARD_TILE_COLOR_WHITE,
                          GRID_ALPHABETIC_INDEX_STRING, GRID_NUMERIC_INDEX_STRING,
                          GRID_ROW_COUNT, GRID_COLUMN_COUNT)
                          
from app.variables import (VAR_BOARD_TILE_COLOR_BLACK, VAR_BOARD_TILE_COLOR_WHITE, 
                           VAR_SESSION_RENDER_MODE_OPENGL, VAR_SESSION_RENDER_MODE_TEXTURE)

# External libraries:
import arcade


class Board:
    
    def __init__(self):
        pass

    def render(self):
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
            tile_color = VAR_BOARD_TILE_COLOR_BLACK
            tile_center_coordinate_x = int(BOARD_MARGIN_OUTER_WIDTH + BOARD_MARGIN_INNER_WIDTH + BOARD_TILE_SIZE_PX / 2)
            tile_center_coordinate_y = int(BOARD_MARGIN_OUTER_WIDTH + BOARD_MARGIN_INNER_WIDTH + BOARD_TILE_SIZE_PX / 2)
            for row in range(GRID_ROW_COUNT):
                for column in range(GRID_COLUMN_COUNT):
                    arcade.draw_rectangle_filled(
                        center_x=tile_center_coordinate_x,
                        center_y=tile_center_coordinate_y,
                        width=BOARD_TILE_SIZE_PX,
                        height=BOARD_TILE_SIZE_PX,
                        color=BOARD_TILE_COLOR_BLACK if tile_color == VAR_BOARD_TILE_COLOR_BLACK else BOARD_TILE_COLOR_WHITE,
                        tilt_angle=0)
                    if tile_color == VAR_BOARD_TILE_COLOR_BLACK:
                        tile_color = VAR_BOARD_TILE_COLOR_WHITE
                    else:
                        tile_color = VAR_BOARD_TILE_COLOR_BLACK
                    tile_center_coordinate_x += BOARD_TILE_SIZE_PX
                tile_center_coordinate_x = int(BOARD_MARGIN_OUTER_WIDTH + BOARD_MARGIN_INNER_WIDTH + BOARD_TILE_SIZE_PX / 2)
                tile_center_coordinate_y += BOARD_TILE_SIZE_PX
                if tile_color == VAR_BOARD_TILE_COLOR_BLACK:
                        tile_color = VAR_BOARD_TILE_COLOR_WHITE
                else:
                    tile_color = VAR_BOARD_TILE_COLOR_BLACK
            
            # Rendering alphanumeric index:
            # TODO: Create render script for alphanumeric index
            pass

        elif SESSION.SESSION_RENDER_MODE == VAR_SESSION_RENDER_MODE_TEXTURE:
            pass
