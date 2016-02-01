
'''
Testing private/public members of a class

'''


class test(object):

	def __init__(self): 
		self._var1 = 5		 
		self.__var2 = 10 

	def printVar(self):
		print(self.__var2)

	def __methodPvt(self):
		self.__varPvt = 1
		self._varPubPvt = 1
		print "Im in pvt method of class test" # + `self.__var` 
	
	def methodPvt(self):
		self.__methodPvt()

	def _methodPub(self):
		self._varPub = 1
		self.__varPvtPub = 1
		print "Im in pub method of class test" # + `self._var`

	def methodPub(self):
		self._methodPub()

class child(test):

	def __init__(self):
		self._var1 = 15
		self.__var2 = 20

	def __methodPvt(self):
		self.__varPvt = 2
		self._varPubPvt = 2
		self._varNewPvt = 2
		print "I'm in pvt method of class child" #+ self.__var

	def _methodPub(self):
		self.__varPvtPub = 2
		self._varPubPvt = 2
		self._varNewPub = 2
		print "Im in pub method of class child"

	def method(self):
		self._methodPub()
