#!usr/bash
#Install Open MPI 1.8 in Linux Based Systems using this bashscript
wget https://www.open-mpi.org/software/ompi/v1.8/downloads/openmpi-1.8.1.tar.gz
sudo apt-get install libibnetdisc-dev
tar -xvf openmpi-1.8.1.tar.gz
cd openmpi-1.8.1
./configure --prefix="/home/$USER/.openmpi"
make
sudo make install
export PATH="$PATH:/home/$USER/.openmpi/bin"
export LD_LIBRARY_PATH="$LD_LIBRARY_PATH:/home/$USER/.openmpi/lib/"
mpirun
echo "OPEN MPI INSTALLED SUCESSFULLY"
