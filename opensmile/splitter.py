import os
import re
import sys

def splitter(input_path, input_path2, output_path):
	with open(input_path + "/filelines.txt","r") as frame_per_file:
		frame_count = []	
		for line in frame_per_file:
			num_list = re.split("\n", line)	
			file_frame_count = int(num_list[0])
			frame_count.append(file_frame_count)
		frame_per_file.close()
	
	with open(input_path + "/filenames.txt", "r") as filenames:
		file_name = []	
		for line in filenames:
			filename = re.split("\n", line)	
			file_name.append(str(filename[0]))
	
	
		filenames.close()

	with open(input_path + "/catgwise_numfiles.txt", "r") as userfile:
		folder_name_count = []	
		for line in userfile:
			data_list = re.split(":|\n", line)
			folder_name = ""
			folder_name  = data_list[0]
			number = int(data_list[1])
		
			data = {}	
			data['folder_name'] = str(folder_name)
			data['count'] = number
			print data
			folder_name_count.append(data)
	
		#print folder_name_count
		userfile.close()



	"""
	for i in range(len(folder_name_count)-1, 0,-1):
		folder_name_count[i]['count'] = folder_name_count[i]['count'] - folder_name_count[i-1]['count']
		#print str(folder_name_count[i]['count'])
	"""

	#print folder_name_count

	with open(input_path2 + "/normalized_text.txt.membership","r") as membership_file:
		count = 0
		i = 0
		j = 0
		for item in folder_name_count:
			number = item['count']
			print item['folder_name']
			directory = os.path.join(output_path, item['folder_name'])
			if not os.path.exists(directory):
				os.makedirs(directory)
			while(number>0):
				while(count<frame_count[i]):	
					with open(str(directory + "/" + str(file_name[i])), "a") as userfile:
						line = membership_file.readline()
					
						#print line
						userfile.write(line)
						
						count = count + 1
			
				userfile.close()
				number = number - frame_count[i] 
				i = i+1		
				count = 0
        


if(len(sys.argv)!=4):
	print "\nUSAGE: python splitter.py <folder_name_of_input_files> <folder_name_of_input_files2> <folder_name_of_output_folders>\n"
else:
	input_folder_name = ""
	input_folder_name = str(sys.argv[1])
        input_folder_name2 = ""
	input_folder_name2 = str(sys.argv[2])
	output_folder_name = ""
	output_folder_name = str(sys.argv[3])
	splitter(input_folder_name, input_folder_name2, output_folder_name)
