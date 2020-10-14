from observer import Observer
from AgentGame import *
import sys
sizex= 6
sizey= 6
pits= 2
diffy= 3
agentnumber=1
games=[]
if agentnumber>0:
    fname="agents" ## test case in this repo: agents 
    agentname="superagent" ## test case in this repo: agent1 or agent (please remove .py)
    sys.path.append(fname)
    cmd="import "+agentname+" as t1"
    exec(cmd)
    #import superagent as t1
    agent=t1.Agent(sizex,sizey)
    game1=AgentGame(sizex,sizey,pits,diffy,agent,o1=Observer())
    games.append(game1)



for i in range(1000):
    for game in games:
        game.step()
