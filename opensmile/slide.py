import sys
import os
def createFile(dir_name,file_for_slide_to_generate,m):
	filename= file_for_slide_to_generate+ "window"+ str(m)
	file= open(dir_name+"/"+filename, 'w')
	return file


def generateSlides(directory_name, file_name, sws, ss):
	f=open(file_name,'r')
	dir_name= str(directory_name)	
	create_dir_cmd ="mkdir "+dir_name
	os.system(create_dir_cmd)
	
	#fp= open('slidingwindows40.txt', 'a')
	file_content = []
	file_content = f.readlines()

	#input file contains frames
	#window size: 80 frames, 2 s :sws  
	#frame size= 25ms 
	#slide size: 10 frames ~ 0.2 s : ss

	frame_cnt = 0
	ending_frame= sws
	m=1  #file_count

	# if os.path.isfile('filename')
	while ending_frame < len(file_content):
	
	  fp=createFile(dir_name,file_for_slide_to_generate,m)
	  m=m+1
	  for i in range(frame_cnt , ending_frame):
		  fp.write(file_content[i])
	    
	  frame_cnt=frame_cnt+ss
	  ending_frame= frame_cnt+sws
	# filename="window" + str(m)
	# try:
	#     with open('filename') as file:
 #        	pass
	# except IOError as e:
	# 	m=m+1
 #    	print "Unable to open file" #Does not exist OR no read permissions
	# remaining jotting down in one file not essentially of size 80
	fp=createFile(dir_name,file_for_slide_to_generate,m)
	for i in range(frame_cnt , len(file_content)):
		  fp.write(file_content[i])
	  

	fp.close()

if(len(sys.argv)!=6):
    print "\nUSAGE: python slide.py <normalized file> <slide window size eg. 80> <slide size eg 10> <directory name for sliding> <filename for which slide is supposed to run>\n" 
else:
    file_name = ""
    file_name = str(sys.argv[1])
    sws=int(sys.argv[2])
    ss=int(sys.argv[3])
    directory_name=str(sys.argv[4])
    file_for_slide_to_generate=str(sys.argv[5])
    generateSlides(directory_name, file_name, sws, ss)
