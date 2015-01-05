import os
from os import listdir
from os.path import isfile, join
import sys
import oct2py

def get_mfcc(folder_name, htk_folder_name, text_folder_name, voicebox_path):
	voicebox_path_tick = "'" + voicebox_path + "'"
	input_directory = folder_name
	print input_directory
	subdirectories = [x[1] for x in os.walk(input_directory)][0]
	print subdirectories
	for directory in subdirectories:
		create_dir_cmd = "mkdir -p " + text_folder_name + "/" + directory
		print create_dir_cmd
		os.system(create_dir_cmd)	
		create_dir_cmd = "mkdir -p " + htk_folder_name + "/" + directory
		print create_dir_cmd
		os.system(create_dir_cmd)
		text_path = text_folder_name + "/" + directory
		htk_path = htk_folder_name + "/" + directory
		current_path = input_directory + "/" + directory
		print current_path
		onlyfiles = []
		onlyfiles = [ f for f in listdir(current_path) if isfile(join(current_path,f)) ]
		for current_file in onlyfiles:
			print current_file
			sound_filepath = current_path + "/" + current_file
			htk_filepath = htk_path + "/" + current_file + ".htk"
			text_filepath = text_path + "/" + current_file + ".txt"
			
			my_exec = 'openSMILE-2.1.0/SMILExtract -C openSMILE-2.1.0/config/MFCC12_E_D_A.conf -I ' + sound_filepath + ' -O ' + htk_filepath
			print my_exec
			os.system(my_exec)
			
			filepath = "'" + htk_filepath + "'"
			output_file_path = "'" + text_folder_name + "/" + directory + "/" + current_file + ".txt'"
			
			my_exec = 'octave -qf --eval "htk2txt(' + filepath + ',' + voicebox_path_tick + ',' + output_file_path + ')"'
			print my_exec
			os.system(my_exec)
			
if(len(sys.argv)!= 5):
	print "\nUSAGE: python accumulator.py <folder_name> <htk_folder_name> <accumulation_folder_name> <voicebox_path>\n"
else:
	sound_samples_folder_name = ""
	text_folder_name = ""
	voicebox_folder_name = ""
	sound_samples_folder_name = str(sys.argv[1])
	htk_folder_name = str(sys.argv[2])
	text_folder_name = str(sys.argv[3])
	voicebox_folder_name = str(sys.argv[4])
	get_mfcc(sound_samples_folder_name, htk_folder_name, text_folder_name,voicebox_folder_name)
