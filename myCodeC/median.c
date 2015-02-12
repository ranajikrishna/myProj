
/* ----------------------
Name:   Median code.  
Author: Ranaji Krishna.

Notes:  The code calculates the median of an array. It uses a quick sort algorithm
	to partition the array until the partitioning position is at the middle of the
	array.
	
Inputs: Pointer to array of integers; starting index (= 0) and size of array and 0);

Outputs: Pointer to sorted median value.
 
 ----------------------- */


#include <stdio.h>
#include <stdlib.h>

int partition(int *strArray, int st, int ed){

	int pvt = *(strArray + ed);				// Pivot position.
	int ind = st;
	while(st < ed){						// Swap if value is less tha pivot.
		if(*(strArray + st) < pvt){
			int m = *(strArray + st);
			*(strArray + st) = *(strArray + ind);		
			*(strArray + ind) = m;
			ind += 1;
		}
		st += 1;	
	}

	*(strArray + ed) = *(strArray + ind);			
	*(strArray + ind) = pvt;
	return(ind);
}

int *median(int *pArray, int srt, int end, int chkPvt){

	if (srt == 0){						// Set pivot. 
		if (end % 2){
			chkPvt = (end + 1)/2 - 1;
		}else{
			chkPvt = (end/2);
		}
	}	

	if (srt <= end){
		int int1 = partition(pArray, srt, end);		
		if(int1 > chkPvt){
			pArray = median(pArray, srt, (int1 - 1), chkPvt);
		}else if(int1 < chkPvt){
			pArray = median(pArray, (int1 + 1), end, chkPvt);
		}else{
			return((pArray+int1));
		}	
	}
	return(pArray);
}
