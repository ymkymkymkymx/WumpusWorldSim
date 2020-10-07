class Node:
    def __init__(self, xcoord, ycoord, label, wall_sizex,wall_sizey):
        self.xcoord = max(0, xcoord)
        self.ycoord = max(0, ycoord)
        self.label = label
        # min wall size is 4 so check that wall size is at least 4
        self.wall_sizex = max(4, wall_sizex)
        self.wallsizey=max(4,wall_sizey)
        self.nw = False
        self.np = False
        self.ng = False
        self.visited = False
        self.breeze = False
        self.stench = False
        self.glitter = False
        
    def set_label(self, new_label):
        # takes in a new label and changes the old label to the new one
        self.label = new_label
    
    def is_start_spot(self):
        # the start spot is the spot in the lower left corner labeled with "s"
        if (self.label == "s" and self.xcoord == (self.wall_sizex - 1) and self.ycoord == 0):
            return True
        # if the Node is in the lower left corner (the starting spot) but not labeled "s", change the label
        if self.xcoord == (self.wall_sizex - 1) and self.ycoord == 0:
            self.set_label("s") 
            return True
        # if the node fits neither of the above things then the node cannot be the starting spot
        if self.label == "s": #if spot is incorrectly labeled, fix the label
            self.set_label("e")
        return False
    
    def next_to_right_wall(self):
        # if the node is next to the right wall, its y coordinate must be the farthest spot to the right
        return self.ycoord == self.wall_sizey - 1
    
    def next_to_left_wall(self):
        # if node is next to left wall then its y coordinate would be 0
        return self.ycoord == 0
    
    def next_to_upper_wall(self):
        #  if node is next to the upper wall then its x coordinate would be 0
        return self.xcoord == 0
    
    def next_to_lower_wall(self):
        # if node is next to the lower wall then its x coord must be the highest index
        return self.xcoord == self.wall_sizex - 1
    
    def is_corner_spot(self):
        # A node is in a corner if it is next to a vertical wall AND a horizontal wall
        if ((self.next_to_left_wall and self.next_to_upper_wall) or
            (self.next_to_left_wall and self.next_to_lower_wall) or
            (self.next_to_right_wall and self.next_to_upper_wall) or
            (self.next_to_right_wall and self.next_to_lower_wall)):
            return True
        # if it does not fit in the above statement then the node is not in a corner
        return False
    
    def is_empty(self):
        # this function assumes that any empty spot is labeled "e"
        return self.label == "e"
    
    def is_pit(self):
        # this function assumes that any spot with a pit is labeled "p"
        return self.label == "p"
    
    def is_wumpus(self):
        # this function assumes that any spot with a wumpus is labeled "w"
        return self.label == "w"
    
    def is_gold(self):
        # this function qssumes that any spot with gold is labeled "g"
        return self.label == "g"
    
    def is_notpit_marked(self):
        # not pit spots are marked "np"
        if self.np:
            return True
        if self.label == "np":
            self.np = True
            return True
        # else if no label or bool changed then it must be false
        return False
    
    def is_notwumpus_marked(self):
        # not wumpus spots are marked "nw"
        if self.nw:
            return True
        if self.label == "nw":
            self.nw = True
            return True
        #else if no label or no bool changed then it must be false
        return False
    
    def is_notgold_marked(self):
        # not gold spots are labeled "ng"
        if self.ng:
            return True
        if self.label == "ng":
            self.ng = True
            return True
        #else if no label or no bool changed then it must be false
        return False
    
    def marked_as_visited(self):
        # visited nodes are marked with a "v"
        if self.visited:
            return True
        if self.label == "v":
            self.visited = True
            return True
        #else if no label or no bool changed then it must be false
        return False
    
    def killw(self):
        """
        if the wumpus is shot and killed, that means the node's label must change from "w"/having a wumpus
        to "e" for it is now empty
        """
        
        if self.label == "w":
            self.set_label("e")
            self.nw = True
            self.np = True
        
    
    