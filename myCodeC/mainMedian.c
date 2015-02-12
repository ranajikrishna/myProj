
/* --------------------------
Name:	Median testing code.
Author: Ranaji Krishna.

Notes: The code tests the fxn. "median".


----------------------------- */


#include <stdio.h>
#include <stdlib.h>
#include "myAlgoPrep.h"	
			
int main(int argc, char* argv[]){

	int num; num = 9;				// Size of array.
	int strArray [9] = {41,2,30,6,24,78,9,14,4};	// Array.
	int *tmp;

	tmp = median(strArray,0,num,0);			// Call fxn. median.

	printf("Median [%d]",*(tmp));
	printf("\n");
	return(0);
}
