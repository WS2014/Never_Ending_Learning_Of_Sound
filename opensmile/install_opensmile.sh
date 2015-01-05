#!usr/bash

result=${PWD}

echo "Everything will be done in this directory."
echo $result

wget http://www.audeering.com/research-and-open-source/files/openSMILE-2.1.0.tar.gz
tar -zxvf openSMILE-2.1.0.tar.gz
sudo apt-get install build-essential libtool

#PORTAUDIO INSTALLATION
echo "run this in the directory where you want to install portaudio."
wget http://www.portaudio.com/archives/pa_stable_v19_20140130.tgz
sudo apt-get install libasound-dev
tar -zvxf pa_stable_v19_20140130.tgz
cd portaudio
./configure && make
sudo make install

#back to openSmile

cd ..

cd openSMILE-2.1.0

bash autogen.sh
./configure
sh buildWithInstalledPortAudio.sh
./SMILExtract -h

#./SMILExtract -C config/MFCC12_E_D_A.conf -I ./../1.wav -O ./../mfcc.htk
cd ..


wget http://www.ee.ic.ac.uk/hp/staff/dmb/voicebox/voicebox.zip
unzip voicebox.zip -d voicebox

VOICEBOX_PATH=$result/voicebox/
#HTKFILE=mfcc.htk
#OUTFILE=mfcc.txt

#octave -qf --eval "htk2txt('$HTKFILE','$VOICEBOX_PATH','$OUTFILE')"
