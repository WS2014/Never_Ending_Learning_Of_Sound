function cluster2bins_test(input_file,output_file) 

disp(input_file) ;
disp(output_file);
    A = load(input_file);
    B = A(:,1);
    B = B';
    Y = hist(B,200);
dlmwrite(output_file,Y,' ');

end