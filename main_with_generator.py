from game import Game 
from observer import Observer
from generatorv3 import *
'''
An example of how to combine generatorv3 with game
'''

def main() :
    o1 = Observer() 
    sizex= int(input("Sizex: "))
    sizey= int(input("Sizey: "))
    pits= int(input("The number of pits: "))
    diffy= int(input("The difficulty: "))
    start_invis_board = tolistofset(findmap(sizex,sizey,pits,diffy),sizex,sizey)
    g1 = Game() 
    g1.subscribeObserver(o1)

    g1.startGame(start_invis_board)
    nextMove = ''
    while(1):
        x=g1.robot_position[0]
        y=g1.robot_position[1]
        for i in range(sizex):
            for j in range(sizey):
                if len(g1.visible_board[sizex-i-1][j])==0 and (sizex-i-1!=x or j!=y):
                    print("00000", end=" ")
                elif not (sizex-i-1!=x or j!=y):
                    print("here!",end=" ")
                else:
                    print("{}".format(g1.visible_board[sizex-i-1][j].difference({}).pop()), end=" ")
            print("")
        nextMove = input("Next Move: ")
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
            print("INVALID MOVE, exiting...")
            return
        
    return 0



main() 
    
