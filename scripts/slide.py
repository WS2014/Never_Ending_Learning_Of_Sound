import sys
import os
def createFile(dir_name,m):
	filename= "window"+ str(m)
	file= open(dir_name+"/"+filename, 'w')
	return file


def generateSlides(file_name, sws, ss):
	f=open(file_name,'r')
	dir_name= "slides_" +str(sws)+"_"+str(ss)	
	create_dir_cmd ="mkdir "+dir_name
	os.system(create_dir_cmd)
	
	fp= open('slidingwindows40.txt', 'a')
	file_content = []
	file_content = f.readlines()

	#input file contains frames
	#window size: 80 frames, 2 s :sws  
	#frame size= 25ms 
	#slide size: 10 frames ~ 0.2 s : ss

	frame_cnt = 0
	ending_frame= sws
	m=1  #file_count

	while ending_frame < len(file_content):
	
	  fp=createFile(dir_name,m)
	  m=m+1
	  for i in range(frame_cnt , ending_frame):
		  fp.write(file_content[i])
	    
	  frame_cnt=frame_cnt+ss
	  ending_frame= frame_cnt+sws

	# remaining jotting down in one file not essentially of size 80
	fp=createFile(dir_name,m)
	for i in range(frame_cnt , len(file_content)):
		  fp.write(file_content[i])
	  

	fp.close()

if(len(sys.argv)!=4):
    print "\nUSAGE: python slide.py <normalized file> <slide window size eg. 80> <slide size eg 10>\n" 
else:
    file_name = ""
    file_name = str(sys.argv[1])
    sws=int(sys.argv[2])
    ss=int(sys.argv[3])
    generateSlides(file_name, sws, ss)

