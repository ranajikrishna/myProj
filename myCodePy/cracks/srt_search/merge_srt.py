
'''
Name: Sort and merge.

Author: Ranaji Krishna.

Notes:You are given two sorted arrays, A and B, where A has a large enough buffer at the
end to hold B.Write a method to merge B into A in sorted order. 
'''

from myLib import *


def merge_srt(tmp, B):

	index_A = len(tmp) - 1
	index_B = len(B) - 1
	mer_ind = index_A + index_B + 1

	A = np.sort(np.zeros(len(tmp) + len(B)))
	A[0:len(tmp)] = tmp
	
	while(index_A >= 0 and index_B >= 0):
		if (A[index_A] < B[index_B]):
			A[mer_ind] = B[index_B]
			index_B = index_B - 1
			mer_ind = mer_ind - 1
		else:
			A[mer_ind] = A[index_A]
			mer_ind = mer_ind - 1
			index_A = index_A - 1
	if(index_B > 0):
		A[0:mer_ind+1] = B[0:index_B+1]
	
#	while(index_B>=0):
#		A[mer_ind]= B[index_B]
#		mer_ind = mer_ind-1
#		index_B = index_B - 1

	return(A)

def main(argv = None):


	A = np.sort(np.random.randint(0, 100, 10))
	B = np.sort(np.random.randint(0, 100, 7))
	
	print(merge_srt(A, B))


	return(0)


if __name__ == '__main__':
	status = main()
	sys.exit(status)




