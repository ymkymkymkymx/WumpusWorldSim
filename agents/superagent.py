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
                line.append(Node(i,j,"e",self.sizex,self.sizey))
            themap.append(line)
        themap[0][0].visited=True
        themap[0][0].nw=True
        themap[0][0].np=True
        themap[0][0].ng=True
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
        newhistory=history.copy()
        newhistory.add((i,j))
        if(i==destinex and j==destiney):  return path
        
        if(i+1<self.sizex and ((i+1,j) not in newhistory) and (gamestate[i+1][j].visited==True or (i+1==destinex and j==destiney) ) ):
            pathup=path.copy()
            pathup.append("move_up")
            resultpath=self.dfs(i+1,j,destinex,destiney,newhistory,pathup)
            if(len(resultpath)>0): return resultpath
        if(j+1<self.sizey and ((i,j+1) not in newhistory) and (gamestate[i][j+1].visited==True or (i==destinex and j+1==destiney) ) ):
            pathright=path.copy()
            pathright.append("move_right")
            resultpath=self.dfs(i,j+1,destinex,destiney,newhistory,pathright)
            if(len(resultpath)>0): return resultpath
        if(i-1>=0 and ((i-1,j) not in newhistory) and (gamestate[i-1][j].visited==True or (i-1==destinex and j==destiney) ) ):
            pathdown=path.copy()
            pathdown.append("move_down")
            resultpath=self.dfs(i-1,j,destinex,destiney,newhistory,pathdown)
            if(len(resultpath)>0): return resultpath
        if(j-1>=0 and ((i,j-1) not in newhistory) and (gamestate[i][j-1].visited==True or (i==destinex and j-1==destiney) ) ):
            pathleft=path.copy()
            pathleft.append("move_left")
            resultpath=self.dfs(i,j-1,destinex,destiney,newhistory,pathleft)
            if(len(resultpath)>0): return resultpath
        
        resultpath=deque()
        return resultpath
    
    def checknextpos(self):
        gamestate=self.board
        for i in range(self.sizex):
            for j in range(self.sizey):
                if (gamestate[i][j].np==True and gamestate[i][j].nw==True and gamestate[i][j].visited==False):
                    gamestate[i][j].visited=True
                    return (i,j)
        return (-1,-1)
    
    def parsemessage(self,messages):
        gamestate=self.board
        i=self.x
        j=self.y
        mapsizex=self.sizex
        mapsizey=self.sizey
        for message in messages:
            if message=="STENCH":
                gamestate[i][j].stench=True
            if message=="BREEZE":
                gamestate[i][j].breeze=True
            if message=="GLITTER":
                gamestate[i][j].glitter=True
                
        if (gamestate[i][j].breeze and gamestate[i][j].stench):
            for x in range(mapsizex):
                for y in range(mapsizey):
                    if(not ((x==i+1 and y==j) or (x==i-1 and y==j) or (x==i and y==j+1) or (x==i and y==j-1))):
                        gamestate[x][y].nw=True		
    
        elif(gamestate[i][j].stench):
            for x in range(mapsizex):
                for y in range(mapsizey):
                    if(not ((x==i+1 and y==j) or (x==i-1 and y==j) or (x==i and y==j+1) or (x==i and y==j-1))):
                        gamestate[x][y].nw=True
    
            if(i+1<mapsizex):
                gamestate[i+1][j].np=True
            if(j+1<mapsizey):
                gamestate[i][j+1].np=True
            if(i-1>=0):
                gamestate[i-1][j].np=True
            if(j-1>=0):
                gamestate[i][j-1].np=True
    
        elif(gamestate[i][j].breeze):
            if(i+1<mapsizex):
                gamestate[i+1][j].nw=True
            if(j+1<mapsizey):
                gamestate[i][j+1].nw=True
            if(i-1>=0):
                gamestate[i-1][j].nw=True
            if(j-1>=0):
                gamestate[i][j-1].nw=True
    
        else:
            if(i+1<mapsizex):
                gamestate[i+1][j].np=True
            if(j+1<mapsizey):
                gamestate[i][j+1].np=True
            if(i-1>=0):
                gamestate[i-1][j].np=True
            if(j-1>=0):
                gamestate[i][j-1].np=True
            if(i+1<mapsizex):
                gamestate[i+1][j].nw=True
            if(j+1<mapsizey):
                gamestate[i][j+1].nw=True
            if(i-1>=0):
                gamestate[i-1][j].nw=True
            if(j-1>=0):
                gamestate[i][j-1].nw=True
    
        if(gamestate[i][j].glitter):
            for x in range(mapsizex):
                for y in range(mapsizey):
                    if(not ((x==i+1 and y==j) or (x==i-1 and y==j) or (x==i and y==j+1) or (x==i and y==j-1))):
                        gamestate[x][y].ng=True
    
        else:
            if(i+1<mapsizex):
                gamestate[i+1][j].ng=True
            if(j+1<mapsizey):
                gamestate[i][j+1].ng=True
            if(i-1>=0):
                gamestate[i-1][j].ng=True
            if(j-1>=0):
                gamestate[i][j-1].ng=True
        return

    def ivegotyouinmysight(self):
        count=0
        for i in range(self.sizex):
            for j in range(self.sizey):
                if(self.board[i][j].nw==False):
                    count+=1
        if count==1:
            return True
        else:
            return False
    def checkvisitedaround(self,i,j):
        gamestate=self.board
        mapsizex=self.sizex
        mapsizey=self.sizey
        if(i+1<mapsizex and gamestate[i+1][j].visited==True):
            return (i+1,j)
        if(j+1<mapsizey and gamestate[i][j+1].visited==True):
            return (i,j+1)
        if(i-1>=0 and gamestate[i-1][j].visited==True):
            return (i-1,j)
        if(j-1>=0 and gamestate[i][j-1].visited==True):
            return (i,j-1)
        return (-1,-1)
    def itshighnoon(self):
        wx=0
        wy=0
        x=self.x
        y=self.y
        for i in range(self.sizex):
            for j in range(self.sizey):
                if(self.board[i][j].nw==False):
                    wx=i
                    wy=j
        destx,desty= self.checkvisitedaround(wx,wy)
        path=deque()
        history=set()
        thepath=self.dfs(x,y,destx,desty,history,path)
        execution=""
        if wx-destx==1:
            execution="shoot_up"
        elif wx-destx==-1:
            execution="shoot_down"
        elif wy-desty==1:
            execution="shoot_right"
        elif wy-desty==-1:
            execution="shoot_left"
        thepath.append(execution)
        self.x=destx
        self.y=desty
        self.board[wx][wy].nw=True
        self.board[wx][wy].np=True
        self.nextmoves=thepath
       
     
    def checkgold(self):  
        count=0
        goldnear=False
        for i in range(self.sizex):
            for j in range(self.sizey):
                if(self.board[i][j].ng==False):
                    count+=1
                    a,b=self.checkvisitedaround(i,j)
                    if a!=-1:
                        goldnear=True
                    
        if count==1 and goldnear:
            return True
        else:
            return False 
    
    def tovictory(self):
        gx=0
        gy=0
        x=self.x
        y=self.y
        for i in range(self.sizex):
            for j in range(self.sizey):
                if(self.board[i][j].ng==False):
                    gx=i
                    gy=j
        path=deque()
        history=set()
        goldpath=self.dfs(x,y,gx,gy,history,path)
        thepath=self.dfs(gx,gy,0,0,history,goldpath)
        self.x=0
        self.y=0
        self.nextmoves=thepath
        
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
        self.parsemessage(state[0])
                
        
        if self.ivegotyouinmysight():
            self.itshighnoon()
            return self.nextmoves.popleft()
        
        if self.checkgold():
            self.tovictory()
            return self.nextmoves.popleft()        
        
        nextx,nexty=self.checknextpos()
        x=self.x
        y=self.y
        history=set()
        path=deque()
        thepath=self.dfs(x,y,nextx,nexty,history,path)
        self.nextmoves=thepath
        self.x=nextx
        self.y=nexty
        print(self.x)
        print(self.y)
        return self.nextmoves.popleft()