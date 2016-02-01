'''
Name:   Classification of Crimes in San Francisco.

Author: Ranaji Krishna.

*** Notes ***:
Predict the category of crimes that occurred in the city by the bay
From 1934 to 1963, San Francisco was infamous for housing some of the world's most notorious criminals on the inescapable island of Alcatraz. Today, the city is known more for its tech scene than its criminal past. But, with rising wealth inequality, housing shortages, and a proliferation of expensive digital toys riding BART to work, there is no scarcity of crime in the city by the bay. From Sunset to SOMA, and Marina to Excelsior, this competition's dataset provides nearly 12 years of crime reports from across all of San Francisco's neighborhoods.
Given time and location, you must predict the category of crime that occurred. We're also encouraging you to explore the dataset visually. What can we learn about the city through visualizations like this Top Crimes Map? The top most up-voted scripts from this competition will receive official Kaggle swag as prizes. 

'''

from myLib import *
from numpy.random import multivariate_normal

def classify(data):

	'''
	means = [(-1,0),(2,4),(3,1)]
	cov = [diag([1,1]), diag([0.5,1.2]), diag([1.5,0.7])]
	alldata = ClassificationDataSet(2, 1, nb_classes=3)
	for n in xrange(400):
		for klass in range(3):
        		input = multivariate_normal(means[klass],cov[klass])
		        alldata.addSample(input, [klass])

#tstdata, trndata = alldata.splitWithProportion( 0.25 )

	trndata = ClassificationDataSet(2,1, nb_classes = 3)
	[trndata.addSample(alldata['input'][k], alldata['target'][k]) for k in xrange(1, int( ceil(0.75 * len(alldata))))]
	
	tstdata = ClassificationDataSet(2,1, nb_classes = 3)
	[tstdata.addSample(alldata['input'][k], alldata['target'][k]) for k in xrange(int( ceil(0.75 * len(alldata)/3)) + 1, len(alldata)/3)]


	trndata._convertToOneOfMany( )
	tstdata._convertToOneOfMany( )	
	
	print "Number of training patterns: ", len(trndata)
	print "Input and output dimensions: ", trndata.indim, trndata.outdim
	print "First sample (input, target, class):"
	print trndata['input'][0], trndata['target'][0], trndata['class'][0]	
	
	fnn = buildNetwork( trndata.indim, 5, trndata.outdim, outclass=SoftmaxLayer )
	trainer = BackpropTrainer( fnn, dataset=trndata, momentum=0.1, verbose=True, weightdecay=0.01)

	ticks = arange(-3.,6.,0.2)
	X, Y = meshgrid(ticks, ticks)
	# need column vectors in dataset, not arrays
	griddata = ClassificationDataSet(2,1, nb_classes=3)
	for i in xrange(X.size):
	    griddata.addSample([X.ravel()[i],Y.ravel()[i]], [0])
	
	griddata._convertToOneOfMany()  # this is still needed to make the fnn feel comfy

	for i in range(20):
		trainer.trainEpochs( 1 )
		trnresult = percentError( trainer.testOnClassData(),
                                trndata['class'] )
		tstresult = percentError( trainer.testOnClassData(
        			dataset=tstdata ), tstdata['class'] )
		
		 print "epoch: %4d" % trainer.totalepochs, \
		       "  train error: %5.2f%%" % trnresult, \
        	       "  test error: %5.2f%%" % tstresult

		out = fnn.activateOnDataset(griddata)
		out = out.argmax(axis=1)  # the highest output activation gives the class
		out = out.reshape(X.shape)

		figure(1)
		ioff()  # interactive graphics off
		clf()   # clear the plot
	        hold(True) # overplot on
	        for c in [0,1,2]:
		        here, _ = where(tstdata['class']==c)
		        plot(tstdata['input'][here,0],tstdata['input'][here,1],'o')
		if out.max()!=out.min():  # safety check against flat field
			contourf(X, Y, out)   # plot the contour
		
		ion()   # interactive graphics on
		draw()  # update the plot
	
	ioff()
	show()
	'''
	'''
	data_sub = data[data['Bin']==0]
	fig = plt.figure()
	ax = fig.add_subplot(111, projection='3d')
	ax.scatter(data_sub['X'],data_sub['Y'],data_sub['Time'])
	
	#sorted(data['Bin'].unique())

	#plt.show()
	'''

	with open('objs.pickle') as trnTstData: trndata, tstdata = pickle.load(trnTstData)
	
	trndata = ClassificationDataSet(4,1, nb_classes = len(data['Bin'].unique()))
	[trndata.addSample(data.iloc[k, 0:4], data.iloc[k,4]) for k in xrange(1, int( ceil(0.75 * len(data))))]
	
	tstdata = ClassificationDataSet(4,1, nb_classes = len(data['Bin'].unique()))
	[tstdata.addSample(data.iloc[k, 0:4], data.iloc[k,4]) for k in xrange(int( ceil(0.75 * len(data))) + 1, len(data))]
	
	trndata._convertToOneOfMany()
	tstdata._convertToOneOfMany()

	n = buildNetwork(trndata.indim, 28, trndata.outdim, outclass=SoftmaxLayer)	
	trainer = BackpropTrainer(n, dataset = trndata, momentum=0.1, verbose=True, weightdecay=0.01) 

	trainer.trainEpochs(1)

	print (percentError(trainer.testOnClassData (dataset=tstdata), tstdata['class']))

	return(0);


def main (argv = None):

	store = pd.HDFStore('store_data.h5')
	
	train = pd.concat([store['data_train'][0], store['data_train'][7], store['data_train'][8], store['data_train'][3], store['data_train'][1]], axis=1)
	train = train.drop(train.index[[0]])
	train.columns = ['Time','X','Y','Day','Bin']
	
	[u, ind] = np.unique(train['Bin'], return_index=True)
	k = 0;
	for i in u:
		train.loc[train['Bin'] == i,'Bin'] = k
		k += 1
	
	dict_day = {'Monday':1,'Tuesday':2,'Wednesday':3,'Thursday':4,'Friday':5,'Saturday':6,'Sunday':7}
	for key in dict_day:
		train.loc[train['Day']==key,'Day'] = dict_day[key]

	weight = classify(train[0:110000])
#train = store['data_train'];
	store.close()
	return(0)


if __name__ == '__main__':
	status = main()
	sys.exit(status)


# ----- Convert data to storable HDFS objects -----	
#file_location = '/Users/vashishtha/myGitCode/myProj/myCodePy/ML/sfCrimeCla/train.xlsx';	 # File location path.
#workbook = xlrd.open_workbook(file_location);
#sheet = workbook.sheet_by_index(0);

#data_train = [[sheet.cell_value(r,c) for c in range(sheet.ncols)] for r in range (sheet.nrows)];  # Import in-sample data from Excel.
#data_train = pd.DataFrame(data_train, dtype = 'd');						  # Training data.
#store = pd.HDFStore('store_data.h5')	# Create hdfs to store values.

#store['data_train'] = data_train;	
	
#file_location = '/Users/vashishtha/myGitCode/myProj/myCodePy/ML/sfCrimeCla/test.xlsx';	 # File location path.
#workbook = xlrd.open_workbook(file_location);
#sheet = workbook.sheet_by_index(0);

#data_test = [[sheet.cell_value(r,c) for c in range(sheet.ncols)] for r in range (sheet.nrows)];  # Import in-sample data from Excel.
#data_test = pd.DataFrame(data_test, dtype = 'd');						 # Testing data.
#store['data_test'] = data_test;	
# -----------



