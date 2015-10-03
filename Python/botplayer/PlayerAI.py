from PythonClientAPI.libs.Game.Enums import *
from PythonClientAPI.libs.Game.MapOutOfBoundsException import *


class PlayerAI:
    def __init__(self):
        self.i = 0
        # Initialize any objects or variables you need here.
        self.i = 0
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

    def is_bullet_chasing(self,player, gameboard):
        player_position = player.x, player.y
        behind_slot = player_position - self.relative_offset_to_absolute(0, 1)
        if gameboard.are_bullets_at_tile(behind_slot):
            bullets = gameboard.bullets_at_tile[behind_slot[0]][behind_slot[1]]
            for bullet in bullets:
                if bullet.direction == player.direction:
                    return True
                else:
                    pass
        return False



    def get_valid_moves(self, gameboard, player, opponent):
        valid_moves = [Move.NONE]
        if self.is_bullet_chasing(player, gameboard):
            valid_moves.append(Move.FORWARD)
            return valid_moves
        return valid_moves


        # if there is a bullet right behind you, you can only move forward


    def get_move(self, gameboard, player, opponent):
        # Write your AI here.

        return Move.NONE
=======


    def get_move(self, gameboard, player, opponent):
        # Write your AI here.
        #gameboard.bullets
        # Write your AI here.
        if self.i == 0:
            self.i = self.i+1
            return Move.FACE_LEFT
        elif self.i == 1:
            self.i = self.i+1
            return Move.SHOOT
        elif self.i == 2:
            self.i = self.i+1
            return Move.FACE_RIGHT
        elif self.i == 3:
            self.i = self.i+1
            return Move.SHOOT
        else :
            return Move.NONE
>>>>>>> new changes

