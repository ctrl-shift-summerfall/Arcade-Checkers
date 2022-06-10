# Internal settings and variables:
from app.variables import (VAR_CHECKER_COLOR_NOT_SET, VAR_CHECKER_COLOR_BLACK, VAR_CHECKER_COLOR_WHITE,
                           VAR_CHECKER_TYPE_NOT_SET, VAR_CHECKER_TYPE_ORDINARY, VAR_CHECKER_TYPE_QUEEN,
                           VAR_SESSION_RENDER_MODE_OPENGL, VAR_SESSION_RENDER_MODE_TEXTURE)

from app.settings import (CHECKER_COLOR_WHITE, CHECKER_COLOR_WHITE_ALTERNATIVE,
                          CHECKER_COLOR_BLACK, CHECKER_COLOR_BLACK_ALTERNATIVE,
                          CHECKER_SIZE_RADIUS_PX, CHECKER_INNER_RADIUS_PX, CHECKER_ADJUST_POSITION_PX,
                          CHECKER_TILT_ANGLE_MIN, CHECKER_TILT_ANGLE_MAX)

# Internal scripts:
from app.scripts import (convert_grid_position_to_alphanumeric_position,    # [row, column] --> "A1"
                         convert_grid_position_to_coordinates)              # [row, column] --> [coord_x, coord_y]

# External libraries:
import arcade


class Checker:

    def __init__(self, 
                 set_color: str = VAR_CHECKER_COLOR_NOT_SET,
                 set_type: str = VAR_CHECKER_TYPE_NOT_SET,
                 set_position: list = [0, 0]):
        
        # Core attributes:
        self.color: str = set_color
        self.type: str = set_type
        self.position_grid: list = set_position             # [row, column]
        self.position_coordinates: list = None              # [coord_x, coord_y]
        self.position_alphanumeric: str = None              # "A1"
        self.waypoints: list = []                           # [["A1", @CheckerObject], ...]

        self.selected: bool = False
        self.update()

    @property
    def can_move(self):
        can_move_status = False
        if len(self.waypoints) > 0:
            can_move_status = True
        return can_move_status

    @property
    def can_attack(self):
        can_attack_status = False
        if self.can_move:
            for waypoint in self.waypoints:
                for move_position, kill_position in waypoint:
                    if kill_position is not None:
                        can_attack_status = True
                        break
        return can_attack_status

    @property
    def can_upgrade(self):
        can_upgrade_status = False
        if self.type == VAR_CHECKER_TYPE_ORDINARY:
            letter, number = self.position_alphanumeric[0], self.position_alphanumeric[1]
            if bool(self.color == VAR_CHECKER_COLOR_WHITE and number == '8' or 
                    self.color == VAR_CHECKER_COLOR_BLACK and number == 1):
                can_upgrade_status = True
        return can_upgrade_status
    
    def update(self):
        self._update_alphanumeric_position()
        self._update_coordinates_position()
        if self.can_upgrade:
            # TODO: Create upgrade script.
            pass

    def _update_coordinates_position(self):
        new_coordinates_position = convert_grid_position_to_coordinates(conv_grid_position=self.position_grid)
        self.position_coordinates = new_coordinates_position

    def _update_alphanumeric_position(self):
        new_alphanumeric_position = convert_grid_position_to_alphanumeric_position(conv_grid_position=self.position_grid)
        self.position_alphanumeric = new_alphanumeric_position

    def render(self):
        import app.session as SESSION

        if SESSION.SESSION_RENDER_MODE == VAR_SESSION_RENDER_MODE_OPENGL:
            
            # Getting coordinates and color codes for rendering:
            coordinate_x, coordinate_y = self.position_coordinates
            if self.color == VAR_CHECKER_COLOR_WHITE:
                color_main = CHECKER_COLOR_WHITE
                color_alternative = CHECKER_COLOR_WHITE_ALTERNATIVE
                text_color = CHECKER_COLOR_BLACK_ALTERNATIVE
            elif self.color == VAR_CHECKER_COLOR_BLACK:
                color_main = CHECKER_COLOR_BLACK
                color_alternative = CHECKER_COLOR_BLACK_ALTERNATIVE
                text_color = CHECKER_COLOR_WHITE_ALTERNATIVE
            else:
                color_main = [255, 0, 0]
                color_alternative = [225, 0, 0]
                text_color = CHECKER_COLOR_BLACK_ALTERNATIVE

            # Rendering outer radius:
            arcade.draw_circle_filled(
                center_x=coordinate_x - int(CHECKER_ADJUST_POSITION_PX / 2),
                center_y=coordinate_y - int(CHECKER_ADJUST_POSITION_PX / 2),
                radius=CHECKER_SIZE_RADIUS_PX,
                color=color_alternative,
                tilt_angle=CHECKER_TILT_ANGLE_MIN * 0,
                num_segments=64)
            arcade.draw_circle_filled(
                center_x=coordinate_x + int(CHECKER_ADJUST_POSITION_PX / 2),
                center_y=coordinate_y + int(CHECKER_ADJUST_POSITION_PX / 2),
                radius=CHECKER_SIZE_RADIUS_PX,
                color=color_main,
                tilt_angle=CHECKER_TILT_ANGLE_MIN * 0,
                num_segments=64)

            # Rendering inner radius:
            arcade.draw_circle_filled(
                center_x=coordinate_x + int(CHECKER_ADJUST_POSITION_PX / 2),
                center_y=coordinate_y + int(CHECKER_ADJUST_POSITION_PX / 2),
                radius=CHECKER_INNER_RADIUS_PX,
                color=color_alternative,
                tilt_angle=CHECKER_TILT_ANGLE_MIN * 0,
                num_segments=64)
            arcade.draw_circle_filled(
                center_x=coordinate_x - int(CHECKER_ADJUST_POSITION_PX / 2),
                center_y=coordinate_y - int(CHECKER_ADJUST_POSITION_PX / 2),
                radius=CHECKER_INNER_RADIUS_PX,
                color=color_main,
                tilt_angle=CHECKER_TILT_ANGLE_MIN * 0,
                num_segments=64)

            # Rendering "Queen" tag, if checker type is Queen:
            if self.type == VAR_CHECKER_TYPE_QUEEN:
                arcade.draw_text(
                    text='Queen',
                    start_x=coordinate_x,
                    start_y=coordinate_y,
                    color=text_color,
                    anchor_x='center',
                    anchor_y='center',
                    rotation=0,
                    font_name='verdana')

        elif SESSION.SESSION_RENDER_MODE == VAR_SESSION_RENDER_MODE_TEXTURE:
            pass