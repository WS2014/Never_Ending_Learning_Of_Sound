# This file intends gerate normalized files of all files in given folder

import os
from os import listdir
from os.path import isfile, join
import sys
import re
import math

def normalize_files(file_name, normalized_folder_name):
			
    
	
	
	with open(normalized_folder_name + "/normalized_file.txt", "w") as norm_file:	
		with open(normalized_folder_name + "/meanVar.txt", "w") as mv_file:
			
			fp= open(file_name)   

			lines= fp.readlines()

			flines=[]
			for x in lines:
				v=re.split('\n',x)[0]
				if (v != ''):
					flines.append(v)	
					
			no_of_lines= len(flines)
			meanSum=[0]*26
			sqX= [0]*26  #sum of sq

			i=0
			#for i in range(26):

			for x in flines: 
				v=re.split(' ',x)
				i=0
				for i in range(26):
					
					meanSum[i]= meanSum[i]+ float(v[i])
					sqX[i]=sqX[i]+float(v[i])*float(v[i])
					i=i+1
						
				
			
			# calculating the variance
			mv_file.write("Mean:\n");
			for i in range(26):
				meanSum[i]= meanSum[i]/no_of_lines  #E(X)
				mv_file.write(str(meanSum[i])+" ")
				sqX[i]= sqX[i]/no_of_lines   #E(X^2)
			mv_file.write("\n");

			#print "Mean:\n"
			#print meanSum
			#print sqX

			variance =[0]*26
			mv_file.write("Variance:\n");
			for i in range(26):
				variance[i]= sqX[i] - meanSum[i]*meanSum[i]
				mv_file.write(str(variance[i])+" ")
			#print "Variance:\n"
			#print variance


			# Normalizing file now
			for x in flines: 
				v=re.split(' ',x)
				i=0
				for i in range(26):
					
					val = (float(v[i])- meanSum[i])/ math.sqrt(variance[i]);
					norm_file.write(str(val)+" ")
					
				norm_file.write("\n")

	fp.close()
	norm_file.close()
	mv_file.close()
				

if(len(sys.argv)!=3):
	print "\nUSAGE: python normalization.py <file_name> <normalized_folder_name>\n"   #normalized_folder would have 2 files: first having the mean n variance, second the normalzed file
else:
	file_name = ""
	normalized_folder_name = ""
	file_name = str(sys.argv[1])
	normalized_folder_name = str(sys.argv[2])
	if not os.path.exists(os.path.dirname('/'+ normalized_folder_name)):
		os.makedirs(os.path.dirname('/'+normalized_folder_name))
	normalize_files(file_name, normalized_folder_name)
