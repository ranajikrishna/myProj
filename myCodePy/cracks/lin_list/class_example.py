'''
Name: Example of a class.

Author: Ranaji Krishna.

Notes:

'''


from myLib import *

class Human(object):

	# Consructor
	def __init__(self, name, gender):
		self.myName = name
		self.myGen = gender
	# Methods
	def hobbies(self, hobby):
		myHobby = hobby

	def performTask(self, *args):
		print add(*args)

# Fuctions
def add(a, b):
	return(a + b)

def main(argv = None):

	per = Human("Ra","M")
	per.performTask(3,4)

	print per.myName
	return(0)


if __name__ == '__main__':
	status = main()
	sys.exit(status)
