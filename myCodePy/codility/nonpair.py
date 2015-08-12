

def solution(A):
	i = 0
	while (len(A) != 1):
		j = 1
		while (j < len(A)):
			if A[i] == A[j]:
				A.remove(A[i])
				A.remove(A[j-1])
				solution(A)
				i = 0
				j = 0
			j += 1
		return(A[i])
			

	return(A[0])
		
def main(argv=None):
	num = [9,3,9,3,9,7,9]
	num = [9,3,9,3,9,7,9,8,8,4,4]
	n = solution(num)
	print(n)
	return(0)



if __name__ == '__main__':
    status = main()
    sys.exit(status)
