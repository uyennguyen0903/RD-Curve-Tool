#! /bin/bash
# call cwebp in a loop. 

num_pic=23
pic_width=320
pic_height=180

echo "" > data.dat
echo "" > data.txt

g++ gen_data.cpp -o gen_data
./gen_data cwebp_list.txt $num_pic png

j=0
while IFS= read -r line; do
	i=0
	while (( $i<=100 ))
	do
		cwebp -q $i -m 4 -print_psnr -short $line &>> data.dat
		i=$(( i+1 ))
	done
done < cwebp_list.txt

g++ calc.cpp -o calc
./calc data.dat data.txt $num_pic $pic_width $pic_height
