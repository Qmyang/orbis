from PythonClientAPI.libs.Game.Enums import *
from PythonClientAPI.libs.Game.MapOutOfBoundsException import *


class PlayerAI:
    def __init__(self):
        # Initialize any objects or variables you need here.
        pass

    def relative_offset_to_absolute(self,facing, x, y):
        if facing == Direction.UP:
            return x,y
        elif facing == Direction.DOWN:
            return -x,-y
        elif facing == Direction.LEFT:
            return y,-x
        elif facing == Direction.RIGHT:
            return -y,x

    def public_direction_to_private(self, direction):
        if direction == Direction.UP:
            return 0
        elif direction == Direction.Right:
            return 1
        elif direction == Direction.Down:
            return 2
        elif direction == Direction.Left:
            return 3

    def translate_directions(self, player):
        self.

    def get_left_private_direction(self, priv_direction):


    def get_valid_moves(self, gameboard, player, opponent):
        pass

    def get_move(self, gameboard, player, opponent):
        # Write your AI here.
        gameboard.bullets
        return Move.NONE

