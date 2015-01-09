import os
import re
import sys

def splitter(input_path, input_path2, output_path):
		
	with open(input_path + "/catgwise_numfiles.txt", "r") as userfile:
		folder_name_count = []	
		for line in userfile:
			splitted_line = line.split(",")
			print splitted_line
			category = splitted_line[0].split(":")[0]
			category_frames = splitted_line[0].split(":")[1]
			start = splitted_line[1].split(":")[0]
			start_frames = splitted_line[1].split(":")[1]
			end = splitted_line[2].split(":")[0]
			end_frames = re.split(":|\n", splitted_line[2])[1]
			
			data = {}	
			data['category'] = str(category)
			data['category_frames'] = int(category_frames)
			data['start'] = int(start_frames)
			data['end'] = int(end_frames)
			
			folder_name_count.append(data)
	
		userfile.close()

	with open(input_path + "/filelines.txt","r") as frame_per_file:
		frame_count = {}
		for item in folder_name_count:
			frame_count[item['category']] = []		
		
		for line in frame_per_file:
			category_details = {}
			num_list = re.split("\n", line)
			category = num_list[0].split(",")[0].split("/")[0]
			file_dict = {}
			file_frame = int(num_list[0].split(",")[1])
			file_name = num_list[0].split(",")[0].split("/")[1]
			file_dict['file_frame'] = int(file_frame)
			file_dict['file_name'] = file_name			
			frame_count[category].append(file_dict)
		frame_per_file.close()
		print frame_count
	
	
	
	with open(input_path2 + "/normalized_text.txt.membership","r") as membership_file:
		count = 0
		i = 0
		j = 0
		for item in folder_name_count:
			category_frames = item['category_frames']
			category = item['category']
			
			directory = os.path.join(output_path, category)
			if not os.path.exists(directory):
				os.makedirs(directory)
			while(category_frames>0):
				print frame_count[category]
				while(count<frame_count[category][i]['file_frame']):	
					with open(str(directory + "/" + str(frame_count[category][i]['file_name'])), "a") as userfile:
						line = membership_file.readline()
						print line
						userfile.write(line)
						count = count + 1
			
				userfile.close()
				category_frames = category_frames - frame_count[category][i]['file_frame'] 
				i = i+1	
				count = 0
			i = 0
				

	
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
