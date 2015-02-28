#!usr/bash

#supply the folder here
current_dir=${PWD}
sound_samples_folder="sound_samples_test"
text_mfcc_folder="$current_dir/text_samples_folder_test"
accumulation_folder="$current_dir/accumulated_folder_test"
kmeans_output="$current_dir/kmeans_output"
text_histogram_folder="$current_dir/text_histogram_folder_test"
text_histogram_folder_norm="text_histogram_folder_norm_test"
SVM_input="$current_dir/SVM_input_test"
#Change this part to make it create a folder whenever there is a folder created using the python slide.py code 
#For now even if it is hard coded it is fine but this needs to be based on a condition for the folder created
slides_80_10="$current_dir/slides_80_10"
slides_80_20="$current_dir/slides_80_20"

rm -r $text_histogram_folder 
rm $accumulation_folder/accumulation_after_slide.txt
mkdir -p $text_mfcc_folder
mkdir -p $accumulation_folder
mkdir -p $text_histogram_folder
mkdir -p $kmeans_output
mkdir -p $text_histogram_folder_norm
mkdir -p $SVM_input
mkdir -p $slides_80_10 
mkdir -p $slides_80_20

python $current_dir/slide.py $accumulation_folder/normalized_text.txt 80 10 slides_80_10

for file_histogram in `ls $slides_80_10/*`
do
 	cat $file_histogram >> $accumulation_folder/accumulation_after_slide.txt
done

python $current_dir/assignment_test1.py $accumulation_folder $kmeans_output $accumulation_folder

python $current_dir/split.py  $accumulation_folder/assignment_test.txt 80 $text_histogram_folder
for txt_file in $text_histogram_folder/* 
do
         text_file_root=`echo $txt_file | sed -e s/text_histogram_folder/text_histogram_folder_norm/`  
         text_file=`echo $text_file_root | sed -e s/$/.txt/`  
         INP_FILE=$txt_file
         OUT_FILE=$text_file  
         echo "'$INP_FILE' '$OUT_FILE'"
         octave -qf --eval "addpath('$current_dir'); cluster2bins_test('$INP_FILE','$OUT_FILE')"
done
python $current_dir/accumulation_test.py $text_histogram_folder_norm $SVM_input

# #for file_hist  in `ls $text_histogram_folder_norm/*`
# #do
# #	cat $text_histogram_norm/*.txt >> $SVM_input/accumulated_file.txt
# #done
python $current_dir/horizontal_normalize.py $SVM_input/accumulated_file.txt $SVM_input

octave -qf --eval "cd $SVM_input ;addpath('$current_dir'); mean_and_var_compute('$SVM_input/horizontal_normalized_histograms.txt'); cd $current_dir"

python $current_dir/vertical_normalize.py $SVM_input/horizontal_normalized_histograms.txt $SVM_input/mean_norm.txt $SVM_input/std_dev_norm.txt $SVM_input

