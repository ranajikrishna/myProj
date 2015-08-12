

from myLib import *

import pandas as pd
import numpy as np
from pandas import Series, DataFrame, Panel



def main(argv=None):

	ao = np.loadtxt('/Users/vashishtha/myGitCode/myProj/myCodePy/timeSeriesData.txt')
	dates = pd.date_range('1950-01', '2015-08', freq='M')	
	
	AO = Series(ao[:,2], index=dates)	
	AO.plot()
	#plt.show()	

	AO['1980':'1990'].plot()
	#plt.show()	
	
	#AO['1960-01']	
	#AO['1960']
	#AO[AO > 0]

	nao = np.loadtxt('/Users/vashishtha/myGitCode/myProj/myCodePy/timeSeriesData2.txt')
	dates_nao = pd.date_range('1950-01', '2015-08', freq='M')
	NAO = Series(nao[:,2], index=dates_nao)

	aonao = DataFrame({'AO' : AO, 'NAO' : NAO})
	
	tmp_=0

	return(0)




if __name__ == '__main__':
	status = main()
	sys.exit(status)
