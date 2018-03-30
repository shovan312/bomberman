class Person(object):

	def __init__(self, type):
		self.type=type

	def getType(self):
		return self.type

	def __str__(self):
		return "It is a %s" %(self.type)