#!usr/bash

#supply the folder here
current_dir=${PWD}
SVM_output="$current_dir/SVM_output"
Confidence_level_files="$current_dir/Confidence_level"
SVM_input_test="SVM_input_test"


mkdir -p $SVM_output
mkdir -p $Confidence_level_files
echo "Enter the category for which you want to do find files"
read category

input_file=$SVM_output/svm_output_$category.txt
output_file=$Confidence_level_files/files_number_to_pick_$category.txt

octave -qf --eval "addpath('$current_dir');find_files_greater_than_a_confidence_level('$input_file','$output_file')"

python select-file_to_put_in_train.py $SVM_input_test $output_file $Confidence_level_files

exit 0;
