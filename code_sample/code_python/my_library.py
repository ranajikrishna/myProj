

import sys
import numpy as np;
import random
import itertools
from math import *	 # Math fxns.
import pandas as pd
import xlrd

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

from sklearn.pipeline import Pipeline
from decimal import Decimal
from sklearn.linear_model import LinearRegression
from scipy.optimize import curve_fit
from random import randint
from cvxopt import blas, lapack, matrix, solvers
solvers.options['show_progress'] = 0
from scipy import linalg as LA
from numpy.linalg import matrix_rank

import svmutil as svm

