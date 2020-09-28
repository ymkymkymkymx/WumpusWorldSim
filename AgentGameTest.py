from observer import Observer
from AgentGame import *
import sys
sizex= int(input("Sizex: "))
sizey= int(input("Sizey: "))
pits= int(input("The number of pits: "))
diffy= int(input("The difficulty: "))
agentnumber=int(input("Number of Agents: "))
games=[]
if agentnumber>0:
    fname=input("Enter the folder name: ") ## test case in this repo: agents 
    agentname=input("Enter the agent name: ") ## test case in this repo: agent1 or agent (please remove .py)
    sys.path.append(fname)
    cmd="import "+agentname+" as t1"
    exec(cmd)
    agent=t1.Agent()
    game1=AgentGame(sizex,sizey,pits,diffy,agent,o1=Observer())
    games.append(game1)
if agentnumber>1:
    fname=input("Enter the folder name: ") ## test case in this repo: agents 
    agentname=input("Enter the agent name: ") ## test case in this repo: agent1 or agent (please remove .py)
    sys.path.append(fname)
    cmd="import "+agentname+" as t1"
    exec(cmd)
    agent=t1.Agent()    
    game2=AgentGame(sizex,sizey,pits,diffy,agent,o1=Observer())
    games.append(game2)
if agentnumber>2:
    fname=input("Enter the folder name: ") ## test case in this repo: agents 
    agentname=input("Enter the agent name: ") ## test case in this repo: agent1 or agent (please remove .py)
    sys.path.append(fname)
    cmd="import "+agentname+" as t1"
    exec(cmd)
    agent=t1.Agent()    
    game3=AgentGame(sizex,sizey,pits,diffy,agent,o1=Observer())
    games.append(game3)
if agentnumber>3:
    fname=input("Enter the folder name: ") ## test case in this repo: agents 
    agentname=input("Enter the agent name: ") ## test case in this repo: agent1 or agent (please remove .py)
    sys.path.append(fname)
    cmd="import "+agentname+" as t1"
    exec(cmd)
    agent=t1.Agent()    
    game4=AgentGame(sizex,sizey,pits,diffy,agent,o1=Observer())
    games.append(game4)
if agentnumber>4:
    fname=input("Enter the folder name: ") ## test case in this repo: agents 
    agentname=input("Enter the agent name: ") ## test case in this repo: agent1 or agent (please remove .py)
    sys.path.append(fname)
    cmd="import "+agentname+" as t1"
    exec(cmd)
    agent=t1.Agent()    
    game5=AgentGame(sizex,sizey,pits,diffy,agent,o1=Observer())
    games.append(game5)
    
if agentnumber>5:
    fname=input("Enter the folder name: ") ## test case in this repo: agents 
    agentname=input("Enter the agent name: ") ## test case in this repo: agent1 or agent (please remove .py)
    sys.path.append(fname)
    cmd="import "+agentname+" as t1"
    exec(cmd)
    agent=t1.Agent()    
    game6=AgentGame(sizex,sizey,pits,diffy,agent,o1=Observer())
    games.append(game6)
if agentnumber>6:
    fname=input("Enter the folder name: ") ## test case in this repo: agents 
    agentname=input("Enter the agent name: ") ## test case in this repo: agent1 or agent (please remove .py)
    sys.path.append(fname)
    cmd="import "+agentname+" as t1"
    exec(cmd)
    agent=t1.Agent()    
    game7=AgentGame(sizex,sizey,pits,diffy,agent,o1=Observer())
    games.append(game7)
if agentnumber>7:
    fname=input("Enter the folder name: ") ## test case in this repo: agents
    agentname=input("Enter the agent name: ") ## test case in this repo: agent1 or agent (please remove .py)
    sys.path.append(fname)
    cmd="import "+agentname+" as t1"
    exec(cmd)
    agent=t1.Agent()    
    game8=AgentGame(sizex,sizey,pits,diffy,agent,o1=Observer())
    games.append(game8)
    agentnumber=8

for i in range(100):
    for game in games:
        game.step()
