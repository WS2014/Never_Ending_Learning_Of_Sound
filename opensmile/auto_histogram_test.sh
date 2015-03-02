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

split_output="$current_dir/split_output"
slide_80_10="$current_dir/slide_80_10"
rm -r $split_output
rm -r $text_histogram_folder 
rm -r $text_histogram_folder_norm
rm -r $slide_80_10
rm -r $text_histogram_folder
rm $accumulation_folder/accumulation_after_slide.txt
rm $SVM_input/accumulated_file.txt
mkdir -p $text_mfcc_folder
mkdir -p $accumulation_folder
mkdir -p $text_histogram_folder
mkdir -p $kmeans_output
mkdir -p $text_histogram_folder_norm
mkdir -p $SVM_input
mkdir -p $slides_80_10 
mkdir -p $slides_80_20
mkdir -p $accumulation_after_slide
mkdir -p $split_output
mkdir -p $slide_80_10

python $current_dir/splitter_test.py $accumulation_folder $accumulation_folder $split_output
#------------------------------------------------------------------------------------------------------------------------------------------------
# The Below for loop generates a sliding windows for each file and places them in a separate folder as per the original file names and window
#------------------------------------------------------------------------------------------------------------------------------------------------
for insubdir in `ls -d $split_output/*`
do
	echo "$insubdir"
 	folder=`echo "${insubdir##/*/}"`
	   echo "$folder"
	 # dirname=`echo $insubdir | sed "s/^$temp_output//"` 
	 # echo "$dirname"
	new_folder="$slide_80_10/$folder"
	mkdir -p $new_folder
	for text_file in `ls $insubdir/*.txt`
	do
	echo "$text_file"
	text_file_name=`echo "${text_file##/*/}"`
	echo "$text_file_name"
	python $current_dir/slide.py $text_file 80 10 $new_folder $text_file_name
	done
done

#-----------------------------------------------------------------------------------------------------------------------------------------------------
# The Below for loop does assignment for each file generated during the above step and then does assignment using the normalised cluster centres file
#-----------------------------------------------------------------------------------------------------------------------------------------------------
for insubdir1 in `ls -d $slide_80_10/*`
do
	echo "$insubdir1"
 	folder1=`echo "${insubdir1##/*/}"`
	   echo "$folder1"
	mkdir -p $text_histogram_folder/$folder1
	for text_file1 in `ls $insubdir1/*`
	do
	echo "$text_file1"
	text_file_name1=`echo "${text_file1##/*/}"`
	echo "$text_file_name1"
	python $current_dir/assignment_test1.py $text_file1 $kmeans_output $text_histogram_folder/$folder1/$text_file_name1
	done
done	

#-------------------------------------------------------------------------------------------------------------------------------------------------------------
#The Below for loop copies the files into a new folder text_histogram_folder_norm and computes the histograms [unnormalised] for each of the sliding window
#-------------------------------------------------------------------------------------------------------------------------------------------------------------
for insubdir2 in `ls -d $text_histogram_folder/*` 
do
	echo "$insubdir2"
 	folder2=`echo "${insubdir2##/*/}"`
	   echo "$folder2"
	   mkdir -p $text_histogram_folder_norm/$folder2
	for txt_file in `ls $insubdir2/*`
	do 
         text_file_root=`echo $txt_file | sed -e s/text_histogram_folder/text_histogram_folder_norm/`  
         text_file=`echo $text_file_root | sed -e s/$/.txt/`  
         INP_FILE=$txt_file
         OUT_FILE=$text_file  
         echo "'$INP_FILE' '$OUT_FILE'"
         octave -qf --eval "addpath('$current_dir'); cluster2bins_test('$INP_FILE','$OUT_FILE')"
    done
done

#------------------------------------------------------------------------------------------------------------------------------------------
# Accumulate the generated files into a new folder SVM_input_test with the filename accumulated_text.txt and category wise number of files
#------------------------------------------------------------------------------------------------------------------------------------------
python $current_dir/accumulation.py $text_histogram_folder_norm $SVM_input


#----------------------------------------------------------------------------------------------------------------------------------------------------
# Below steps are for the normalization of the above file histograms generated both horizontally and vertically as similar done in the training case
#----------------------------------------------------------------------------------------------------------------------------------------------------

python $current_dir/horizontal_normalize.py $SVM_input/accumulated_file.txt $SVM_input

octave -qf --eval "cd $SVM_input ;addpath('$current_dir'); mean_and_var_compute('$SVM_input/horizontal_normalized_histograms.txt'); cd $current_dir"

python $current_dir/vertical_normalize.py $SVM_input/horizontal_normalized_histograms.txt $SVM_input/mean_norm.txt $SVM_input/std_dev_norm.txt $SVM_input