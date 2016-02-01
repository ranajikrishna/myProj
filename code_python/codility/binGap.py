
from math import *

def solution(N):

	bit = tuple(bin(N)[2:])
	ind = []
	j = 0
	k = 0
	for i in bit:
		if (i != '0'):
			ind.append(k) 
			k = -1
			j += 1
		k += 1
	if (ind == []):
		return(0)
	else:
		return(max(ind))


def main(argv=None):
	num = 529
	n = solution(num)
	print(n)
	return(0)



if __name__ == '__main__':
    status = main()
    sys.exit(status)
