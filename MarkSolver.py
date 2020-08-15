from nodeclass import *
def checkgold(gamestate, mapsizex, mapsizey):
	for i in range(mapsizex):
		for j in range(mapsizey):
			if(gamestate[i][j].visited == False and gamestate[i][j].is_gold()==True):
				return False
	return True

#check this function
def checkglitter(gamestate, mapsizex, mapsizey):
	count = 0
	goldnear = False
	for i in range(mapsizex):
		for j in range(mapsizey):
			if(gamestate[i][j].ng == False):
				count = count + 1
			if(gamestate[i][j].is_gold()):
				if(i+1<mapsizex and gamestate[i+1][j].visited):
					goldnear = True
				if(j+1<mapsizey and gamestate[i][j+1].visited):
					goldnear = True
				if(i-1>=0 and gamestate[i-1][j].visited):
					goldnear = True
				if(j-1>=0 and gamestate[i][j-1].visited):
					goldnear = True
	if(goldnear and count==1):
		return True
	return False


def countposwnum(gamestate, mapsizex, mapsizey):
	count = 0
	for i in range(mapsizex):
		for j in range(mapsizey):
			if (gamestate[i][j].nw == False):
				count = count + 1
	return count




def expandbyrule(gamestate, mapsizex, mapsizey):
	expanding = True
	
	while(expanding):
		expanding=False
		for i in range(mapsizex):
			for j in range(mapsizey):
				if(gamestate[i][j].visited==False and gamestate[i][j].nw==True and gamestate[i][j].np==True):
					gamestate[i][j].visited=True
					expanding=True
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

					
	return gamestate


def marksolver( theboard, mapsizex, mapsizey ):
	'''initialize the game'''
	
	gamestate=theboard.copy()
	i=0
	j=0
	gamestate[i][j].visited=True
	
	gamestate[i][j].nw=True
	gamestate[i][j].np=True
	
	if (gamestate[i][j].breeze and gamestate[i][j].stench):
		for x in range(mapsizex):
			for y in range(mapsizey) :
				if(not ((x==i+1 and y==j)or(x==i-1 and y==j)or(x==i and y==j+1)or(x==i and y==j-1)) ) :
					gamestate[x][y].nw=True
	
	elif(gamestate[i][j].stench):
		for x in range(mapsizex):
			for y in range(mapsizey):
				if(not((x==i+1 and y==j)or(x==i-1 and y==j)or(x==i and y==j+1)or(x==i and y==j-1)) ) :
					gamestate[x][y].nw=True
				
			
		
		if(i+1<mapsizex): gamestate[i+1][j].np=True
		if(j+1<mapsizey): gamestate[i][j+1].np=True
		if(i-1>=0): gamestate[i-1][j].np=True
		if(j-1>=0): gamestate[i][j-1].np=True
	
	
	elif(gamestate[i][j].breeze):
		if(i+1<mapsizex): gamestate[i+1][j].nw=True
		if(j+1<mapsizey): gamestate[i][j+1].nw=True
		if(i-1>=0): gamestate[i-1][j].nw=True
		if(j-1>=0): gamestate[i][j-1].nw=True
	
	else:
		if(i+1<mapsizex): gamestate[i+1][j].np=True
		if(j+1<mapsizey): gamestate[i][j+1].np=True
		if(i-1>=0): gamestate[i-1][j].np=True
		if(j-1>=0): gamestate[i][j-1].np=True
		if(i+1<mapsizex): gamestate[i+1][j].nw=True
		if(j+1<mapsizey): gamestate[i][j+1].nw=True
		if(i-1>=0): gamestate[i-1][j].nw=True
		if(j-1>=0): gamestate[i][j-1].nw=True
	
	
	''' first round of expanding, before try to shoot the wumpus.'''
	beforeshooting=expandbyrule(gamestate,mapsizex,mapsizey)
	''' if gold already reached, just return true '''
	if(checkgold(beforeshooting,mapsizex,mapsizey)): return true
	if(checkglitter(beforeshooting,mapsizex,mapsizey)): return true
	'''shoot the wumpus down if it is possible'''
	wnumber=countposwnum( beforeshooting, mapsizex,mapsizey)
	'''only one possible place for wumpus'''
	if(wnumber==1):
		
		x=0
		y=0
		
		for i in range(mapsizex):
			for j in range(mapsizey):
				if (beforeshooting[i][j].nw==false):
					x=i
					y=j
			
		if beforeshooting[x][y].is_wumpus():
			beforeshooting[x][y].nw=true
			beforeshooting[x][y].np=true
			for a in range(mapsizex):
				for b in range(mapsizey):
					beforeshooting[a][b].stench=false
				
			
		
		else:
			beforeshooting[x][y].nw=true
		
		beforeshooting[x][y].killw()
		
		aftershooting=expandbyrule(beforeshooting,mapsizex,mapsizey)
		
		if(checkgold(aftershooting,mapsizex,mapsizey)): return true
		if(checkglitter(aftershooting,mapsizex,mapsizey)): return true
	
	
	
	
	return false




