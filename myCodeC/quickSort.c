
/* ----------------------

Name: 	Quicksort algorithm.
Author: Ranaji Krishna.

Notes:	The fxn. sorts arrays in an ascending order.

Inputs: Pointer to the array to be sorted, starting index (=0)
	and size of array

Outputs: Pointer to the sorted array.
------------------------- */

#include <stdio.h>
#include <stdlib.h>

int partition(int *tmpArray, int st, int ed){
	
	int pvt = *(tmpArray + ed);	// Set the pivot.	
	int int1 = st;			// Starting index.

	while(st < ed){
		if(*(tmpArray+st) < pvt){		// Swap if value is less than the pivot.
			int m = *(tmpArray+int1);	
			*(tmpArray + int1) = *(tmpArray + st);
			*(tmpArray + st) = m;
			int1++;
		}
	st++;
	}

	*(tmpArray + ed) = *(tmpArray + int1);		// Update starting index.
	*(tmpArray + int1) = pvt;			// Update pivot.

	return(int1);
}


int *quick_sort(int *pArray, int strt, int end){

	if(strt < end){					// Sort.
		int int1;
		int1 = partition(pArray, strt, end);
		pArray = quick_sort(pArray, strt, int1 - 1);
		pArray = quick_sort(pArray, int1 + 1, end);
	}
	return(pArray);
}












