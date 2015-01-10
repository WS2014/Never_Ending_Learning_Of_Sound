#!usr/bash

#code to get the MFCC for all sample files for the test database.
bash get_mfcc_for_samples_test.sh

#code to get the accumulated MFCC File
mkdir -p accumulated_folder_test
python accumulation.py text_samples_folder_test accumulated_folder_test

#code to normalize the accumulated file. The Mean and Variance are taken from the accumulated folder where the training data values are stored in mean_norm.txt and std_dev.txt
bash autonorm_test.sh

