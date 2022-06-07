# Internal scripts and modules:
from app.settings import GRID_NUMERIC_INDEX_STRING, GRID_ALPHABETIC_INDEX_STRING


def convert_grid_position_to_alphanumeric_position(grid_position: list):
    row, column = grid_position
    numeric_index = GRID_NUMERIC_INDEX_STRING[row]
    alphabetic_index = GRID_ALPHABETIC_INDEX_STRING[column]
    alphanumeric_position = f'{alphabetic_index}{numeric_index}'
    return alphanumeric_position


def convert_alphanumeric_position_to_grid_position(alphanumeric_position: str):
    alphabetic_index, numeric_index = alphanumeric_position[0], alphanumeric_position[1]
    row = GRID_NUMERIC_INDEX_STRING.index(numeric_index)
    column = GRID_ALPHABETIC_INDEX_STRING.index(alphabetic_index)
    grid_position = [row, column]
    return grid_position
