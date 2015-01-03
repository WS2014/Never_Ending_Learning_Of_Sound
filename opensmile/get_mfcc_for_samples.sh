#!usr/bash

#supply the folder here
current_dir=${PWD}
sound_samples_folder="sound_samples"
voicebox_folder_name=$current_dir/"voicebox"
echo $voicebox_folder_name
text_mfcc_folder="text_samples_folder"
mkdir $current_dir/$text_mfcc_folder
python fetch_mfcc.py $sound_samples_folder $text_mfcc_folder $voicebox_folder_name


