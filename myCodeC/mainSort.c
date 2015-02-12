
/* --------------------

Name: 	Testing framework.
Author: Ranaji Krishna.

Notes:	The code calls bubble sort and 
	quicksort algo. for sorting.

---------------------- */


#include <stdio.h>
#include <stdlib.h>
#include "myAlgoPrep.h"	
			
int main(int argc, char* argv[]){

	int num; num = 9;				// Size of the array.
	int strArray [9] = {41,2,30,6,24,9,14,4,5};	// Array of integers.	
	int *tmp, *tmp1;

	tmp = quick_sort(strArray,0,(num-1));		// Call quick sort fxn.
	//tmp = bubble_sort(strArray,num);		// Call bubble sort fxn.

	printf("In ascending order:");
	for (int i =0; i<num; i++){			// Print Array.
		if(i != (num-1)){
			printf("[%d],",*(tmp+i));
		}else{
			printf("[%d]",*(tmp+i));
		}
	}
	printf("\n");

	return(0);
}
