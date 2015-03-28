function precision_recall_plot(input,output)
Y = load(input);
A = Y(:,1);
Y1 = load(output);
B = Y1(:,2);
res = precrec(A,B,1,100)

