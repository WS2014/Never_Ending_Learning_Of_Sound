import os
from os import listdir
from os.path import isfile, join
import sys

def accumulate_file(folder_name, accumulation_folder_name):
	directory = folder_name
	print directory
	x = os.walk(os.path.dirname(os.path.abspath(__file__)))
	print [x[1] for x in os.walk(directory)]
	#subdirectories = [x[1] for x in os.walk(directory)][0]

	with open(accumulation_folder_name + "/filelines.txt", "w") as filelines:
		with open(accumulation_folder_name + "/catgwise_numfiles.txt", "w") as catg_file:			
			with open(accumulation_folder_name + "/accumulated_file.txt", "w") as final_file:
				global_count = 0
				current_count = 0
				current_path = directory
				onlyfiles = []
				onlyfiles = [ f for f in listdir(current_path) if isfile(join(current_path,f)) ]

				for current_file in onlyfiles:
					file_count = 0 
					print current_path + "/" + current_file
					if '~' not in current_file:		
						with open(current_path + "/" + current_file, "r") as userfile:
							for line in userfile:
								final_file.write(line)
								file_count = file_count + 1
						current_count = current_count + file_count
						filelines.write(str(directory) + "/" + str(current_file) + "," + str(file_count)+"\n")
							
				catg_file.write(directory+":"+str(current_count)+",start:" + str(global_count+1) + ",end:" + str(global_count+current_count) + "\n")
				global_count = global_count + current_count


			final_file.close()
			catg_file.close()
			filelines.close()
	
if(len(sys.argv)!=3):
	print "\nUSAGE: python accumulation.py <folder_name> <accumulation_folder_name>\n"
else:
	folder_name = ""
	accumulation_folder_name = ""
	folder_name = str(sys.argv[1])
	accumulation_folder_name = str(sys.argv[2])
	accumulate_file(folder_name, accumulation_folder_name)
