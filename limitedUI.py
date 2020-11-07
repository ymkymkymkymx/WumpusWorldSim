from tkinter import *
import Single_agent_window_setmap as sagentmap
import sys

class Board:
    def __init__(self, difficulty="EASY", pits=1, rows=3, cols=3):
        self.difficulty = difficulty
        self.pits = pits
        self.gridX = rows
        self.gridY = cols
        self.diffy=0
board=Board()
root = Tk()
canvas = Canvas(root)
temp_new = Toplevel(canvas)
fname="agents"
agentname=input("Enter the agent name: ") ## test case in this repo: agent1 or agent (please remove .py)
sys.path.append(fname)
cmd="import "+agentname+" as agentclass"
exec(cmd)
maptxt=input("Enter the map as a list: 0=empty,1=pit,2=wumpus,3=gold\n")
cmd="themap="+maptxt
loc = {}
glb={} 
exec(cmd,glb,loc)
themap=loc['themap']
sagentmap.Single_agent_window(temp_new, board,agentclass,themap)
root.quit()
root.mainloop()