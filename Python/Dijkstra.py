from PythonClientAPI.libs.Game.Enums import *
from PythonClientAPI.libs.Game.GameBoard import *
from PythonClientAPI.libs.Game.fibonacci_heap_mod import *
import queue
from queue import PriorityQueue
class grid:
    def __init__(self,x,y,value):
        self.x=x
        self.y=y
        self.value = value
    def mod_value(self,value):
        self.value = value
class Dijkstra:
    def __init__(self,gameboard):
        self.grid = [[None for x in range(gameboard.height)] for x in range(gameboard.width)]
        self.run()
        self.qset = queue()
        self.pqueue = PriorityQueue()

    def run(self, gameboard,x,y):
        print(gameboard.height*gameboard.width)
        for i in range (gameboard.height):
            for j in range (gameboard.width):
                self.grid[i][j] = grid(i,j,999)
                self.pqueue._put(self.grid[i][j])
        self.grid[x][y]=0
        while self.pqueue.empty():
            lilgrid = self.pqueue._get()
            
        pass

gameboard = Gameboard(10, 20, 0, 100)
a = Dijkstra(gameboard)
a.run(gameboard)


