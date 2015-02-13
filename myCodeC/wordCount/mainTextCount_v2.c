
/* --------------------------------

Name : Word Count.
Author: Ranaji Krishna.
   
Notes:	The program reads in a text file and prints out the 10 most frequent words from that file together 
	with their counts. A word is defined as a space-separated token. If several words have the same frequency, 
	they are considered to occupy a single “slot” from 1 to 10; and the program prints them all out. 
	The program takes as input argument a file, and print to STDOUT the list of words and their counts.

 ---------------------------------*/


#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "myAlgoPrep.h"

#define MAX_TOKEN 100			// Maximum number of Tokens.
#define TOP_FREQ 4			// Top 4 most frequent Tokens.


struct token{				// Linked List of all tokens.
	string word[MAX_CHARS];		// Maximum Characters.
	int freq;
	struct token *next;
};

int main(int argc, char *argv[]){

	struct token strToken[MAX_TOKEN];	// SIZE:100. Store all tokens.

	/* ------ Read the file and store the Tokens. ----- */
   	FILE *my;		
   	my = fopen("textFile_v2.txt","r");			// Parse file.
	int i = 0;
   	while(1){
    		fscanf(my, "%s", (*(strToken + i)).word);	// Read file & store words.
		if (feof(my)){
			break;
		}
		i++;
   	}
   	fclose(my);
	/* ----------------- */

	/*------- Extract Unique Tokens --------*/
	int ptrSkip = 1;			 // Counter for Words skipped.
	int uniqToken = 1;			 // Unique Words.		
	for (int j =0; j < i; j++){		 // Iterarte through words.
		
		(strToken + j)->freq = 0;		
		for (int k = 0; k < i; k++){ 	 // Check for word match.

			if ((strcmp( (strToken + j)->word, (strToken + k)->word ) == 0)){
				if (j > k){	          // Word already counted.
					ptrSkip++;
					break;
				}
				(strToken + j)->freq += 1; // New word.
			}
		}
		
		if ((strToken + j)->freq != 0 && j != 0){
			(strToken + j - ptrSkip)->next = (strToken + j);  
			ptrSkip = 1;
			uniqToken ++;
		}
	}
	/* ----------------- */

	/*  ------ Sort Tokens by Ascending Frequency ----- */	
	struct token *var = strToken;			
	struct uniqWord wordArray[MAX_TOKEN];			 // SIZE:100. Unique Tokens.	
	for (int m = 0; m < uniqToken; m++){
		strcpy((wordArray + m)->word, (var)->word);
		(wordArray + m)->freq = var->freq;
		var = (var)->next;
	}

	//printf("No. Unique words: %d\n", uniqToken);          // For verification.

	struct uniqWord *srtArray;			        // Sorted Words (aka. Tokens).
	srtArray = quickSortStruct(wordArray,0,(uniqToken-1));	// Call fxn. "quickSortSTruct" to sort tokens by freq.

	//for (int m = 0; m < uniqToken; m++){ 		// For Verification.
		//printf("%s : %d\n", (srtArray+m)->word, (srtArray+m)->freq);
	// }
	/* ---------------- */


	/* -------- Print the TOP_FREQ  Tokens with the Highest Frequecy ----- */
	int m = 0; int q = 0; int n = 0;
	while (m < TOP_FREQ){
		if((srtArray + uniqToken - 1 - q)->freq == (srtArray + uniqToken - 1 - n)->freq){
			printf("%s : %d\n", (srtArray + uniqToken - 1 - n)->word, (srtArray + uniqToken - 1 - n)->freq);
			n++;
		}else{
			m++; 
			q = n;
		}
	}
	/* -------------- */
	
	return(0);
	
}	
