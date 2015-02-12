
/* -------------------------
 
Name: Bubble sort algo.
Author: Ranaji Krishna.

Notes:	The fxn. implements bubblesort algo. to sort integers in an
	ascending order.

Inputs: Pointer to the array of integers to be sorted and the size of the array.

Output: Pointer to the sorted array
 
 -------------------------- */

#include <stdio.h>
#include <stdlib.h>


int large(int *pLarge){
	if (*pLarge > *(pLarge + 1)){			// Swap if value to the left is greater than the value to the right.
		*pLarge += *(pLarge +1);
		*(pLarge+1) = *(pLarge) - *(pLarge + 1);
		*(pLarge) = *(pLarge) - *(pLarge+1);
		return (0);
	}else{
		return (0);	
	}
}

int exchange(int *tmpArray, int end){
	
	int chkArray [99] = {0};			
	for (int i =0; i < end; i++){			// Iterate through the array.
		*(chkArray + i) = *(tmpArray + i); 
		large(tmpArray + i);			// Call swaping fxn.
	}
	
	for (int j =0; j < end; j++){
		if(*(chkArray + j) != *(tmpArray + j)){ // Evaluate swapping.
			exchange(tmpArray, end);	
		}
	}
	return (0);
}

int *bubble_sort(int *pArray, int end){

	exchange(pArray, end);	
	return(pArray);	
}
