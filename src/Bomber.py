from Persons import Person 
from Board import Board
from Bomb import Bomb
import sys
import time

class Bomber(Person):
	xspeed=1
	yspeed=1

	def __init__(self, posx, posy, board, score):
		Person.__init__(self, "Bomber")
		self.posx=posx
		self.posy=posy
		self.bomb_num=1
		self.board=board
		self.score=0
		self.lives=3

	def getMatrix(self):
		"""Returns a lofl"""
		self.matrix=[]
		self.matrix.append(["\033[0;33m[", "\033[0;33m^", "\033[0;33m^", "\033[0;33m]"])
		self.matrix.append([" ", "\033[0;33m]", "\033[0;33m[", " "])
		return self.matrix
	
	def erase(self):
		for i in range(0, 2):
			for j in range(0, 4):
				self.board.matrix[self.posx+i][self.posy+j]=" "

	def checkCollision(self, keypressed):
		x=self.posx
		y=self.posy
		if keypressed=="w":
			x-=self.xspeed
		elif keypressed=="s":
			x+=self.xspeed
		elif keypressed=="a":
			y-=self.yspeed
		elif keypressed=="d":
			y+=self.yspeed
		for i in range(0, 2):
			for j in range(0, 4):
				newPos=self.board.matrix[x+i][y+j]
				if newPos == "\033[0;32m#" or newPos == "\033[0;32m/":
					return True
		
		for i in range(0, 2):
			for j in range(0, 4):
				newPos=self.board.matrix[x+i][y+j]
				if newPos == "B" or newPos == "\033[0;31m{" or newPos == "\033[0;31m}" or newPos == "\033[0;31m.":
					self.die()
	
	def move(self, keypressed):
		if keypressed=="w":
			if not(self.checkCollision(keypressed)):
				self.erase()
				self.posx-=self.xspeed
		elif keypressed=="s":
			if not(self.checkCollision(keypressed)):
				self.erase()
				self.posx+=self.xspeed
		elif keypressed=="a":
			if not(self.checkCollision(keypressed)):
				self.erase()
				self.posy-=self.yspeed
		elif keypressed=="d":
			if not(self.checkCollision(keypressed)):
				self.erase()
				self.posy+=self.yspeed
		elif keypressed=="b":
			self.dropBomb()
		elif keypressed=="q":
			print("You quit the game")
			sys.exit(0)
		self.board.edit(self.posx, self.posy, self)

	def dropBomb(self):
		if self.bomb_num==1:
			self.bomb=Bomb(self.posx, self.posy, round(time.time()), self.board)
			self.bomb_num-=1

	def bomb_update(self):
		if self.bomb_num==0:
			self.bomb.update()
			if self.bomb.time-round(time.time())==-4:
				
				for i in range(self.bomb.posx, self.bomb.posx+2):
					for j in range(self.bomb.posy-4, self.bomb.posy+8):
						if self.board.matrix[i][j]!="#":
							self.board.matrix[i][j]=" "

				for i in range(self.bomb.posx-2, self.bomb.posx+4):
					for j in range(self.bomb.posy, self.bomb.posy+4):
						if self.board.matrix[i][j]!="#":
							self.board.matrix[i][j]=" "

				self.bomb_num=1

		# print(self.board.wallpos)

		# for i in range(0, self.board.noOfWalls):
		# 	for j in range(0, 2):
		# 		for k in range(0, 4):
		# 			if self.board.matrix[(self.board.wallpos[i][1])+j][(self.board.wallpos[i][0])+k]=="B":
		# 				self.board.wallpos.remove(self.board.wallpos[i])
		# 				self.score+=20

	def die(self):
		if self.lives==1:
			print("You died")
			sys.exit(0)
		else:
			isdead=True
			self.lives-=1