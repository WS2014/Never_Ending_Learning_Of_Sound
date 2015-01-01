function htk2txt(htk_file,voicebox_path,text_file) 
addpath(voicebox_path);
[D,FP,DT,TC,T]=readhtk(htk_file); 
E=D(:,1:26);
#save text_file.mat E
#load('text_file.mat')
#save('text_file','-ascii')
dlmwrite(text_file,E,' ',0,0);
#[m,n] = size(D);
#for i = 1:m
#    E = (D(:,i) - mean(D(:,i)))/std(D(:,i));
#end
