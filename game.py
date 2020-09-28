from observer import Observer





class Game : 
    
    def __init__(self):
        self.observers = [] 

    def resetGame(self, start_board):
        self.M = len(start_board)
        self.N = len(start_board[0])

        self.visible_board = [[set() for j in range(self.N)] for i in range(self.M)]

        self.finished = False 
        self.invisible_board = start_board 

        dirs = [0, 1, 0, -1, 0] 

        for i in range(self.M):
            for j in range(self.N):
                for x in range(4):
                    npos = [i + dirs[x], j + dirs[x + 1]]
                    if self.checkPosition(npos):
                        if "LiveWumpus" in self.invisible_board[i][j]:
                            self.invisible_board[npos[0]][npos[1]].add("Stench")
                        if "Pit" in self.invisible_board[i][j]:
                            self.invisible_board[npos[0]][npos[1]].add("Breeze")
                        if "Gold" in self.invisible_board[i][j]:
                            self.invisible_board[npos[0]][npos[1]].add("Glitter")
        
        self.robot_position = [0, 0]
        self.hasArrow = True 
        self.foundGold = False  
        self.notifyObservers( self.visible_board, self.robot_position, "", self.hasArrow, self.foundGold, [0,1])
    

    def startGame(self, start_board):
        self.resetGame(start_board) 


    def broadcastStateOnMove(self):
        messages = []
        rxi = self.robot_position[0]
        ryi = self.robot_position[1]
        if not self.checkPosition(self.robot_position):
            self.finished = True 
            messages.append("FAIL")
            messages.append("OUT-OF-BOUNDS")
            self.notifyObservers(self.visible_board, self.robot_position, messages, self.hasArrow, self.foundGold, [0, 1])
            return 
        
        if "Pit" in self.invisible_board[rxi][ryi]:
            self.finished = True 
            messages.append("FAIL")
            messages.append("PIT")
            self.visible_board[rxi][ryi].add("Pit")
            self.notifyObservers(self.visible_board, self.robot_position, messages, self.hasArrow, self.foundGold, [0, 1])
            return
        
        if "LiveWumpus" in self.invisible_board[rxi][ryi]:
            self.finished = True 
            messages.append("FAIL")
            messages.append("LIVE-WUMPUS")
            self.visible_board[rxi][ryi].add("LiveWumpus")
            self.notifyObservers(self.visible_board, self.robot_position, messages, self.hasArrow, self.foundGold, [0, 1])
            return 
        if self.foundGold and rxi == 0 and ryi == 0:
            self.finished = True 
            messages.append("SUCCESS")
            self.notifyObservers(self.visible_board, self.robot_position, messages, self.hasArrow, self.foundGold, [0, 1])
            return 
        
        messages.append("CONTINUE")
        if "Breeze" in self.invisible_board[rxi][ryi]:
            messages.append("BREEZE")
            self.visible_board[rxi][ryi].add("Breeze")
        if "Stench" in self.invisible_board[rxi][ryi]:
            messages.append("STENCH")
            self.visible_board[rxi][ryi].add("Stench")
        if "Glitter" in self.invisible_board[rxi][ryi]:
            messages.append("GLITTER")
            self.visible_board[rxi][ryi].add("Glitter")
        if "Gold" in self.invisible_board[rxi][ryi]:
            messages.append("GOLD")
            self.visible_board[rxi][ryi].add("Gold")
            self.foundGold = True 

        self.notifyObservers(self.visible_board, self.robot_position, messages, self.hasArrow, self.foundGold, [0, 1])


    def broadcastStateOnShoot(self, up, right):
        messages = [] 
        messages.append("SHOOT")

        if not self.hasArrow:
            messages.append("NO-MORE-ARROWS")
            self.notifyObservers(self.visible_board, self.robot_position, messages, self.hasArrow, self.foundGold, [0, 1])
            return
        
        dirs = [0, 1, 0, -1, 0]
        rxi = self.robot_position[0]
        ryi = self.robot_position[1]

        axi = rxi + up 
        ayi = ryi + right 

        self.hasArrow = False 

        self.invisible_board[axi][ayi].add("Arrow")
        self.visible_board[axi][ayi].add("Arrow")

        if "LiveWumpus" in self.invisible_board[axi][ayi]:
            self.invisible_board[axi][ayi].discard("LiveWumpus")
            self.invisible_board[axi][ayi].add("DeadWumpus")
            self.visible_board[axi][ayi].add("DeadWumpus")
            messages.append("KILLED-WUMPUS")

            for i in range(4):
                if self.checkPosition([axi + dirs[i], ayi + dirs[i + 1]]):
                    self.invisible_board[axi + dirs[i]][ayi + dirs[i + 1]].discard("Stench")
                    self.visible_board[axi + dirs[i]][ayi + dirs[i + 1]].discard("Stench")

        else:
            messages.append("MISSED-WUMPUS")

        self.notifyObservers(self.visible_board, self.robot_position, messages, self.hasArrow, self.foundGold, [0, 1])


    def subscribeObserver(self, observer):
        self.observers.append(observer) 



    def notifyObservers(self, visible_board, robot_position, messages, hasArrow, hasGold, orientation):
        for observer in self.observers: 
            observer.update(visible_board, robot_position, messages, hasArrow, hasGold, orientation)




    def moveRobotUp(self):
        if not self.finished:
            self.robot_position[0] += 1 
            self.broadcastStateOnMove()

    def moveRobotDown(self):
        if not self.finished:
            self.robot_position[0] -= 1
            self.broadcastStateOnMove()
    
    def moveRobotLeft(self):
        if not self.finished:
            self.robot_position[1] -= 1
            self.broadcastStateOnMove()

    def moveRobotRight(self):
        if not self.finished:
            self.robot_position[1] += 1 
            self.broadcastStateOnMove()
    
    def shootArrowUp(self):
        if not self.finished:
            self.broadcastStateOnShoot(1, 0)

    def shootArrowDown(self):
        if not self.finished:
            self.broadcastStateOnShoot(-1, 0)

    def shootArrowRight(self):
        if not self.finished:
            self.broadcastStateOnShoot(0, 1)

    def shootArrowLeft(self):
        if not self.finished:
            self.broadcastStateOnShoot(0, -1)


    def checkPosition(self, position):
        return position[0] >= 0 and position[1] >= 0 and position[0] < self.M and position[1] < self.N