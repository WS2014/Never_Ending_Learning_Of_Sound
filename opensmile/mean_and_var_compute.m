function[] = mean_and_var_compute (filename)

A = load(filename);
[m,n] = size(A); 
for j = 1:n
   B = A(1:m,j);
   me_an = mean(B);
   std_dev = std(B);
   meanval(1,j) = me_an;
   stdval(1,j) = std_dev;
end

dlmwrite('mean_norm.txt',meanval);
dlmwrite('std_dev_norm.txt',stdval);
end

