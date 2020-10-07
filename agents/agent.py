class Agent:
    def __init__(self,sizex, sizey):
        self.sizex=sizex
        self.sizey=sizey        
        ##TODO: Put the variables you need for your agents here.

        
    ##TODO: define the functions you need here
    
    
    '''
    move(visible_board) will read in a current board which shows the state of the game that should be visible to the robot and return the move the agent will make based on the current information. 
    This is the only function that will be called by the game and the name, param and return must not be changed.
    @param state will be a tuple (visible_board, robot_position, messages, hasArrow, hasGold, orientation)      orientation is currently useless.
           The visible_board will be a list(list(set)) where the set keeps all the information about a node. visible_board[i][j] will be like:
                                                   i=2  *   *   *
                                                   i=1  *   *   *
                                                   i=0  *   *   *
                                                       j=0 j=1 j=2
    @return This function should return a string "move_up", "move_down" , "move_left", "move_right" , "shoot_up", "shoot_down", "shoot_right", "shoot_left" based on the current state.
    '''
    def move(self,state):
        ##TODO: Implement your algorithm here
        return "move_right"