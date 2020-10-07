from collections import deque
from nodeclass import  *
class Agent:
    def __init__(self,sizex,sizey):
        ##TODO: Put the variables you need for your agents here.
        self.board=[]
        self.nextmoves=deque()
        self.sizex=sizex
        self.sizey=sizey
        self.x=0
        self.y=0
        
    ##TODO: define the functions you need here
    def createboard(self):
        themap=list(list())
        for i in range(self.sizex):
            line=list()
            for j in range(self.sizey):
                line.append(Node(i,j,"e",wallsizex,wallsizey))
            themap.append(line)
        themap[0][0].visited=True
        themap[0][1].nw=True
        themap[0][1].np=True
        themap[1][0].nw=True
        themap[1][0].np=True        
        self.board=themap
        return
    
    def dfs(self,currentx,currenty,destinex,destiney,history,path):
        i=currentx
        j=currenty
        gamestate=self.board
        if(i==destinex and j==destiney):  return path
        
        if(i+1<self.sizex and gamestate[i+1][j].=True):
            
        if(j+1<self.sizey):
            gamestate[i][j+1].np=True
        if(i-1>=0):
            gamestate[i-1][j].np=True
        if(j-1>=0):
            gamestate[i][j-1].np=True
        
    """
    move(visible_board) will read in a current board which shows the state of the game that should be visible to the robot and return the move the agent will make based on the current information. 
    This is the only function that will be called by the game and the name, param and return must not be changed.
    @param state will be a tuple (visible_board, robot_position, messages, hasArrow, hasGold, orientation)      orientation is currently useless.
           The visible_board will be a list(list(set)) where the set keeps all the information about a node. visible_board[i][j] will be like:
                                                   i=2  *   *   *
                                                   i=1  *   *   *
                                                   i=0  *   *   *
                                                       j=0 j=1 j=2
    @return This function should return a string "move_up", "move_down" , "move_left", "move_right" , "shoot_up", "shoot_down", "shoot_right", "shoot_left" based on the current state.
    """
    def move(self,state):
        ##TODO: Implement your algorithm here
        if len(self.nextmoves)!=0:
            return self.nextmoves.popleft()
        if len(self.board)==0:
            self.createboard()
            
        return self.nextmoves.popleft()