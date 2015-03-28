function file_files_greater_than_a_confidence_level(input_file,output_file)
y = load(input_file)
y1 = y(:,2)
p = find(y1>0.7)
dlmwrite(output_file,p)

