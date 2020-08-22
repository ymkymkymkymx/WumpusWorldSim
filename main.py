from game import Game 
from observer import Observer



def main() :
    o1 = Observer() 
    start_invis_board = [[set() for j in range(4)] for i in range(4)]
    start_invis_board[2][0].add("LiveWumpus")
    start_invis_board[2][1].add("Gold")
    start_invis_board[0][2].add("Pit")
    start_invis_board[2][2].add("Pit")
    start_invis_board[3][3].add("Pit")

    g1 = Game() 
    g1.subscribeObserver(o1)

    g1.startGame(start_invis_board)
    nextMove = ''
    while(1):
        nextMove = input("Next Move: ")
        if nextMove == "move_up":
            g1.moveRobotUp()
        elif nextMove == "move_down":
            g1.moveRobotDown()
        elif nextMove == "move_right":
            g1.moveRobotRight()
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
        print("")
    return 0



main() 
    
