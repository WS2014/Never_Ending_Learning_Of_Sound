#!usr/bash
bash install_opensmile.sh
bash get_mfcc_for_samples.sh
mkdir -p accumulated_folder
python accumulation.py text_samples_folder accumulated_folder
bash autonorm_train.sh
bash install_OpenMPI_Linux.sh
bash install_MPI_C_Compiler.sh
bash install_ParallelNetCDF.sh
