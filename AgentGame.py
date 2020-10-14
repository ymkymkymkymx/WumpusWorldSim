from game import Game 
from observer import Observer
import signal
import time
from generatorv3 import *
'''
An example of how to combine generatorv3 with game
'''
def handle(signum,frame):
    raise RuntimeError
class AgentGame:
    def __init__(self,sizex,sizey,pits,diffy,agent,o1=Observer()):
        self.agent= agent
        self.o1 = o1 
        self.sizex= sizex
        self.sizey= sizey
        self.pits= pits
        self.diffy= diffy
        self.start_invis_board = tolistofset(findmap(sizex,sizey,pits,diffy),sizex,sizey)
        self.ob=Observer()
        self.g = Game() 
        self.g.subscribeObserver(o1)
        self.g.subscribeObserver(self.ob)
        self.g.startGame(self.start_invis_board)
        self.stepcount=0

    def step(self):
        if self.g.finished == True:
            return
        if self.stepcount>1000:
            print("Too much steps")
            return
           
        g1=self.g
        nextMove = ''
        x=g1.robot_position[0]
        y=g1.robot_position[1]
        sizex=self.sizex
        sizey=self.sizey
        for i in range(sizex):
            for j in range(sizey):
                if len(g1.visible_board[sizex-i-1][j])==0 and (sizex-i-1!=x or j!=y):
                    print("00000", end=" ")
                elif not (sizex-i-1!=x or j!=y):
                    print("here!",end=" ")
                else:
                    print("{}".format(g1.visible_board[sizex-i-1][j].difference({}).pop()), end=" ")
            print("")
        try:
        
            nextMove = self.agent.move(self.ob.currentstate())
            
        except Exception as e:
            print(e)
            print("Robot ran out of time")
            nextMove=''

        if nextMove == "move_up":
            g1.moveRobotUp()
        elif nextMove == "move_down":
            g1.moveRobotDown()
        # elif nextMove == "move_right":
        #     g1.moveRobotRight()
        elif nextMove == "move_left":
            g1.moveRobotLeft()
        elif nextMove == "move_right":
            g1.moveRobotRight() 
        elif nextMove == "shoot_up":
            g1.shootArrowUp()
        elif nextMove == "shoot_down":
            g1.shootArrowDown()
        elif nextMove == "shoot_right":
            g1.shootArrowRight()
        elif nextMove == "shoot_left":
            g1.shootArrowLeft() 
        else:
            print("INVALID MOVE")
            
        self.stepcount+=1
        return 



