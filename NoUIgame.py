from observer0 import Observer
from AgentGame import *
import sys
fname="agents"
agentname=input("Enter the agent name: ") ## test case in this repo: agent1 or agent (please remove .py)
sys.path.append(fname)
cmd="import "+agentname+" as t1"
exec(cmd)
maptxt=input("Enter the map as a list: 0=empty,1=pit,2=wumpus,3=gold\n")
cmd="themap="+maptxt
loc = {}
glb={} 
exec(cmd,glb,loc)
themap=loc['themap']
sizex=len(themap)
sizey=len(themap[0])
games=[]
agent=t1.Agent(sizex,sizey)
game1=AgentGame(sizex,sizey,0,0,agent,o1=Observer())
game1.setboard(themap)
games.append(game1)



for i in range(1000):
    for game in games:
        game.step()
