from Persons import Person 
from Bomber import Bomber
import random

class Enemy(Person):

	def __init__(self, posx, posy, board, bomber):
		Person.__init__(self, "Enemy")
		self.posx=posx
		self.posy=posy
		self.board=board
		self.isDead=False
		self.bomber=bomber

	def getMatrix(self):
		"""Returns a lofl"""
		if not self.isDead:
			self.matrix=[]
			self.matrix.append(["\033[0;31m{", "\033[0;31m.", "\033[0;31m.", "\033[0;31m}"])
			self.matrix.append([" ", "\033[0;31m}", "\033[0;31m{", " "])
			return self.matrix
		else:
			self.matrix=[]
			self.matrix.append([" ", " ", " ", " "])
			self.matrix.append([" ", " ", " ", " "])
			return self.matrix

	def erase(self):
		for i in range(0, 2):
			for j in range(0, 4):
				self.board.matrix[self.posx+i][self.posy+j]=" "

	def checkCollision(self, prob):
		x=self.posx
		y=self.posy
		if prob<=0.25:
			x-=1
		elif prob>0.25 and prob<=0.5:
			x+=1
		elif prob>0.5 and prob<=0.75:
			y-=1
		elif prob>0.75:
			y+=1

		for i in range(0, 2):
			for j in range(0, 4):
				newPos=self.board.matrix[x+i][y+j]
				if newPos == "\033[0;32m#" or newPos == "\033[0;32m/":
					return True

		for i in range(0, 2):
			for j in range(0, 4):
				newPos=self.board.matrix[x+i][y+j]
				if newPos == "B":
					self.die()

	def move(self):
		if not self.isDead:
			prob=random.random()
			if prob<=0.25:
				self.erase()
				if not(self.checkCollision(prob)):
					self.posx-=1
			elif prob>0.25 and prob<=0.5:
				self.erase()
				if not(self.checkCollision(prob)):
					self.posx+=1
			elif prob>0.5 and prob<=0.75:
				self.erase()
				if not(self.checkCollision(prob)):
					self.posy-=1
			elif prob>0.75:
				self.erase()
				if not(self.checkCollision(prob)):
					self.posy+=1	

	def die(self):
		self.bomber.score+=100
		self.isDead=True			 