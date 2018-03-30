import random
import math

class Board(object):
	
	def __init__(self, rows, columns, matrix):
		self.rows=rows
		self.columns=columns
		self.matrix=matrix
		self.noOfWalls=30
		self.wallpos=[]
	
	def getBoard(self): 
		"""Returns a string."""
		columns=self.columns
		rows=self.rows
		board=[]
		
		for i in range(0, columns):
		    row=[]
		    for j in range(0, rows):
		        row.append(" ")
		    self.matrix.append(row)

		for i in self.wallpos:
			for j in range(0, 2):
				for k in range(0, 4):
					self.matrix[i[1]+j][i[0]+k]="\033[0;32m/"

		for i in range(0, 2):
		    for j in range(0, rows):
		        self.matrix[i][j]="\033[0;32m#"
		        self.matrix[-i-1][j]="\033[0;32m#"

		for i in range(2, columns-1):
		    for j in range(0, 4):
		        self.matrix[i][j]="\033[0;32m#"
		        self.matrix[i][-j-1]="\033[0;32m#"

		for i in range(4, self.rows-4):
			for j in range(2, self.columns-2):
				if not((i//4)%2):
					if not((j//2)%2):
						self.matrix[j][i]="\033[0;32m#"
						
		for i in range(0, columns):
			board.append(''.join(str(e) for e in self.matrix[i]))
		str1='\n'.join(str(e) for e in board)
		return str1
		
	def makeWall(self):
		for i in range(0, self.noOfWalls):
			xbrick=math.floor(random.random()*15)*4
			ybrick=math.floor(random.random()*15)*2
			if (xbrick>=4 and xbrick<=64) and (ybrick>=4 and ybrick<=32): 
				self.wallpos.append([xbrick, ybrick])

	def edit(self, x, y, type_object):
		for i in range(0, 2):
			for j in range(0, 4):
				self.matrix[x+i][y+j]=type_object.getMatrix()[i][j]
