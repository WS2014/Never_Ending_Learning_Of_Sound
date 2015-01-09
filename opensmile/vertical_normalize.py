import sys
import os
import re
import numpy as np


def vertical_normalize_bag_of_words(mean_training_data, stddev_training_data, histogram_testing_data):
	return np.divide(np.subtract(histogram_testing_data, mean_training_data), stddev_training_data) 



def main():
	if(len(sys.argv)!=5):
		print "USAGE: python assignment.py <horizontal_normalized_accumulated_file> <mean_normalization_filepath> <stddev_normalization_filepath> <output_directory>"
	else:
		accumulated_file_path = sys.argv[1]
		mean_normalization_filepath = sys.argv[2]
		stddev_normalization_filepath = sys.argv[3]
		output_directory = sys.argv[4]
	
		#mean code	
		mean_list = []
	
		with open(mean_normalization_filepath, "r") as mean_file:
			for line in mean_file:
				temp_list = re.split(",|\n", line)[0:200]
				#print temp_list
				for item in temp_list:
					mean_list.append(float(item))
			mean_file.close()
		#print mean_list	
		stddev_list = []
		with open(stddev_normalization_filepath, "r") as stddev_file:
			for line in stddev_file:
				temp_list = re.split(",|\n", line)[0:200]
				#print temp_list
				for item in temp_list:
					stddev_list.append(float(item))
			stddev_file.close()
		#print stddev_list
	
		normalized_hist = []
	
		with open(accumulated_file_path,"r") as userfile:
			histgram = []
			histogram = []
			for line in userfile:
				histogram = re.split(" |\n",line)[0:200]
				hist = []
				for item in histogram:
					print item
					try:
						hist.append(float(item))
					except ValueError,e:
						print "Error: ", e
						return

				histgram.append(hist)
			print histgram
		userfile.close()	
	
		with open(output_directory + "/vertical_and_horizontal_normalized_histograms.txt", "w") as userfile:
			for item in histgram:
				normalized_hist = vertical_normalize_bag_of_words(mean_list, stddev_list, list(item))
				for value in normalized_hist:
					print value
					if str(value) == 'nan':
						userfile.write("0 ")
					else:
						userfile.write(str(value) + " ")
				userfile.write("\n")
			userfile.close()

if __name__ == "__main__":
    main()
