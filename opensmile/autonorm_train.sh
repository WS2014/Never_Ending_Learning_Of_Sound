#!/bin/bash
#### Find the normalization for the accumulated.txt file columnwise
current_dir=${PWD}
sound_samples_folder="sound_samples"
text_mfcc_folder="$current_dir/text_samples_folder"
accumulation_folder="$current_dir/accumulated_folder"

echo "'$accumulation_folder/accumulated_file.txt'"
octave -qf --eval "cd $accumulation_folder;addpath('$current_dir');norm_column_train('$accumulation_folder/accumulated_file.txt')"

exit 0;
