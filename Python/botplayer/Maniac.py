from PythonClientAPI.libs.Game.Enums import *
class Maniac:
    def __init__(self):
        self.state = 0
    def act(self):
        self.state=self.state+1
        if self.state ==1:
            return Move.FACE_LEFT
        elif self.state ==2:
            return Move.SHOOT
        elif self.state ==3:
            return Move.SHOOT
        elif self.state ==4:
            return Move.FACE_DOWN
        elif self.state ==5:
            self.state = 0
            return Move.FORWARD
    def checkforassasin(self, gameboard, player, opponent):

        if player.laser_count!=0 and opponent.direction == player.direction and ((abs(player.x-opponent.x)<5 and opponent.x ==player.x) or (abs(player.x-opponent.x)<5 and opponent.y == player.y)):
            if(opponent.y>player.y and player.direction==Direction.DOWN):
                return Move.LASER
            if (opponent.y<player.y and player.direction==Direction.UP):
                return Move.LASER
            if (opponent.x<player.x and player.direction==Direction.LEFT):
                return Move.LASER
            if (opponent.x>player.x and player.direction==Direction.RIGHT):
                return Move.LASER

        """
        if ((abs(player.x-opponent.x)==1 or abs(player.x-opponent.x)==1)) and ((opponent.y == player.y) or (opponent.x == player.x)):
            if player.x<opponent.x and player.direction==Direction.LEFT:
             return Move.
        """

        if self.checkaim(gameboard, player, opponent) ==True:
            return Move.SHOOT
        else:
            return self.autoadjust(gameboard,player,opponent)




    def checkaim(self, gameboard, player, opponent):
            if opponent.y>player.y and player.direction==Direction.DOWN and opponent.x ==player.x:
                return True
            elif opponent.x == player.x and opponent.y<player.y and player.direction==Direction.UP:
                return True
            elif opponent.x<player.x and player.direction==Direction.LEFT and opponent.y==player.y:
                return True
            elif opponent.x>player.x and player.direction==Direction.RIGHT and opponent.y==player.y:
                return True
            else:
                return False
    def autoadjust(self, gameboard, player, opponent):
            if opponent.y>player.y and player.direction!=Direction.DOWN and opponent.x ==player.x:
                return Move.FACE_DOWN
            elif opponent.x == player.x and opponent.y<player.y and player.direction!=Direction.UP:
                return Move.FACE_UP
            elif opponent.x<player.x and player.direction!=Direction.LEFT and opponent.y==player.y:
                return Move.FACE_LEFT
            elif opponent.x>player.x and player.direction!=Direction.RIGHT and opponent.y==player.y:
                return Move.FACE_RIGHT
            else:
                return Move.NONE



