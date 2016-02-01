
'''
Name: Arrange anagram.

Author: Ranaji Krishna.

Notes:
Given a sorted array of n integers that has been rotated an unknown number of times, write code to find an element in the array. You may assume that the array was originally sorted in increasing order.


'''


from myLib import * 

def find_elmt(A, left, right, tgt):

	mid = (left + right)/2
	if (A[mid] == tgt):
		return(mid)
	if (right < left):
		return -1

	if (A[left] < A[mid]):
		if (A[left] <= tgt and A[mid] >= tgt):
			return find_elmt(A, left, mid - 1, tgt)
		else:
			return find_elmt(A, mid + 1, right, tgt)
	
	elif (A[mid] < A[left]):
		if (A[mid] <= tgt and tgt <= A[right]):
			return find_elmt(A, mid + 1, right, tgt)
		else:
			return find_elmt(A, left, mid - 1, tgt)
	
	elif (A[mid] == A[left]):
		if (A[mid] != A[right]):
			return find_elmt(A, mid + 1, right, tgt)
		else:
			result = find_elmt(A, left, mid - 1, tgt)
			if (result == -1):
				return find_elmt(A, mid + 1, right, tgt)
			else:
				return result
	return -1			

def main(argv = None):

	tmp = np.sort(np.random.randint(0, 20, 18))	
	A = np.sort(np.random.randint(21, 40, 10))	
	A = np.concatenate((A,tmp),axis=0)

	tgt = A[7]
	print(find_elmt(A, 0, len(A)-1, tgt))



	return(0)


if __name__ == '__main__':
	status = main()
	sys.exit(status)
