'''
Name: Super Class Inheritence. 

Link: http://learnpythonthehardway.org/book/ex44.html#video

'''
import sys

class Parent(object):

    def override(self):
        print "PARENT override()"

    def implicit(self):
        print "PARENT implicit()"

    def altered(self):
        print "PARENT altered()"

class Child(Parent):

    def override(self):
        print "CHILD override()"

    def altered(self):
        print "CHILD, BEFORE PARENT altered()"
        super(Child, self).altered()
        print "CHILD, AFTER PARENT altered()"


def main (argv = None):
	
	dad = Parent()
	son = Child()

	dad.implicit()
	son.implicit()

	dad.override()
	son.override()

	dad.altered()
	son.altered()

	return(0)

if __name__ == '__main__':
	status = main()
	sys.exit(status)
