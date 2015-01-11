import re
import sys

def frameStrtEnd(strtfn, num_fr):
	val= 0.25*(strtfn-1)
	return(val, val + 2+0.25*(num_fr-1))   # returns start time and end time in s 


def generateDurations(file_name):
	
	fp= open(file_name)    # result from svm
	ano=open(file_name+'_durations','w')

	lines= fp.readlines()

	flines=[]
	for x in lines:
		v=re.split('\n',x)[0]
		if (v != ''):
			flines.append(int(v))

	fc=0
	cnt=0
	pv=0
	st=1

	for u in flines:
		fc=fc+1
		if (u==1):
			cnt=cnt+1
			if(pv!=1):
				st=fc
				pv=1

		else:
			if (pv==1):
				strt,end =frameStrtEnd(st, cnt)
				if strt!=end:
					ano.write(str(strt)+":"+str(end)+"\n")
			cnt=0
			pv=-1


if(len(sys.argv)!=2):
    print "\nUSAGE: python owindow_slide.py <svm output file> \n" 
else:
    file_name = ""
    file_name = str(sys.argv[1])
    generateDurations(file_name)
