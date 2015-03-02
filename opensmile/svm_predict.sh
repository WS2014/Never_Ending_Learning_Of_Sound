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
mkdir -p $SVM_output

libSVM_path="$current_dir/libsvm-3.20"
cd $libSVM_path

echo "Enter the category for which you want to train the SVM - The name of category needs to be entered as a single word in lower case"
read category

./svm-train $SVM_input/svm_input_$category.train $SVM_input/svm_input_$category.train.model

./svm-predict $SVM_input_test/svm_input_$category.test $SVM_input/svm_input_$category.train.model $SVM_output/svm_output_$category.txt
