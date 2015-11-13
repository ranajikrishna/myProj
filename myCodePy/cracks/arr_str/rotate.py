'''
Name: Look for the unique character.

Author: Ranaji Krishna.

Notes:
Given an image represented by an NxN matrix, where each pixel in the image is 4 bytes, write a method to rotate the image by 90 degrees. Canyou do this in place?

'''

from myLib import *

def rotate(mat, n):

	for layer in range(0, n/2): # layer
		first = layer
		last = n - 1 - layer
		for  i in range(first, last):
			offset = i - first
			# save top  
			top = mat[first,i]

			# left -> top
		       	mat[first,i] = mat[last-offset,first]

			# bottom -> left
			mat[last-offset,first] = mat[last,last - offset]	

			# right -> bottom
			mat[last,last - offset] = mat[i,last]

			# top -> right
		      	mat[i,last] = top	

	return(mat)


def main(argv = None):

	mat = np.matrix([[1,2,3,4],[1,2,3,4],[1,2,3,4],[1,2,3,4]])
	res = rotate(mat,4)
	print(res)

	return(0)

if __name__ == '__main__':
	status = main()
	sys.exit(status)
