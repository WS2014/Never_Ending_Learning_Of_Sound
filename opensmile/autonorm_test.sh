#!/bin/bash
#### Find the normalization for the accumulated.txt file columnwise
current_dir=${PWD}
sound_samples_folder="sound_samples_test"
text_mfcc_folder="$current_dir/text_samples_folder_test"
accumulation_folder="$current_dir/accumulated_folder_test"

echo "'$accumulation_folder/accumulated_file.txt'"
octave -qf --eval "cd $accumulation_folder;addpath('$current_dir');norm_column_test('$accumulation_folder/accumulated_file.txt')"

exit 0;
