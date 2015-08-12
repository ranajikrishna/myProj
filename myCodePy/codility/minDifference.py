

from myLib import *

def solution(tmpArray):
    
    tot_sum = sum(tmpArray)
    left_sum = 0
    diff = [i for i in range(len(tmpArray)-1)]
    for i in range(0,(len(tmpArray)-1)):
        left_sum += tmpArray[i]
        diff[i] = fabs(tot_sum - (2*left_sum))
    
    return (int(min(diff)))

def main(argv = None):
    
    myArray = [3,1,2,4,3]
    minDiff = solution(myArray)
    print(minDiff)
    return (0)


if __name__ == '__main__':
    status = main()
    sys.exit(status)
