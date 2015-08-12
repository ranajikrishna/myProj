
from math import sqrt

def solution(A,B,T):
    
    if None == T:
	return 0
    else:
        sub_tree = [solution(A,B,branch) for branch in T[1:]]
         
    return 0 




def main (argv = None):
#T = [5, [3, [20, None, None], [21, None, None]], [10, [1, None, None], None]]
#T = (5, (3, (20, None, None), (21, None, None)), (10, (1, None, None), None))
#	T = [1, [2, None, None], [3, None, None]]
#T = [5, [2, [3, [4, None, None], [6, None, None]], None],[1, [7, None, None], [8, None, None]]]

	L =  (15, 29, (25, (19, (12, (4, None, None), None), (22, None, (23, None, None))), (37, (29, None, (30, None, None)), None)))

	n = solution(L[0],L[1],L[2:])
	print (n)
	return (0)

if __name__ == '__main__':
    status = main()
    sys.exit(status)
