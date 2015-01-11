Project Description: 
=========================
NEVER ENDING LEARNING OF SOUND: 
=========================
The world is full of sounds which carry a wealth of information about the processes that create them. Nature has its own grammar in the sense that the sounds follow certain rules that humans can understand intuitively, but this information is unusable by machines. The NELS team is developing a web-based intelligence system that will continually search the internet for sound samples and automatically learn their meanings, associations, and semantics. This is an ambitious, long-term project that is literally intended to never end.


OPENSMILE INSTALLATION SCRIPT
=========================

Run following cmd to install opensmile and all its dependencies.
 
bash opensmile/install_opensmile.sh


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


Project Contributors:
=========================

The following is the NELS Team. We are developing a web-based intelligence system that will continually search the internet for sound samples and automatically learn their meanings, associations, and semantics. If you have any questions or want to contribute, contact:

Rohan Badlani, 3rd year undergraduate student, Computer Science, BITS Pilani (rohan.badlani@gmail.com)

Aditi Bhatnagar, 3rd year undergraduate student, Information and Communication Technology, DAIICT (aditi24.bhatnagar@gmail.com)

Amogh Hiremath, 1st year M.Tech Student, Electronics and Communication, NIT Surathkal (amogh3892@gmail.com)

Ankit Shah, 4th year undergraduate student, Electronics and Communication, NIT Surathkal (ankit.tronix@gmail.com)

Parnika Nevaskar, 2nd year undergraduate student, Computer Science, DAU Indore, (parnika.nevaskar@gmail.com)

The developers of the project would like to thank Prof Bhiksha Raj, CMU, Prof Rita Singh, CMU and Pulkit Agrawal, PhD Student, UCB for their suggestions and guidance throughout the execution of this project.

