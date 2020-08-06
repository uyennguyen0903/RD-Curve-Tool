tmp = read('data1.txt',-1,2);
data = tmp(2:size(tmp,'r'),:);
data(:,1) = data(:,1)/(tmp(1,1)*tmp(1,2));

clf();
xlabel("Bit-rate","fontsize", 4);
ylabel("PSNR","fontsize", 4);
title("Metacurve","fontsize", 6)

ind = 1;
num_pic = size(data, 'r') / 101;
for i = 1 : num_pic
    t = data(ind:(ind+100),:);
    plot(t(:,1),t(:,2),'b-',"marker");
    ind = ind + 100 + 1; 
end
