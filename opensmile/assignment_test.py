import os
import re
import numpy as np
import sys
from scipy.cluster.vq import vq

def get_bag_of_words(filename, cluster_file_path):
	with open(filename, "r") as userfile:
		lst = []	
		hist_data = []
		count = 0
		for line in userfile:
			count = count + 1
			data = re.split(' |\n', line)
			temp_list = []		
			for i in range(1,27):		
				print data[i]
				temp_list.append(float(data[i]))
			lst.append(temp_list)
			#if(count == 80):
			#	print count
				#print "LST Count = " + str(len(lst))
			#	hist_data.append(lst)
			#	count = 0
				#lst = []
		print count
		print "LST:LEN: " + str(lst)
		hist_data.append(lst)
	userfile.close()

	with open(cluster_file_path, "r") as userfile:
		lst2 = []	
		for line in userfile:
			data = re.split(' |\n', line)
			temp_list = []
			for i in range(1,27):		
				#print re.split(' |\n', data[i])[0]					
				temp_list.append(float(re.split(' |\n', data[i])[0]))
			lst2.append(temp_list)
			
		userfile.close()
	print lst2
	bins = []	
	for i in range(0,201):
		bins.append(i)
	#print bins
	histograms = []
	for item in hist_data:		
		[C,D]  = vq(np.array(lst), np.array(item))
		#print "C:\n" + str(C)	
		#print np.histogram(C, np.array(bins))
		[hist,B] = np.histogram(C, np.array(bins))
		histograms.append(hist)
		#print "Bin length = " + str(len(hist))
		#print hist
	return histograms

def horizontal_normalize_bag_of_words(histogram_testing_data):
	sum1 = 0.0
	print histogram_testing_data
	
	for item in histogram_testing_data:
		sum1 = sum1 + item
	return np.divide(histogram_testing_data, sum1) 


if(len(sys.argv)!=4):
	print "USAGE: python assignment.py <filepath_accumulated_file> <cluster_file_path> <output_directory>"
else:
	accumulated_file_path = sys.argv[1]
	cluster_file_path = sys.argv[2]
	output_directory = sys.argv[3]
	#print accumulated_file_path

		
	normalized_hist = []
	horizontal_hist = []
	histgram = get_bag_of_words(accumulated_file_path, cluster_file_path)
	
	with open(output_directory + "/histograms_test.txt", "w") as userfile:
	        for item in histgram:
			horizontal_hist = horizontal_normalize_bag_of_words(list(item))
			for value in horizontal_hist:
				if str(value) == 'nan':
					userfile.write("0 ")
				else:
					userfile.write(str(value) + " ")
			userfile.write("\n")
		userfile.close()
	

	
