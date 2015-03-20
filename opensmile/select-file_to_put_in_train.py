import os
import re
import sys

def fileselection(input_path,input_filename,output_folder_path):
    with open(input_path +"/filelines.txt","r") as userfile:
    	lines = userfile.readlines()
    	print lines
	with open(output_folder_path +"/file_to_pick_in_training_database.txt","w") as file1:
		with open(input_filename,"r") as filenumber:
			filenum = filenumber.readlines()
			size = len(filenum)
			print filenum
			i = 0
			for item in filenum:
				y = filenum[i]
				y = int(y)
				i=i+1
				print y
				k = lines[y]
				print k
				k = k.split(',')
				k = k[0]
				print k
				k = str(k)
				line3 = file1.writelines(k)
				line4 = file1.writelines("\n")
		filenumber.close()
	file1.close()
    userfile.close()		
	
if(len(sys.argv)!=4):
	print "\nUSAGE: python select-file_to_put_in_train.py <foldername_of_input1> <file_containing_confidence_input_file_numbers> <output_folder_path>\n"
else:
	input_path=""
	input_path=str(sys.argv[1])
        print input_path
	input_filename=""
	input_filename=str(sys.argv[2])
	output_folder_path=""
	output_folder_path=str(sys.argv[3])
	fileselection(input_path,input_filename,output_folder_path)

