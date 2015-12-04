'''
Name: Tetsing pvt/pub members of a class.

Author: Ranaji Krishna.


Notes:
(1) When we use from test_pub_pvt1 import *, the instance of a class is created using
a = test(). If we use import test_pub_pvt1, then the instance of a class is created using
a = test_pub_pvt1.test(). ALL OTHER FUNCTIONALITIES REMAIN THE SAME.

(2) A single underscore varible is a convention used to indicate that the variable is private. In python it is no different 
from a regular variable, i.e. it can be accessed from outside the class (eg. print a._var1). But it should be treated 
as private and should not be accessed from outside the object. 
** From Python Docs **
Private instance variables that cannot be accessed except from inside an object don't exist in Python. 
However, there is a convention that is followed by most Python code: a name prefixed with an underscore 
(e.g. _spam) should be treated as a non-public part of the API (whether it is a function, a method or a data member). 
It should be considered an implementation detail and subject to change without notice.

(3) A double underscore variable provides the capabilities of a private variable, i.e. it cannot be accessed from outside the 
object (eg. print a.__var2 does not work). However, name mangling can be used to access the variable from outside the object
by using object._classname__varname (eg. print a._test__var2). The properties of a private method is seen when inheritence is 
used. Since __methodPvt is private, the subclass 'child' of baseclass 'test' cannot override the variables of the method.
Therefore c.methodPvt yields the contents of methodPvt in the class test (and not the contents of methodPvt in the class child).
Similarly, c._test__methodPvt() yields the content of methodPvt in the class test. 
Note1: Name mangling has to be used here since methodPvt is a private method (i.e. a.__methodPvt() will not work).
Note2: It is bad practice to read contents of a method using this technique.
Note3: c._child__methodPvt won't work.

(4) Variables inside methods can be read using the same syntax as for those inside constructors (regardless of methods being public
or private). This means that name mangling has to be used for private variables (eg.a.__varPvt and a.__varPvtPub won't work). 
Moreover, if a variable inside a private method of a subclass does not appear in the respective method (private) 
of the baseclass, it cannot be read (eg. c._test__varNewPvt does not work; however c._varNewPub yields 2).
'''

import sys

#import test_pub_pvt1
from test_pub_pvt1 import *

def main(argv = None):

	# ===== Variables ====

	#a = test_pub_pvt1.test()
	a = test()
	# dir(a) 		# To get the members of the class.
	print a._var1		# 5
	#print a.__var2		# Will not work.
	print a._test__var2	# 10
	#a.printVar()		# 10

	a._var1 = 7
	print a._var1		# 7	 
	a.__var2 = 9		
	print a.__var2		# 9
	a._test__var2 = 11
	print a._test__var2	# 11

	#b = test_pub_pvt1.test()
	b = test()
	print b._var1		# 5  (and not 7)
	print b._test__var2	# 10 (and not 11)

	
	c = child()
	print c._var1		# 15  (and not 5)
	print c._child__var2	# 20 (and not 10)

	# ==== Methods ====
	a.methodPvt()		# I'm in pvt method of class test
	a.methodPub()		# I'm in pub method of class test
	c.methodPvt()		# I'm in pvt method of class test (and not "I'm in pvt method of class child")
	c.methodPub()		# I'm in pub method of class child

	# ---- Variables within methods ---
	print a._test__varPvt	 # 1
	print a._varPubPvt       # 1
	print a._varPub		 # 1
	print a._test__varPvtPub # 1 

	#print c._child__varPvt	# Error.
	#print c._varNewPvt	# Error
	print c._test__varPvt	# 1 (and not 2, because it inherits a pvt method from its parent class test)
	print c._varPubPvt	# 2
	print c._varNewPub	# 2

	# ==== Bad practice  ====
	print a._test__methodPvt()	# Im in pvt method of class test /n None 
	print a._methodPub()		# Im in pub method of class test /n None
	print c._test__methodPvt()	# Im in pvt method of class test /n None
	print c._methodPub()		# Im in pub method of class child /n None
	return(0)

if __name__ == '__main__':
	status = main()
	sys.exit(status)

