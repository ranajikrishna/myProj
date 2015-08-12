

def solution(S,K):

	if(S=='r'):
		if(K ==1):
			return('r')

	S_new = S.replace("-","")
	S = S_new.upper()


	N = len(S)
	pos = N - K
	
	while (K < N):
		S = S[:pos] + '-' + S[pos:]
		N = pos
		pos = N - K

	return(S)


def main(argv=None):
	num = '2-4A0r7-4k'
	num = 'r'
#num = [-1,-1,-1]
	n = solution(num,1)
	print(n)
	return(0)



if __name__ == '__main__':
    status = main()
    sys.exit(status)
