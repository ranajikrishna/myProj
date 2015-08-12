

from math import sqrt

def boundedSlicesGolden(K, A):
	N = len(A)
	maxINT = 2000000000

	maxQ = [0] * (N + 1)
	posmaxQ = [0] * (N + 1)
	minQ = [0] * (N + 1)
	posminQ = [0] * (N + 1)

	firstMax, lastMax = 0, -1
	firstMin, lastMin = 0, -1
	j, result = 0, 0

	for i in xrange(N):
		while (j < N):
		# added new maximum element
			while (lastMax >= firstMax and maxQ[lastMax] <= A[j]):
				lastMax -= 1
			lastMax += 1
			maxQ[lastMax] = A[j]
			posmaxQ[lastMax] = j

			while (lastMin >= firstMin and minQ[lastMin] >= A[j]):
				lastMin -= 1
			lastMin += 1
			minQ[lastMin] = A[j]
			posminQ[lastMin] = j

			if (maxQ[firstMax] - minQ[firstMin] <= K):
				j += 1
			else:
				break
			result += (j - i)
			if result >= maxINT:
				return maxINT
			if posminQ[firstMin] == i:
				firstMin += 1
			if posmaxQ[firstMax] == i:
				firstMax += 1
	return result

#def solution(K,A):
#	N = len(A)
#	num_pairs = 0
#	for i in range(N):
#		j = i+1
#		while(j <= N):
#			sub_A = A[i:j]
#			if (max(sub_A) - min(sub_A) <= K):
#				num_pairs += 1
#				j += 1
#			else:
#			 	break
#	
#	print(num_pairs)	 
#	return num_pairs	
	
def main (argv = None):
	A = [3,5,7,6,3]
    	K = 2
#n = solution(K,A)
    	n = boundedSlicesGolden(K,A)
	print (n)
	return (0)

if __name__ == '__main__':
    status = main()
    sys.exit(status)
