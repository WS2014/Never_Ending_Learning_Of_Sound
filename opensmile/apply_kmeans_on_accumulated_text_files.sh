#!usr/bash

#supply the folder here
current_dir=${PWD}
sound_samples_folder="sound_samples"
#voicebox_folder_name=$current_dir/"voicebox"
#echo $voicebox_folder_name
text_mfcc_folder="$current_dir/text_samples_folder"
accumulation_folder="$current_dir/accumulated_folder"
kmeans_output="$current_dir/kmeans_output"
#mkdir -p $text_mfcc_folder
#mkdir -p $accumulation_folder
mkdir -p $kmeans_output
#python accumulation_train.py $text_mfcc_folder $accumulation_folder

wget -nc 'users.eecs.northwestern.edu/~wkliao/Kmeans/parallel-kmeans.tar.gz'
tar -zxvf parallel-kmeans.tar.gz
cd parallel-kmeans
make
./omp_main -o    -n 200 -i $accumulation_folder/normalized_text.txt
mv $accumulation_folder/normalized_text.txt.cluster_centres $kmeans_output/normalized_text.txt.cluster_centres
mv $accumulation_folder/normalized_text.txt.membership $kmeans_output/normalized_text.txt.membership  
