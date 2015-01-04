import os
from os import listdir
from os.path import isfile, join
import sys

def accumulate_file(folder_name, accumulation_folder_name):
	directory = folder_name
	print directory
	x = os.walk(os.path.dirname(os.path.abspath(__file__)))
	print [x[1] for x in os.walk(directory)]
	subdirectories = [x[1] for x in os.walk(directory)][0]

	with open(accumulation_folder_name + "/accumulated_file.txt", "w") as final_file:
	
		for subdirectory in subdirectories:
			current_path = directory + "/" + subdirectory
			onlyfiles = []
			onlyfiles = [ f for f in listdir(current_path) if isfile(join(current_path,f)) ]
			for current_file in onlyfiles:
				print current_path + "/" + current_file
				if '~' not in current_file:		
					with open(current_path + "/" + current_file, "r") as userfile:
						for line in userfile:
							final_file.write(line)
					userfile.close()


	final_file.close()

if(len(sys.argv)!=3):
	print "\nUSAGE: python accumulator.py <folder_name> <accumulation_folder_name>\n"
else:
	folder_name = ""
	accumulation_folder_name = ""
	folder_name = str(sys.argv[1])
	accumulation_folder_name = str(sys.argv[2])
	accumulate_file(folder_name, accumulation_folder_name)
