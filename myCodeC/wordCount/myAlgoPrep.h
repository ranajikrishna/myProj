
#include <stdio.h>
#include <stdlib.h>

#define MAX_CHARS 10
typedef char string[MAX_CHARS+1];  
struct uniqWord{
	string word[100];
	int freq;
};

struct uniqWord *quickSortStruct(struct uniqWord *pArray, int strt, int end);	// Quicksort algorithm that takes  the argument struct uniqWord.

