#!usr/bash

#code to get the MFCC for all sample files for the test database.
bash get_mfcc_for_samples_test.sh

mkdir -p accumulated_folder_test
python accumulation.py text_samples_folder_test accumulated_folder_test

