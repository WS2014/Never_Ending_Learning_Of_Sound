#!usr/bash

#supply the folder here
current_dir=${PWD}
sound_samples_folder="sound_samples_test"
voicebox_folder_name=$current_dir/"voicebox"
echo $voicebox_folder_name
htk_mfcc_folder="htk_samples_folder_test"
mkdir $current_dir/$htk_mfcc_folder
text_mfcc_folder="text_samples_folder_test"
mkdir $current_dir/$text_mfcc_folder
python fetch_mfcc.py $sound_samples_folder $htk_mfcc_folder $text_mfcc_folder $voicebox_folder_name


