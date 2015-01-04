#!usr/bash

#get the package for Parallel Net CDF
wget -np http://cucis.ece.northwestern.edu/projects/PnetCDF/Release/parallel-netcdf-1.5.0.tar.gz

#Requires installation of MPI C Compiler.
#Extract the downloaded package
gunzip parallel-netcdf-1.5.0.tar.gz
tar xf parallel-netcdf-1.5.0.tar
cd parallel-netcdf-1.5.0

#Configure PnetCDF specifying the installation directory:
./configure --prefix=$HOME/PnetCDF

#Build PnetCDF:
make

#Install PnetCDF
make install

#Test
PATH=$HOME/PnetCDF/bin:$PATH ; export PATH
which ncmpidump
which ncmpidiff

echo "SUCCESSFULLY INSTALLED Parallel Net CDF"

