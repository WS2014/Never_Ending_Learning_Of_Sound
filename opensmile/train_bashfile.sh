#!usr/bash
bash install_opensmile.sh
bash get_mfcc_for_samples.sh
mkdir -p accumulated_folder
python accumulation.py text_samples_folder accumulated_folder
