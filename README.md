Project Description: NEVER ENDING LEARNING OF SOUND

About Never Ending Learning of Sound: 

The world is full of sounds which carry a wealth of information about the processes that create them. Nature has its own grammar in the sense that the sounds follow certain rules that humans can understand intuitively, but this information is unusable by machines. The NELS team is developing a web-based intelligence system that will continually search the internet for sound samples and automatically learn their meanings, associations, and semantics. This is an ambitious, long-term project that is literally intended to never end.

Approach to the Problem:

Step 1 :  Given any audio data as wav files only, classify the data into training set and the testing set. 
-------
Step 2 :  To maintain consistency, change the sampling frequency of the audio clip to 44100 Hz for improvement in the quality of the audio clip using the lame software library
-------
Step 3 :  After the change of frequency, use the openSMILE toolkit to extract features of the audio clip. (For our case, right now the MFCC features are extracted, The openSmile toolkit would give an output file with a .htk extension. This .htk file can be read in Octave with a readhtk function. The format of readhtk function is [D,FP,DT,TC,T]=readhtk('filename'). The desired matrix is stored in D. The D matrix contains 13 MFCC coefficients, 13 delta coefficients and 13 acceleration coefficients. Pick up the first 26 columns [13 MFCC and 13 delta coeffs] from the D matrix because 13 acceleration coefficients generally does not convey useful information thus leaving them out to reduce computation.)
-------
Step 4 :  Convert the .htk file to a .txt file with the help of octave using htk2txt.m file
-------
Step 5 :  After all the training files and testing files converted to .txt concatenate the training file into a single .txt file according to their order in folder.
-------
Step 6 :  Normalise the concatenated .txt file columnwise for a particular feature coefficient and save their u[mean] and sigma[stddev] values. [ Normalization is performed to get the data in a suitable range for better analysis of the data on a comparative scale ] 
-------
Step 7 :  Use the normalised coefficient file, apply Kmeans algorithm [done on training data] to find the cluster centers and their membership information 
-------
Step 8 :  With the cluster and membership information for the concatenated file, now find the cluster and membership for the individual files using the count of frames. This count for frames is the unnormalised bag of words representation for each audio file
------- 
Step 9 :  The Histogram file generated has to be normalized horizontally [that is divide by the sum of the frames] 
-------
Step 10 : Each of the horizontally normalized file needs to be concatenated to normalize them vertically and then split them back to individual files for the normalized bag of words representation.
-------
Step 11 : Now take a testing audio file and extract the MFCC coefficients using steps 3 and 4, then using the u[mean] and sigma[stddev] values obtained in step 6 perform the columnwise normalization.
-------
Step 12 : In the columnwise normalized file take a 1 second segment, may be and find the histogram representation for the 1 second segment and follow step 9 and then normalise this histogram file vertically with the u[mean] and sigma[stddev] values found in step 6 for this testing file.
-------
Step 13 : With the normalised file, find the nearest centroid location for each of the frames using the cluster_centers file generated in step 7 from the Kmeans algorithm and assign the membership value [cluster number] for the segment. 
-------
Step 14 : Repeat the same choosing a next segment of 1 second starting from 0.5-1.5 sec until the file completes and perform steps 12 and 13 on it and find the histogram representation for each of the sliding window
-------
Step 15 : The files generated in step 10 needs to be concatenated back into a single file and then after appending 1 for positives and 0 for the negative [wrt categories] and then convert to the file format needed for SVM training
-------
Step 16 : Similarly for file in step 14 apply the same step 15 needed for SVM predictio n[While conversion of the file to SVM file format 1 is for positives and -1 for negatives]
-------
Step 17 : Now generate a .model file by running the svm-train on the file generated from the step 15.
-------
Step 18 : Using the .model file test it against the test file generated using svm-predict
-------
Step 19 : The Predicted test file is used to draw the ROC Plots.
-------

Tools Used:

 openSMILE
   - open Speech and Music Interpretation by Large-space Extraction -
  Copyright (C) 2008-2013  Florian Eyben, Felix Weninger, Martin Woellmer, Bjoern Schuller
  
  Institute for Human-Machine Communication
  Technische Universitaet Muenchen (TUM)
  D-80333 Munich, Germany


About openSMILE:
================

openSMILE is a complete and open-source toolkit for audio analysis, processing and classification especially targeted at speech and music applications, e.g. ASR, emotion recognition, or beat tracking and chord detection.
The toolkit is developed at the Institute for Human-Machine Communication at the Technische Universitaet Muenchen in Munich, Germany.
It was started withtin the SEMAINE EU FP7 project.

==============================================================


Third-party dependencies:
=========================

openSMILE uses LibSVM (by Chih-Chung Chang and Chih-Jen Lin) for classification tasks. It is distributed with openSMILE and is included in the svm/ directory.

PortAudio is required for live recording from sound card and for the SEMAINE component.
You can get it from: http://www.portaudio.com
A working snapshot is included in thirdparty/portaudio.tgz

Optionally, openSMILE can be linked against the SEMAINE API and the Julius LVCSR engine, enabling an interface to the SEMAINE system and a keyword spotter component. See http://www.semaine-project.eu/ for details on running the SEMAINE system.

Moreover, there is an experimental dependency on the Speex Codec package for an echo cancellation component. By default openSMILE is compiled without this component, thus you do not require Speex. If you want to experiment with the echo cancellation feature, please read the unix build files and the speex echo canceller source files. 


Documentation/Installing/Using:
===============================

openSMILE is well documented in the openSMILE book, which can be found in doc/openSMILE_book.pdf.

For quick-start information on how to compile openSMILE, see the file INSTALL.

================================================================

Project Contributors:

The following is the NELS Team. We are developing a web-based intelligence system that will continually search the internet for sound samples and automatically learn their meanings, associations, and semantics. If you have any questions or want to contribute, contact:

1. Rohan Badlani, 3rd year undergraduate student, Computer Science, BITS Pilani (rohan.badlani@gmail.com)
2. Aditi Bhatnagar, 3rd year undergraduate student, Information and Communication Technology, DAICT (aditi24.bhatnagar@gmail.com)
3. Amogh Hiremath, 1st year M.Tech Student, Electronics and Communication, NIT Surathkal (amogh3892@gmail.com)
4. Ankit Shah, 4th year undergraduate student, Electronics and Communication, NIT Surathkal (ankit.tronix@gmail.com)
5. Parnika Nevaskar, 2nd year undergraduate student, Computer Science, DAU Indore, (parnika.nevaskar@gmail.com)


