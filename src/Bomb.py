import time
from Board import Board

class Bomb(object):

	def __init__(self, posx, posy, time, board):
		self.posx=posx
		self.posy=posy
		self.time=time
		self.board=board

	def getMatrix(self):
		self.matrix=[]
		self.matrix.append(["\033[0;34m[", "\033[0;34m"+str(3+self.time-round(time.time())), "\033[0;34m"+str(3+self.time-round(time.time())), "\033[0;34m]"])
		self.matrix.append(["\033[0;34m[", "\033[0;34m"+str(3+self.time-round(time.time())), "\033[0;34m"+str(3+self.time-round(time.time())), "\033[0;34m]"])
		return self.matrix

	def update(self):
		self.board.edit(self.posx, self.posy, self)
		if self.time-round(time.time())==-3:
			self.explode()

	def explode(self):
		for i in range(self.posx, self.posx+2):
			for j in range(self.posy-4, self.posy+8):
				if self.board.matrix[i][j]!="#":
					self.board.matrix[i][j]="B"
					if self.board.matrix[i][j]=="\033[0;32m/":
						self.board.matrix[i][j]=" "

		for i in range(self.posx-2, self.posx+4):
			for j in range(self.posy, self.posy+4):
				if self.board.matrix[i][j]!="#":
					self.board.matrix[i][j]="B"
					if self.board.matrix[i][j]=="\033[0;32m/":
						self.board.matrix[i][j]=" "