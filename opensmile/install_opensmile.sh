#!usr/bash

result=${PWD}


wget http://www.ee.ic.ac.uk/hp/staff/dmb/voicebox/voicebox.zip
unzip voicebox.zip -d voicebox

VOICEBOX_PATH=$result/voicebox/
HTKFILE=mfcc.htk
OUTFILE=mfcc.txt

octave -qf --eval "htk2txt('$HTKFILE','$VOICEBOX_PATH','$OUTFILE')"
