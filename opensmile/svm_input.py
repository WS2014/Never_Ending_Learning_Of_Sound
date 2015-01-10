# This file intends gerate normalized files of all files in given folder

import os
import sys
import re

def generateInputFile(norm_file, file_name, catg_name, output_file):
            
        with open(output_file, "w") as o_file:
            
            fp= open(norm_file)
            fp1= open(file_name)   

            lines= fp1.readlines()

            fterms=[]
            for x in lines:
                v=re.split(':',x)[0]
                if (v ==catg_name ):
                    fterms=re.split(':',x)
                    
                    break

            hist_lines= fp.readlines()

            i=0
            for x in hist_lines: 
                i=i+1
                if i >= int(re.split(',',fterms[2])[0]) and i<=int(fterms[3]):
                    val=1
                else:
                    val=-1

                o_file.write(str(val)+",")

                v=re.split(' ',x)
                
                for y in range(len(v)-1):
                    o_file.write(v[y]+",")
                o_file.write(v[len(v)-1]+"\n")

                


                
        fp.close()
        fp1.close()
        o_file.close()
                

if(len(sys.argv)!=4):
    print "\nUSAGE: python svm_input.py <normalized_file><Category file> <category name(all lower case one word)> \n"   #normalized_folder would have 2 files: first having the mean n variance, second the normalzed file
else:
    file_name = ""
    norm_file = ""
    catg_name = ""
    norm_file = str(sys.argv[1])
    file_name = str(sys.argv[2])
    catg_name = str(sys.argv[3])
    output_file= "svm_input_"+catg_name+".txt"
    generateInputFile(norm_file,file_name, catg_name, output_file)
