
class letter():

	vowel = 0;			# Indicates Vowel (1: Vowel).
	pos = None;			# Position of letters. If letter appears both in string1 & string2, store position of string1.
	alpha = None;			# The letter.

	def setFreqOne(self, freq):
		self.freq1 = freq;	# Freq. of letter in string1.

	def setFreqTwo(self, freq):
		self.freq2 = freq;	# Freq. of letter in string2.
	
	def isActive(self):
		return(self.freq2 - self.freq1);	# If freq. in string1 != freq. in string2.

	def getFreq(self):
		return([self.freq1,self.freq2]);

