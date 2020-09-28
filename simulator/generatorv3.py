from MarkSolver import *
from nodeclass import *
import random


'''
randgrid will generator a random map which is not verified to be solvable
'''
def randgrid(sizex, sizey, pits):

    grid=list(list())
    # create 1 board without any stuff in it
    for i in range(sizex):
        line=list()
        grid.append(line)
        for j in range(sizey):
            grid[i].append(0)
            

    alreadyput=False
    # put in gold
    while(not alreadyput):
        x=random.randint(0,sizex-1)
        y=random.randint(0,sizey-1)
        if((x!=0 or y!=0)and grid[x][y]==0):
            grid[x][y]=3
            alreadyput=True

                
        
    alreadyput=False
    #put in wumpus;
    while(not alreadyput):
        x=random.randint(0,sizex-1)
        y=random.randint(0,sizey-1)
        if((x!=y or x!=0) and not(x==0 and y==1) and not(x==1 and y==0) and grid[x][y]==0):
            grid[x][y]=2
            alreadyput=True

        
    alreadyput=False
    #put in pits
    '''
    if(pits>=size*size-6){
            cerr<<"too many pits";
    return grid;
    }
    '''
    for num in range(pits):
        alreadyput=False
        while(not alreadyput):
            x=random.randint(0,sizex-1)
            y=random.randint(0,sizey-1)
            if((x!=y or x!=0) and not(x==0 and y==1) and not(x==1 and y==0)and grid[x][y]==0):
                grid[x][y]=1
                alreadyput=True

                        
                
    
    return grid






'''
print out the map, for debug purpose
'''
def printgrid(grid , sizex , sizey ):
    print("")
    for i in range(sizex):
        for j in range(sizey):
            print(grid[sizex-i-1][j],end="")
        print("")        
                
        
'''
findmap will find the map that is solvable
        //difficulty	-1 cantsolve
			//0 easy, which doesnt involve glitter check and shoot wumpus
			//1 medium, which involve glitter check
			//2 hard which involve shooting down the wumpus
			//3 extreme, which involve both shooting down the wumpus and glitter check
'''

def findmap(sizex,sizey,pits,diffy):
    
    grid=randgrid(sizex,sizey,pits)
    while(not marksolver(maptrans(grid),sizex,sizey) or not(diffy==evaluate(maptrans(grid),sizex,sizey))):
        grid=randgrid(sizex,sizey,pits)
    
    return grid


def tolistofset(themap,sizex,sizey):
    start_invis_board = [[set() for j in range(sizey)] for i in range(sizex)]
    for i in range(sizex):
        for j in range(sizey):
            if themap[i][j]==2:
                start_invis_board[i][j].add("LiveWumpus")
            if themap[i][j]==3:
                start_invis_board[i][j].add("Gold")
            if themap[i][j]==1:    
                start_invis_board[i][j].add("Pit")
    return start_invis_board    
    
    
if __name__ == "__main__":
    
    printgrid(findmap(4,4,3,3),4,4)
    printgrid(findmap(5,6,3,3),5,6)

'''
#srand(int(clock()*10000)); #must import sys up on top
#print(findmap(sizex,sizey,pits,diffy), sizex, sizey)
threadsnum = 1
sizex = input("Enter the horizontal board size:" )
while ((not sizex.isdigit()) or (int(sizex) < 1)):
	sizex = input("Invalid input. Please enter a positive integer horizontal size." )
sizex = int(sizex)

sizey = input("Enter the vertical board size:" )
while ((not sizey.isdigit()) or (int(sizey) < 1)):
	sizey = input("Invalid input. Please enter a positive integer vertical size." )
sizey = int(sizey)

pits = input("Enter the number of pits:" )
while ((not pits.isdigit()) or (int(pits) >= size * size - 6 )):
	if (not pits.isdigit()):
		pits = input("Invalid input. Please enter a positive integer number of pits." )
	else:
		pits = input("Too many pits. Please enter a lower number.")

pits = int(pits)

diffy = input("Enter the size:" )
while ((not (diffy.isdigit()) or (int(diffy) < -1 or int(diffy) > 3)):
	diffy = input("Invalid input. Please enter an integer from -1 to 3.")

diffy = int(diffy)

threadsnum = input("Enter 1-16 for the number of threads you want for the program to use:" )
while ((not (threadsnum.isdigit()) or (int(threadsnum) < 1 or int(threadsnum) > 16)):
	threadsnum = input("Invalid input. Please enter an integer between 1-16.")

threadsnum = int(threadsnum)


'''
'''
vector<thread> threads;
	for(int t=0;t<threadsnum;t++){
		threads.push_back(thread(findmap,t*t+1));
	}
	for(int t=0;t<threadsnum;t++){
		threads[t].join();
	}
	cout<<"Found difficulty: "<<diffy<<endl;
	printgrid(answer[0],size);
'''
      
