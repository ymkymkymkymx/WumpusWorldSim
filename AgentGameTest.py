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
    agent=t1.Agent(sizex,sizey)
    game1=AgentGame(sizex,sizey,pits,diffy,agent,o1=Observer())
    games.append(game1)
if agentnumber>1:
    fname=input("Enter the folder name: ") ## test case in this repo: agents 
    agentname=input("Enter the agent name: ") ## test case in this repo: agent1 or agent (please remove .py)
    sys.path.append(fname)
    cmd="import "+agentname+" as t2"
    exec(cmd)
    agent2=t2.Agent(sizex,sizey)    
    game2=AgentGame(sizex,sizey,pits,diffy,agent2,o1=Observer())
    games.append(game2)
if agentnumber>2:
    fname=input("Enter the folder name: ") ## test case in this repo: agents 
    agentname=input("Enter the agent name: ") ## test case in this repo: agent1 or agent (please remove .py)
    sys.path.append(fname)
    cmd="import "+agentname+" as t3"
    exec(cmd)
    agent3=t3.Agent(sizex,sizey)    
    game3=AgentGame(sizex,sizey,pits,diffy,agent3,o1=Observer())
    games.append(game3)
if agentnumber>3:
    fname=input("Enter the folder name: ") ## test case in this repo: agents 
    agentname=input("Enter the agent name: ") ## test case in this repo: agent1 or agent (please remove .py)
    sys.path.append(fname)
    cmd="import "+agentname+" as t4"
    exec(cmd)
    agent4=t4.Agent(sizex,sizey)    
    game4=AgentGame(sizex,sizey,pits,diffy,agent4,o1=Observer())
    games.append(game4)
if agentnumber>4:
    fname=input("Enter the folder name: ") ## test case in this repo: agents 
    agentname=input("Enter the agent name: ") ## test case in this repo: agent1 or agent (please remove .py)
    sys.path.append(fname)
    cmd="import "+agentname+" as t5"
    exec(cmd)
    agent5=t5.Agent(sizex,sizey)    
    game5=AgentGame(sizex,sizey,pits,diffy,agent5,o1=Observer())
    games.append(game5)
    


for i in range(100):
    for game in games:
        game.step()
