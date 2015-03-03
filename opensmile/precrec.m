function res = precrec(ytrue, ypred, drawgraphs,L)

% PRECREC : does precision-recall analysis for binary classification
% ytrue is a N-element vector with the true labels
%   the classes in ytrue are integers A and B , where A<B
% ypred is a N-element vector with the algorithm's output
%   ypred should be higher the more the algorithm thinks the label is B
% drawgraphs is 1 by default, set to 0 if you don't want 
%   any graphs drawn.
% L (=100 by default) is the number of thresholds you want to try
% res is a struct with precision/recall/Fscores for each of the 
%   L thresholds tried. Apart from cm (which is a 1xL cell array), 
%   all fields below are 1xL vectors.
%   .thresh   At the i-th threshold, anything below thresh(i) is classified A
%               and anything above it is classified as B.
%   .precA    precision for class A 
%              (e.g. precA(i) = precision for A at i-th threshold) 
%   .recA     recall for class A
%   .FA       F-score for class A
%   .precB    precision for class B
%   .recB     recall for class B
%   .FB       F-score for class B
%   .ac       unweighted accuracy
%   .wac      accuracy if examples are weighted by their inverse class probabilities 
%               (equivalent to the mean precision (precA+precB)/2
%   .cm       cm{i} has confusion matrix for i-th threshold
%   
%
% Note: ROC curves are not precision-recall curves!
%     if the classes are {negative,positive} then an ROC curve
%     is false positive rate(=1-true negative rate) VS true positive rate
%     i.e. 1-precision for negatives VS precision for positives
%
% 

if nargin<3
  drawgraphs=1;
end
if nargin<4
  L=100;
end



classes = sort(unique(ytrue));  % = [A B]
if (length(classes)~=2)
  error('not a binary classification problem');
end
N=length(ytrue);
YTRUE=zeros(N,1);          
YTRUE(find(ytrue==classes(2)))=1;
  
% y is like ytrue but with only 0 and 1 classes

predvals = sort(ypred);  

a=min(predvals); 
b=max(predvals);
bins=interp1(1:N,predvals,1:(N-1)/(L-1):N);

% bins have approximately equal number of samples in them

[h,h2]=hist(ypred,bins);

for i=1:L
  res.thresh(i)=bins(i);
  YPRED = zeros(N,1);
  YPRED(find(ypred > res.thresh(i))) = 1;
  [cm,nc,prec,rec,fscore]=getcm(YTRUE,YPRED,[0 1]);
  res.cm{i} = cm;
  res.ac(i) = nc/N;
  res.wac(i) = mean(prec);
  res.precA(i) = prec(1);
  res.precB(i) = prec(2);
  res.recA(i) = rec(1);
  res.recB(i) = rec(2);
  res.FA(i) = fscore(1);
  res.FB(i) = fscore(2);
end

if drawgraphs
  figure;
  subplot(2,3,1); 
    plot(res.recA,res.precA,'r-',res.recA,res.precA,'bo'); 
    xlabel('recall');
    ylabel('precision');
    title(sprintf('precision/recall for class %d',classes(1)));
    axis([0 1 0 1]);
  
  subplot(2,3,2); 
    plot(res.recB,res.precB,'r-',res.recB,res.precB,'bo'); 
    xlabel('recall');
    ylabel('precision');
    title(sprintf('precision/recall for class %d',classes(2)));
    axis([0 1 0 1]);

  subplot(2,3,3); 
    plot(res.FA,res.FB,'r-',res.FA,res.FB,'bo'); 
    xlabel(sprintf('F-score for class %d',classes(1)));
    ylabel(sprintf('F-score for class %d',classes(2)));
    title('Fscores');  
    axis([0 1 0 1]);
    
    
  subplot(2,3,4);
    plot(res.precA,res.precB,'r-',res.precA,res.precB,'bo'); 
    xlabel(sprintf('precision for class %d',classes(1)));
    ylabel(sprintf('precision for class %d',classes(2)));
    title('Precision');
    
  subplot(2,3,5);
    plot(1-res.precA,res.precB,'r-',1-res.precA,res.precB ,'bo'); 
    xlabel(sprintf('1-True class%d rate',classes(1)));
    ylabel(sprintf('True class%d rate',classes(2)));
    title('ROC curve');    
    axis([min(1 - res.precA) max(1 - res.precA) min(res.precB) max(res.precB)]);
    
  subplot(2,3,6); 

    plot(res.thresh,res.wac,'r-',res.thresh,res.ac,'r--');
    legend('weighted','unweighted');
    hold on; plot(res.thresh,res.wac,'bo');
    xlabel('threshold');
    ylabel('accuracy');
    title('accuracy (un/weighted by 1/class prob)');
    axis([min(res.thresh) max(res.thresh) 0 1]);

    print -djpg image.jpg
    hold on;
end
