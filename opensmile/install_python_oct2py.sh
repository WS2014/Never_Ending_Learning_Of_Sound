!usr/bash

result=${PWD}

echo "Everything will be done in this directory."
echo $result
sudo yum install python-virtualenv python-pip
sudo apt-get install python-virtualenv python-pip
sudo yum-builddep python-numpy python-scipy
sudo apt-get build-dep python-numpy python-scipy
sudo pip install oct2py
sudo yum install python-scipy
sudo apt-get install python-scipy
