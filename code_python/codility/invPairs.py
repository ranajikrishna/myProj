

def solution(A):
	MAX_INV = 1,000,000,000
	N = len (A)
	inv = 0
	for i in range(N-1,-1,-1):
		j = 0
		while (j < i):
			if (A[j] > A[i]):
				inv += 1
				if (inv == MAX_INV): return(-1)
			j += 1

	return(inv)

def main(argv=None):
	num = [-1,6,3,4,7,4]
#num = [-1,-1,-1]
	n = solution(num)
	print(n)
	return(0)



if __name__ == '__main__':
    status = main()
    sys.exit(status)
