#!usr/bash

#supply the folder here
current_dir=${PWD}
sound_samples_folder_test="sound_samples_test"
text_mfcc_folder_test="$current_dir/text_samples_folder_test"
accumulation_folder_test="$current_dir/accumulated_folder_test"
kmeans_output_test="$current_dir/kmeans_output_test"
text_histogram_folder_test="$current_dir/text_histogram_folder_test"
text_histogram_folder_norm_test="$current_dir/text_histogram_folder_norm"
SVM_input_test="$current_dir/SVM_input_test"

sound_samples_folder="sound_samples"
text_mfcc_folder="$current_dir/text_samples_folder"
accumulation_folder="$current_dir/accumulated_folder"
kmeans_output="$current_dir/kmeans_output"
text_histogram_folder="$current_dir/text_histogram_folder"
text_histogram_folder_norm="$current_dir/text_histogram_folder_norm"
SVM_input="$current_dir/SVM_input"

SVM_output="$current_dir/SVM_output"

echo "Enter the category for which you want to generate the precison and recall curve"
read category

INP_FILE=SVM_input_test/svm_input_$category.txt
OUT_FILE=SVM_output/svm_output_$category.txt

echo "$INP_FILE $OUT_FILE"

octave -qf --eval "addpath('$current_dir'); precision_recall_plot('$INP_FILE','$OUT_FILE')"


sleep 20