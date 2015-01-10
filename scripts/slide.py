import sys

def createFile(m):
	filename= "window"+ str(m)
	file= open(filename, 'w')
	return file



f=open('accumulated_file_test.txt','r')
fp= open('slidingwindows40.txt', 'a')
file_content = []
file_content = f.readlines()

#input file contains frames
#window size: 80 frames, 2 s  
#frame size= 25ms 
#slide size: 10 frames ~ 0.2 s

frame_cnt = 0
ending_frame=40
m=1  #file_count

while ending_frame < len(file_content):
	
  #fp=createFile(m)
  m=m+1
  for i in range(frame_cnt , ending_frame):
	  fp.write(file_content[i])
    
  frame_cnt=frame_cnt+10
  ending_frame= frame_cnt+40

# remaining jotting down in one file not essentially of size 80
#fp=createFile(m)
for i in range(frame_cnt , len(file_content)):
	  fp.write(file_content[i])
  

fp.close()


