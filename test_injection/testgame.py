from importlib import import_module, util
import imp 
# import our own simulator from /simulator/game.py 
game = imp.load_source('game', '../simulator/game.py')

# modified observer class that allows our simulator to communicate 
# with the student's Agent. 
class AgentObserver:
    def __init__ (self, solverObj):
        self.solver = solverObj 
        self.latestMove = ""
        nextMove = getattr(self.solver, 'nextMove', None)
        if not callable(nextMove):
            print("Agent Observer Error: user inputted solver does not contain def nextMove(), Exiting()...")
            exit() 
            
    def update(self, visible_board, robot_position, messages, hasArrow, hasGold, orientation):
        print("SYSTEM: " + str(messages))
        
        # exit if failure signal is recieved 
        if ("FAIL" in messages):
            print("Agent failure signal recieved. Exiting...")
            exit() 
        self.latestMove = self.solver.nextMove(messages)
        print("AGENT: " + self.latestMove) 

    def getLatestMove(self):
        return self.latestMove 
        

def main():

    # Import the agent from the desired file path. 
    fname = "" 
    fname = input("Input file to execute: ")

    try: 
        fname = fname.split('.')[0]
        Agent = import_module(fname).Agent
    except:
        print("error loading file. Exiting...")
        exit() 
    
    # instantiate the student's agent 
    s1 = Agent() 
    # create an agent observer using the student's agent
    o1 = AgentObserver(s1)

    # create a board. 
    start_invis_board = [[set() for j in range(4)] for i in range(4)]
    start_invis_board[2][0].add("LiveWumpus")
    start_invis_board[2][1].add("Gold")
    start_invis_board[0][2].add("Pit")
    start_invis_board[2][2].add("Pit")
    start_invis_board[3][3].add("Pit")

    # create a simulator object
    g1 = game.Game() 

    # subscribe the observer to the simulator object
    g1.subscribeObserver(o1)

    # start the game. This sends the first move to the student's agent
    g1.startGame(start_invis_board)

    # this variable contains the next move
    nextMove = '' 
    while(1):

        #get the latest move from the student's agent. 
        nextMove = o1.getLatestMove() 

        # map the next move to the simulator functions. 
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