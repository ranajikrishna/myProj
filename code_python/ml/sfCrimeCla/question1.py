

# ---------------------------
#
# Name: Question 1, Homework 2.
#
# Author: Ranaji Krishna.

# Notes:  Run a computer simulation for flipping 1,000 virtual fair coins. Flip each coin independently
# 10 times. Focus on 3 coins as follows: c1 is the first coin flipped, crand is a
# coin chosen randomly from the 1,000, and cmin is the coin which had the minimum
# frequency of heads (pick the earlier one in case of a tie). Let v, rand, and min be
# the fraction of heads obtained for the 3 respective coins out of the 10 tosses.
# Run the experiment 100,000 times in order to get a full distribution of v, rand, and
# min (note that crand and cmin will change from run to run).:
#
# ---------------------------


import sys;
import numpy as np;
import random;
import itertools;
from math import *		        # Math fxns.


def main (argv = None):

	allFlips = np.ndarray((10,1000),  dtype = np.int);	# Store flips. Size: 10 X 1000.	
	row_sum = np.zeros(1000, int);				# Store no. H (=1) for each coin.

	for i in range(0,1000):
		allFlips[:,i] = np.random.binomial(1,0.5,10);	# Generate flips.
		row_sum[i] = sum(allFlips[:,i]);		# Determine no. H.

	c_1 = 0;						# First coin.
	c_min = np.where(row_sum == row_sum.min())[0][0];	# Determine coin with min. H.
	c_rand = random.randint(0,1000);			# Assign random coin.

	# ---- Average no. H -----
	v_1 = np.mean(allFlips[:,c_1]);				
	v_min = np.mean(allFlips[:,c_min]);
	v_rand = np.mean(allFlips[:,c_rand]);

	print 'The average value of v_min', v_min;

if __name__ == '__main__':
	status = main();
	sys.exit(status);
