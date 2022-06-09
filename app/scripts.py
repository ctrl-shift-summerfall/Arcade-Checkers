# Internal settings and variables:
from app.settings import (GRID_NUMERIC_INDEX_STRING, GRID_ALPHABETIC_INDEX_STRING,
                          BOARD_MARGIN_TOTAL_WIDTH, BOARD_TILE_SIDE_SIZE_PX, BOARD_PLAY_SURFACE_MIN, BOARD_PLAY_SURFACE_MAX)


def convert_grid_position_to_alphanumeric_position(conv_grid_position: list):
    row, column = conv_grid_position
    numeric_index = GRID_NUMERIC_INDEX_STRING[row]
    alphabetic_index = GRID_ALPHABETIC_INDEX_STRING[column]
    alphanumeric_position = f'{alphabetic_index}{numeric_index}'
    return alphanumeric_position


def convert_alphanumeric_position_to_grid_position(conv_alphanumeric_position: str):
    alphabetic_index, numeric_index = conv_alphanumeric_position[0], conv_alphanumeric_position[1]
    row = GRID_NUMERIC_INDEX_STRING.index(numeric_index)
    column = GRID_ALPHABETIC_INDEX_STRING.index(alphabetic_index)
    grid_position = [row, column]
    return grid_position

def convert_coordinates_to_grid_position(conv_coordinates: list):
    grid_position = None
    coordinate_x, coordinate_y = conv_coordinates
    if bool(BOARD_PLAY_SURFACE_MAX > coordinate_x > BOARD_PLAY_SURFACE_MIN and
            BOARD_PLAY_SURFACE_MAX > coordinate_y > BOARD_PLAY_SURFACE_MIN):
        row = int((coordinate_x - BOARD_MARGIN_TOTAL_WIDTH) // BOARD_TILE_SIDE_SIZE_PX)
        column = int((coordinate_y - BOARD_MARGIN_TOTAL_WIDTH) // BOARD_TILE_SIDE_SIZE_PX)
        grid_position = [row, column]
    return grid_position

def convert_grid_position_to_coordinates(conv_grid_position: list):
    row, column = conv_grid_position
    coordinate_x = int(BOARD_MARGIN_TOTAL_WIDTH + BOARD_TILE_SIDE_SIZE_PX / 2 + BOARD_TILE_SIDE_SIZE_PX * (column))
    coordinate_y = int(BOARD_MARGIN_TOTAL_WIDTH + BOARD_TILE_SIDE_SIZE_PX / 2 + BOARD_TILE_SIDE_SIZE_PX * (row))
    coordinates = [coordinate_x, coordinate_y]
    return coordinates

def create_new_checker(ch_color: str, ch_type: str, ch_grid_position: list):
    from app.checker import Checker

    new_checker = Checker()
    new_checker.color = ch_color
    new_checker.type = ch_type
    new_checker.position_grid = ch_grid_position
    new_checker.update()

    return new_checker