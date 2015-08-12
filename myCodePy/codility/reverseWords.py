

def solution(S):

	N = len(S)

	if (N == 1):
		return (0)
	elif (N % 2 == 0):
		return(-1)
	else:
		mid = N//2
		for i in range(1, mid+1):
			if(S[mid - i] != S[mid + i]):
				return(-1)
			else: pass
	return(mid)
		
def main(argv=None):

#n = solution("carerac")
	n = solution("x")
	print(n)
	return(0)



if __name__ == '__main__':
    status = main()
    sys.exit(status)
