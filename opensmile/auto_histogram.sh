#!usr/bash

#supply the folder here
current_dir=${PWD}
sound_samples_folder="sound_samples"
text_mfcc_folder="$current_dir/text_samples_folder"
accumulation_folder="$current_dir/accumulated_folder"
kmeans_output="$current_dir/kmeans_output"
text_histogram_folder="$current_dir/text_histogram_folder"
text_histogram_folder_norm="$current_dir/text_histogram_folder_norm"
SVM_input="$current_dir/SVM_input"
mkdir -p $text_mfcc_folder
mkdir -p $accumulation_folder
mkdir -p $text_histogram_folder
mkdir -p $kmeans_output
mkdir -p $text_histogram_folder_norm
mkdir -p $SVM_input
python $current_dir/splitter.py $accumulation_folder $kmeans_output $text_histogram_folder

for in_subdir in `ls -d $text_histogram_folder/*`
do  
     out_subdir=`echo $in_subdir | sed -e s/text_histogram_folder/text_histogram_folder_norm/` 
     mkdir -p $out_subdir
     for txt_file in $in_subdir/*.txt 
     do
         text_file_root=`echo $txt_file | sed -e s/text_histogram_folder/text_histogram_folder_norm/`  
         text_file=`echo $text_file_root | sed -e s/.txt$/.txt/`  
         INP_FILE=$txt_file
         OUT_FILE=$text_file  
         echo "'$INP_FILE' '$OUT_FILE'"
         octave -qf --eval "addpath('$current_dir'); cluster2bins('$INP_FILE','$OUT_FILE')"
     done
done
python $current_dir/accumulation.py $text_histogram_folder_norm $SVM_input


python $current_dir/horizontal_normalize.py $SVM_input/accumulated_file.txt $SVM_input

octave -qf --eval "cd $SVM_input ;addpath('$current_dir'); mean_and_var_compute('$SVM_input/horizontal_normalized_histograms.txt'); cd $current_dir"

python $current_dir/vertical_normalize.py $SVM_input/horizontal_normalized_histograms.txt $SVM_input/mean_norm.txt $SVM_input/std_dev_norm.txt $SVM_input