''' 
The assembled main function which takes in a board and return the difficulty
	@param theboard  It is the game board the generator generated
	@param mapsize  It is n for an n*n board, we assume that all the boards are in shape of n*n.
	@return -1 cantsolve
			0 easy, which doesnt involve glitter check and shoot wumpus
			1 medium, which involve glitter check
			2 hard which involve shooting down the wumpus
			3 extreme, which involve both shooting down the wumpus and glitter check
'''

def marksolver( theboard, mapsizex, mapsizey ):
	'''initialize the game'''
	
	gamestate=theboard.copy()
	i=0
	j=0
	gamestate[i][j].visited=True
	
	gamestate[i][j].nw=True
	gamestate[i][j].np=True
	
	if (gamestate[i][j].breeze and gamestate[i][j].stench):
		for x in range(mapsizex):
			for y in range(mapsizey) :
				if(not ((x==i+1 and y==j)or(x==i-1 and y==j)or(x==i and y==j+1)or(x==i and y==j-1)) ) :
					gamestate[x][y].nw=True
	
	elif(gamestate[i][j].stench):
		for x in range(mapsizex):
			for y in range(mapsizey):
				if(not((x==i+1 and y==j)or(x==i-1 and y==j)or(x==i and y==j+1)or(x==i and y==j-1)) ) :
					gamestate[x][y].nw=True
				
			
		
		if(i+1<mapsizex): gamestate[i+1][j].np=True
		if(j+1<mapsizey): gamestate[i][j+1].np=True
		if(i-1>=0): gamestate[i-1][j].np=True
		if(j-1>=0): gamestate[i][j-1].np=True
	
	
	elif(gamestate[i][j].breeze):
		if(i+1<mapsizex): gamestate[i+1][j].nw=True
		if(j+1<mapsizey): gamestate[i][j+1].nw=True
		if(i-1>=0): gamestate[i-1][j].nw=True
		if(j-1>=0): gamestate[i][j-1].nw=True
	
	else:
		if(i+1<mapsizex): gamestate[i+1][j].np=True
		if(j+1<mapsizey): gamestate[i][j+1].np=True
		if(i-1>=0): gamestate[i-1][j].np=True
		if(j-1>=0): gamestate[i][j-1].np=True
		if(i+1<mapsizex): gamestate[i+1][j].nw=True
		if(j+1<mapsizey): gamestate[i][j+1].nw=True
		if(i-1>=0): gamestate[i-1][j].nw=True
		if(j-1>=0): gamestate[i][j-1].nw=True
	
	
	''' first round of expanding, before try to shoot the wumpus.'''
	beforeshooting=expandbyrule(gamestate,mapsizex,mapsizey)
	''' if gold already reached, just return true '''
	if(checkgold(beforeshooting,mapsizex,mapsizey)): return 0
	if(checkglitter(beforeshooting,mapsizex,mapsizey)): return 1
	'''shoot the wumpus down if it is possible'''
	wnumber=countposwnum( beforeshooting, mapsizex,mapsizey)
	'''only one possible place for wumpus'''
	if(wnumber==1):
		
		x=0
		y=0
		
		for i in range(mapsizex):
			for j in range(mapsizey):
				if (beforeshooting[i][j].nw==false):
					x=i
					y=j
			
		if beforeshooting[x][y].is_wumpus():
			beforeshooting[x][y].nw=true
			beforeshooting[x][y].np=true
			for a in range(mapsizex):
				for b in range(mapsizey):
					beforeshooting[a][b].stench=false
				
			
		
		else:
			beforeshooting[x][y].nw=true
		
		beforeshooting[x][y].killw()
		
		aftershooting=expandbyrule(beforeshooting,mapsizex,mapsizey)
		
		if(checkgold(aftershooting,mapsizex,mapsizey)): return 2
		if(checkglitter(aftershooting,mapsizex,mapsizey)): return 3
	
	return -1