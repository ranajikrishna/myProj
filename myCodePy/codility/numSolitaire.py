

NR_POSSIBLE_ROLLS = 6
MIN_VALUE = -10000000001
 
def solution(A):
    sub_solutions = [MIN_VALUE] * (len(A)+NR_POSSIBLE_ROLLS)
    sub_solutions[NR_POSSIBLE_ROLLS] = A[0]
     
    # iterate over all steps
    for idx in xrange(NR_POSSIBLE_ROLLS+1, len(A)+NR_POSSIBLE_ROLLS):
        max_previous = MIN_VALUE
        for previous_idx in xrange(NR_POSSIBLE_ROLLS):
            max_previous = max(max_previous, sub_solutions[idx-previous_idx-1])
        # the value for each iteration is the value at the A array plus the best value from which this index can be reached
        sub_solutions[idx] = A[idx-NR_POSSIBLE_ROLLS] + max_previous
     
    return sub_solutions[len(A)+NR_POSSIBLE_ROLLS-1]


def main(argv=None):
	num = [1,-2,0,9,-1,-2]
#num = [-1,-1,-1]
	n = solution(num)
	print(n)
	return(0)


if __name__ == '__main__':
    status = main()
    sys.exit(status)
