def checkgold(gamestate, mapsize):
	for i in range(mapsize):
		for j in range(mapsize):
			if(gamestate[i][j].visited == False and gamestate[i][j].is_gold()==True):
				return False
	return True

#check this function
def checkglitter(gamestate, mapsize):
	count = 0
	goldnear = False
	for i in range(mapsize):
		for j in range(mapsize):
			if(gamestate[i][j].ng == False):
				count = count + 1
			if(gamestate[i][j].is_gold()):
				if(i+1<mapsize and gamestate[i+1][j].visited):
					goldnear = True
				if(j+1<mapsize and gamestate[i][j+1].visited):
					goldnear = True
				if(i-1>=0 and gamestate[i-1][j].visited):
					goldnear = True
				if(j-1>=0 and gamestate[i][j-1].visited):
					goldnear = True
	if(goldnear and count==1):
		return True
	return False


def countposwnum(gamestate, mapsize):
	count = 0
	for i in range(mapsize):
		for j in range(mapsize):
			if (gamestate[i][j].nw == False):
				count = count + 1
	return count




def expandbyrule(gamestate, mapsize):
	expanding = True
	
	while(expanding):
		expanding=False
		for i in range(mapsize):
			for j in range(mapsize):
				if(gamestate[i][j].visited==False and gamestate[i][j].nw==True and gamestate[i][j].np==True):
					gamestate[i][j].visited=True
					expanding=True
					if (gamestate[i][j].breeze and gamestate[i][j].stench):
						for x in range(mapsize):
							for y in range(mapsize):
								if(not ((x==i+1 and y==j) or (x==i-1 and y==j) or (x==i and y==j+1) or (x==i and y==j-1))):
									gamestate[x][y].nw=True		
	
					elif(gamestate[i][j].stench):
						for x in range(mapsize):
							for y in range(mapsize):
								if(not ((x==i+1 and y==j) or (x==i-1 and y==j) or (x==i and y==j+1) or (x==i and y==j-1))):
									gamestate[x][y].nw=True

						if(i+1<mapsize):
							gamestate[i+1][j].np=True
						if(j+1<mapsize):
							gamestate[i][j+1].np=True
						if(i-1>=0):
							gamestate[i-1][j].np=True
						if(j-1>=0):
							gamestate[i][j-1].np=True
	
					elif(gamestate[i][j].breeze):
						if(i+1<mapsize):
							gamestate[i+1][j].nw=True
						if(j+1<mapsize):
							gamestate[i][j+1].nw=True
						if(i-1>=0):
							gamestate[i-1][j].nw=True
						if(j-1>=0):
							gamestate[i][j-1].nw=True
						
					else:
						if(i+1<mapsize):
							gamestate[i+1][j].np=True
						if(j+1<mapsize):
							gamestate[i][j+1].np=True
						if(i-1>=0):
							gamestate[i-1][j].np=True
						if(j-1>=0):
							gamestate[i][j-1].np=True
						if(i+1<mapsize):
							gamestate[i+1][j].nw=True
						if(j+1<mapsize):
							gamestate[i][j+1].nw=True
						if(i-1>=0):
							gamestate[i-1][j].nw=True
						if(j-1>=0):
							gamestate[i][j-1].nw=True
						
				if(gamestate[i][j].glitter):
					for x in range(mapsize):
						for y in range(mapsize):
							if(not ((x==i+1 and y==j) or (x==i-1 and y==j) or (x==i and y==j+1) or (x==i and y==j-1))):
								gamestate[x][y].ng=True
								
				else:
					if(i+1<mapsize):
						gamestate[i+1][j].ng=True
					if(j+1<mapsize):
						gamestate[i][j+1].ng=True
					if(i-1>=0):
						gamestate[i-1][j].ng=True
					if(j-1>=0):
						gamestate[i][j-1].ng=True

				if(testing):
					print()
					for i in range(mapsize):
						for j in range(mapsize):
							if (gamestate[i][j].nw==False):
								print("0", end = "")
				
							else:
								print("1", end = "")		
						print()
						
	return gamestate
