import re
import shutil
import os,sys

def file_copy(input_folder_path,search_folder_path,output_folder_path):
	f = []
	for (dirpath,dirnames,filenames) in os.walk(search_folder_path):
		f.extend(filenames) 
	print f
	'''paths = [os.path.join(search_folder_path,fn) for fn in next(os.walk(search_folder_path))[2]]
	print paths'''
	if not os.path.exists(output_folder_path +'/dogs' ):
    		os.makedirs(output_folder_path +'/dogs')
	
	with open(input_folder_path + "/file_to_pick_in_training_database.txt","r") as userfile:
		lines = userfile.readlines()
		#print lines
		i = 0
		for item in lines:
			y = lines[i]
			i = i+1
			#print y
			y = y.split('.t')
			p = y[0]+  '.t' + y[1]
			tmp = y[0]
			tmp = tmp.split('/')
			sub_dir_name = tmp[0]
			file_name = tmp[1]
			print file_name
			if not os.path.exists(output_folder_path +'/'+ sub_dir_name):
				os.makedirs(output_folder_path +'/'+ sub_dir_name)
			#print y[0]
			#print p
			w = search_folder_path + p
			print w
			print output_folder_path+"/"+p
			shutil.copyfile(w,output_folder_path+"/"+ p)					

if(len(sys.argv)!=4):
	print "\nUSAGE: python file_copy_for_train_from_test.py <folder_name_of_input_files> <folder_name_of_input_files2> <folder_name_of_output_folders>\n"
else:
	input_folder_path = ""
	input_folder_path = str(sys.argv[1])
	search_folder_path = ""
	search_folder_path = str(sys.argv[2])
	output_folder_path = ""
	output_folder_path = str(sys.argv[3])
	file_copy(input_folder_path,search_folder_path,output_folder_path)

