#!usr/bash

#supply the folder here
current_dir=${PWD}
sound_samples_folder="sound_samples_test"
text_mfcc_folder="$current_dir/text_samples_folder_test"
accumulation_folder="$current_dir/accumulated_folder_test"
kmeans_output="$current_dir/kmeans_output_test"
text_histogram_folder="$current_dir/text_histogram_folder_test"
text_histogram_folder_norm="$current_dir/text_histogram_folder_norm"
echo "Enter the category for which you want to train the SVM - The name of category needs to be entered as a single word in lower case"
read category
SVM_input="$current_dir/SVM_input_test"
mkdir -p $text_mfcc_folder
mkdir -p $accumulation_folder
mkdir -p $text_histogram_folder
mkdir -p $kmeans_output
mkdir -p $text_histogram_folder_norm
mkdir -p $SVM_input
gcc convert.c -o convert
python svm_input.py $SVM_input/vertical_and_horizontal_normalized_histograms.txt $SVM_input/catgwise_numfiles.txt $category
mv svm_input_$category.txt $SVM_input/svm_input_$category.txt
./convert $SVM_input/svm_input_$category.txt > $SVM_input/svm_input_$category.test


