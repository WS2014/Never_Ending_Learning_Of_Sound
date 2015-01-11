#!usr/bash

result=${PWD}

echo "Everything will be done in this directory."
echo $result

wget http://www.csie.ntu.edu.tw/~cjlin/cgi-bin/libsvm.cgi?+http://www.csie.ntu.edu.tw/~cjlin/libsvm+tar.gz
mv libsvm.cgi\?+http\:%2F%2Fwww.csie.ntu.edu.tw%2F~cjlin%2Flibsvm+tar.gz libsvm.tar.gz
tar -zxvf libsvm.tar.gz
cd $result/libsvm-3.20
make
cd $result
