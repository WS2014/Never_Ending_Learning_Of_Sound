#!usr/bash

#supply the folder here
current_dir=${PWD}
freesounds=freesounds
freesounds_wav=freesounds_wav
mkdir -p $freesounds
mkdir -p $freesounds_wav

for insubdir in `ls -d $freesounds/*`
do
	echo "$insubdir"
	outsub_dir=`echo $insubdir | sed -e s/$freesounds/$freesounds_wav/`
	mkdir -p $outsub_dir
	echo "$outsub_dir"
	for mp3_file in $insubdir/*.mp3
	do
		wav_file_root=`echo $mp3_file | sed -e s/$freesounds/$freesounds_wav/`
		wav_file_name=`echo $wav_file_root | sed -e s/.mp3/.wav/`
		echo "$mp3_file"
		echo "$wav_file_name"
		sox $mp3_file -r 16000 -e signed-integer -b 16 -c 1 $wav_file_name.wav
	done
done

exit 0;