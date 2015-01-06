import os
import re
import sys
import numpy as np

def horizontal_normalize_bag_of_words(histogram_testing_data):
	sum1 = 0.0
	print histogram_testing_data
	
	for item in histogram_testing_data:
		sum1 = sum1 + item
	return np.divide(histogram_testing_data, sum1) 


if(len(sys.argv)!=3):
	print "USAGE: python horizontal_normalize.py <filepath_accumulated_file> <output_directory>"
else:
	accumulated_file_path = sys.argv[1]
	output_directory = sys.argv[2]
	
	
	horizontal_hist = []
	
	with open(accumulated_file_path,"r") as userfile:
		histgram = []
		histogram = []
		for line in userfile:
			histogram = re.split(" |\n",line)[0:200]
			hist = []
			for item in histogram:
				hist.append(int(item))		
			histgram.append(hist)
		print histgram
	userfile.close()	
	
	with open(output_directory + "/horizontal_normalized_histograms.txt", "w") as userfile:
		for item in histgram:
			horizontal_hist = horizontal_normalize_bag_of_words(list(item))
			for value in horizontal_hist:
				if str(value) == 'nan':
					userfile.write("0 ")
				else:
					userfile.write(str(value) + " ")
			userfile.write("\n")
		userfile.close()
	
	
