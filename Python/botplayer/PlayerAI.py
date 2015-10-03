from PythonClientAPI.libs.Game.Enums import *
from PythonClientAPI.libs.Game.MapOutOfBoundsException import *


class PlayerAI:
    def __init__(self):
        # Initialize any objects or variables you need here.
            self.up = None
            self.right = None
            self.down = None
            self.left = None

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
        if player.direction == Direction.UP:
            self.up = Direction.UP
            self.right = Direction.RIGHT
            self.down = Direction.DOWN
            self.left = Direction.LEFT
        elif player.direction == Direction. RIGHT:
            self.up = Direction.RIGHT
            self.right = Direction.DOWN
            self.down = Direction.LEFT
            self.left = Direction.UP
        elif player.direction == Direction. DOWN:
            self.up = Direction.DOWN
            self.right = Direction.LEFT
            self.down = Direction.UP
            self.left = Direction.RIGHT
        elif player.direction == Direction. LEFT:
            self.up = Direction.LEFT
            self.right = Direction.UP
            self.down = Direction.RIGHT
            self.left = Direction.DOWN
        else:
            self.up = None
            self.right = None
            self.down = None
            self.left = None
    def get_left_private_direction(self, priv_direction):


    def get_valid_moves(self, gameboard, player, opponent):
        pass

    def get_move(self, gameboard, player, opponent):
        # Write your AI here.
        gameboard.bullets
        return Move.NONE

