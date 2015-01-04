function[] = norm_column_train(filename)

A = load(filename);
[m,n] = size(A); 

normalized = zeros(m,n);
for j = 1:n
   B = A(1:m,j);
   me_an = mean(B);
   std_dev = std(B);
   meanval(1,j) = me_an;
   stdval(1,j) = std_dev;
   normalized(:,j) = (A(:,j) -me_an )./ std_dev ;  
end

temp = normalized;
normalized(1:m,1) = 1:m;
normalized(1:m,2:n+1) = temp;  
[m,n] = size(normalized);
disp(n);

dlmwrite('normalized_text.txt',normalized,' ');
dlmwrite('mean_norm.txt',meanval);
dlmwrite('std_dev_norm.txt',stdval);
end

