from PythonClientAPI.libs.Game.Enums import *
from botplayer.Maniac import *
from PythonClientAPI.libs.Game.MapOutOfBoundsException import *
import operator
import math


class PlayerAI:
    def __init__(self):
        # Initialize any objects or variables you need here.
            self.i = 0
            self.up = None
            self.right = None
            self.down = None
            self.left = None
            self.height = None
            self.width = None
            self.turret_counter = None
            self.vertical = None
            self.maniac = Maniac()

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

    def translate_directions(self, player, gameboard):
        if player.direction == Direction.UP:
            self.up = Direction.UP
            self.right = Direction.RIGHT
            self.down = Direction.DOWN
            self.left = Direction.LEFT
            self.height = gameboard.height
            self.width = gameboard.width
            self.vertical = True
        elif player.direction == Direction. RIGHT:
            self.up = Direction.RIGHT
            self.right = Direction.DOWN
            self.down = Direction.LEFT
            self.left = Direction.UP
            self.height = gameboard.width
            self.width = gameboard.height
            self.vertical = False
        elif player.direction == Direction. DOWN:
            self.up = Direction.DOWN
            self.right = Direction.LEFT
            self.down = Direction.UP
            self.left = Direction.RIGHT
            self.height = gameboard.height
            self.width = gameboard.width
            self.vertical = True
        elif player.direction == Direction. LEFT:
            self.up = Direction.LEFT
            self.right = Direction.UP
            self.down = Direction.RIGHT
            self.left = Direction.DOWN
            self.height = gameboard.width
            self.width = gameboard.height
            self.vertical = False
        else:
            pass

    def is_bullet_chasing(self, player, gameboard):
        player_position = player.x, player.y
        behind_slot = tuple(map(operator.add, player_position, self.relative_offset_to_absolute(player.direction, 0,1)))
        if behind_slot[0] < 0 or behind_slot[0] == gameboard.width or behind_slot[1] < 0 or behind_slot[1] == gameboard.height:
            behind_slot = tuple(map(operator.add, player_position, self.relative_offset_to_absolute(player.direction, 0,-self.height + 1)))
        if gameboard.are_bullets_at_tile(behind_slot[0], behind_slot[1]):
            bullets = gameboard.bullets_at_tile[behind_slot[0]][behind_slot[1]]
            for bullet in bullets:
                if bullet.direction == player.direction:
                    return True
        return False

    def distance(self, pos1, pos2):
        return math.sqrt((pos1[0] - pos2[0])**2 + (pos1[1] - pos2[1])**2)

    def in_turret_range(self, turret, player_x, player_y):
        if self.distance((turret.x, turret.y), (player_x, player_y)) < 5:
            return True

    def get_left_coords(self, player, player_position, gameboard):
        left_bullet_slot = tuple(map(operator.add, player_position, self.relative_offset_to_absolute(player.direction, -1,0)))
        if left_bullet_slot[0] < 0 or left_bullet_slot[0] == gameboard.width or left_bullet_slot[1] < 0 or left_bullet_slot[1] == gameboard.height:
            left_bullet_slot = tuple(map(operator.add, player_position, self.relative_offset_to_absolute(player.direction, self.width - 1, 0,)))
        return left_bullet_slot

    def get_right_coords(self, player, player_position, gameboard):
        right_bullet_slot = tuple(map(operator.add, player_position, self.relative_offset_to_absolute(player.direction, +1,0)))
        if right_bullet_slot[0] < 0 or right_bullet_slot[0] == gameboard.width or right_bullet_slot[1] < 0 or right_bullet_slot[1] == gameboard.height:
            right_bullet_slot = tuple(map(operator.add, player_position, self.relative_offset_to_absolute(player.direction, -self.width + 1, 0)))
        return right_bullet_slot

    def get_front_coords(self, player, player_position, gameboard):
        front_bullet_slot = tuple(map(operator.add, player_position, self.relative_offset_to_absolute(player.direction, 0,-1)))
        if front_bullet_slot[0] < 0 or front_bullet_slot[0] == gameboard.width or front_bullet_slot[1] < 0 or front_bullet_slot[1] == gameboard.height:
            front_bullet_slot = tuple(map(operator.add, player_position, self.relative_offset_to_absolute(player.direction, 0, self.height - 1)))
        return front_bullet_slot

    def turret_dangerous(self, turret):
        print("turret_counter")
        print(self.turret_counter[turret.x][turret.y])
        print("cool down + fire time")
        print(turret.cooldown_time + turret.fire_time)
        if turret.is_dead or self.turret_counter[turret.x][turret.y] > turret.fire_time:
            return False
        else:
            return True

    def immediate_danger(self, gameboard, player):
        player_position = player.x, player.y
        for i in range(self.width):
            if self.vertical:
               turret_pos = (i, player.y)
            else:
                turret_pos = (player.x, i)
            if gameboard.is_turret_at_tile(turret_pos[0], turret_pos[1]):
                turret = gameboard.turret_at_tile[turret_pos[0]][turret_pos[1]]
                if not turret.is_dead and turret.is_firing_next_turn and self.in_turret_range(turret, player.x, player.y):
                    return True
        for i in range(gameboard.height):
            if gameboard.is_turret_at_tile(player.x, i):
                turret = gameboard.turret_at_tile[player.x][i]
                if turret.is_firing_next_turn and self.in_turret_range(turret, player.x, player.y):
                    return True

        left_bullet_slot = self.get_left_coords(player, player_position, gameboard)
        right_bullet_slot = self.get_right_coords(player, player_position, gameboard)

        left_bullets = gameboard.bullets_at_tile[left_bullet_slot[0]][left_bullet_slot[1]]
        right_bullets = gameboard.bullets_at_tile[right_bullet_slot[0]][right_bullet_slot[1]]

        for bullet in left_bullets:
            if bullet.direction == self.right:
                return True
        for bullet in right_bullets:
            if bullet.direction == self.left:
                return True
        return False

    def frontal_danger(self, player, gameboard, opponent):
        player_position = player.x, player.y
        front_slot = self.get_front_coords(player ,player_position, gameboard)
        front_left_slot = self.get_left_coords(player, front_slot, gameboard)
        front_right_slot = self.get_right_coords(player, front_slot, gameboard)
        front_front_slot = self.get_front_coords(player, front_slot, gameboard)

        print("player_position")
        print(player_position)
        print("front_slot")
        print(front_slot)
        print("front_left")
        print(front_left_slot)
        print("front_right")
        print(front_right_slot)
        print("front front")
        print(front_front_slot)

        if gameboard.is_wall_at_tile(front_slot[0], front_slot[1]) or front_slot == (opponent.x, opponent.y):
            return True
        for i in range(self.width):
            if self.vertical:
               turret_pos = (i, front_slot[1])
            else:
                turret_pos = (front_slot[0], i)
            if gameboard.is_turret_at_tile(turret_pos[0], turret_pos[1]):
                turret = gameboard.turret_at_tile[turret_pos[0]][turret_pos[1]]
                if self.turret_dangerous(turret) and self.in_turret_range(turret, front_slot[0],front_slot[1]):
                    return True
        if gameboard.are_bullets_at_tile(front_left_slot[0], front_left_slot[1]):
            for bullet in gameboard.bullets_at_tile[front_left_slot[0]][front_left_slot[1]]:
                if bullet.direction == self.right:
                    return True
        if gameboard.are_bullets_at_tile(front_right_slot[0], front_right_slot[1]):
            for bullet in gameboard.bullets_at_tile[front_right_slot[0]][front_right_slot[1]]:
                if bullet.direction == self.left:
                    return True

        if gameboard.are_bullets_at_tile(front_front_slot[0], front_front_slot[1]):
            for bullet in gameboard.bullets_at_tile[front_front_slot[0]][front_front_slot[1]]:
                if bullet.direction == self.down:
                    return True
        return False


    def get_valid_moves(self, gameboard, player, opponent):
        valid_moves = []
        if self.is_bullet_chasing(player, gameboard):
            valid_moves.append(Move.FORWARD)
            return valid_moves

        if self.immediate_danger(gameboard, player):
            valid_moves.append(Move.FORWARD)
            return valid_moves

        valid_moves.append(Move.SHOOT)
        valid_moves.append(Move.NONE)
        if (player.laser_count > 0):
            valid_moves.append(Move.LASER)
        if (player.shield_count > 0 and  (not player.shield_active)):
            valid_moves.append(Move.SHIELD)
        if not self.frontal_danger(player, gameboard, opponent):
            valid_moves.append(Move.FORWARD)



        return valid_moves



        # if there is a bullet right behind you, you can only move forward

    def update_turret_counters(self, gameboard):
        if self.turret_counter == None:
            self.turret_counter = [[None for x in range(gameboard.height)] for x in range(gameboard.width)]
            for turret in gameboard.turrets:
                self.turret_counter[turret.x][turret.y] = 0
            return
        else:
            for turret in gameboard.turrets:
                if self.turret_counter[turret.x][turret.y] == turret.fire_time + turret.cooldown_time - 1:
                    self.turret_counter[turret.x][turret.y] = 0
                    return
                self.turret_counter[turret.x][turret.y] += 1

    def get_move(self, gameboard, player, opponent):
        # Write your AI here.

        self.update_turret_counters(gameboard)
        self.translate_directions(player, gameboard)
        move_choice = Move.NONE
        valid_moves = self.get_valid_moves(gameboard, player, opponent)
        print (valid_moves)

        temp_move = self.maniac.checkforassasin(gameboard,player,opponent)
        if temp_move in valid_moves:
            move_choice = temp_move
        else:
            for move in valid_moves:
                move_choice = move
        return move_choice



