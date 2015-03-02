import os
import re
import scipy
import sys
from scipy.cluster.vq import vq	
from numpy import array

def assignment(accumulated_file_path,cluster_folder_path):
	with open(accumulated_file_path, "r") as userfile:
			lst2 = []	
			for line in userfile:
				data = re.split(' |\n', line)
				temp_list = []
				for i in range(1,27):		
					#print re.split(' |\n', data[i])[0]					
					temp_list.append(float(re.split(' |\n', data[i])[0]))
				lst2.append(temp_list)
				
			userfile.close()

	print len(lst2)
	with open(cluster_folder_path + "/normalized_text.txt.cluster_centres", "r") as cluster_file:
			lst3 = []	
			for line in cluster_file:
				data = re.split(' |\n', line)
				temp_list = []
				for i in range(1,27):		
					#print re.split(' |\n', data[i])[0]					
					temp_list.append(float(re.split(' |\n', data[i])[0]))
				lst3.append(temp_list)
				
			cluster_file.close()

	print len(lst3)


	code_book = array(lst3)
	features = array(lst2)

	[C,D] = vq(features,code_book)
	print C
	print D
	return C
	print len(C)

if(len(sys.argv)!=4):
	print "USAGE: python assignment_test1.py <accumulated_file_path> <cluster_folder_path> <output_file_with_path>"
else:
	accumulated_file_path = sys.argv[1]
	cluster_folder_path = sys.argv[2]
	output_file_with_path = sys.argv[3]

	lst4 = assignment(accumulated_file_path, cluster_folder_path)
	with open(output_file_with_path,"w") as userfile3:
		userfile3.writelines(["%s\n" % item for item in lst4])
