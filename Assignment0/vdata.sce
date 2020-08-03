data = read('data.txt', -1, 2);
points = read('points.txt', -1, 1);

clf();
xlabel("Bit-rate","fontsize", 4);
ylabel("PSNR","fontsize", 4);
title("Avengers Trailer - RD curve","fontsize", 6)

cnt = 0;
ind = 1;
num_pic = size(data, 'r') / 101;
num_point = size(points, 'r') / num_pic;
dem = 0;
res = [];
for i = 1 : num_pic
    tmp = i;
    for j = 1 : num_point
        final_ind = 0;
        dis = 200;
        for h = 0 : 100
            if (abs(data(ind+h,2)-points(tmp)) < dis) then
                dis = abs(data(ind+h,2)-points(tmp));
                final_ind = ind+h;
            end
         end
         res = [res; final_ind];
         if (j == num_point) then
            dem = dem + 1;
            plot(data(final_ind:final_ind,1),data(final_ind:final_ind,2),"go");
         else
            plot(data(final_ind:final_ind,1),data(final_ind:final_ind,2),"ro"); 
            dem = dem + 1;
         end
         tmp = tmp + num_pic;
    end
    t = data(ind:(ind+100),:);
    plot(t(:,1),t(:,2),'b-',"marker");
    ind = ind + 100 + 1; 
end
