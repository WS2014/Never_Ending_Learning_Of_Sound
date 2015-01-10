function[] = norm_column_test(filename)

A = load(filename);
[m,n] = size(A); 
S = load('accumulated_folder/std_dev_norm.txt');
M = load('accumulated_folder/mean_norm.txt');
normalized = zeros(m,n);
for j = 1:n
   B = A(1:m,j);
   me_an = M(1,j);
   std_dev = S(1,j);
   normalized(:,j) = (A(:,j) -me_an )./ std_dev ;  
end

temp = normalized;
normalized(1:m,1) = 1:m;
normalized(1:m,2:n+1) = temp;  
[m,n] = size(normalized);
disp(n);

dlmwrite('normalized_text.txt',normalized,' ');
end

