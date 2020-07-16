#! /bin/bash
# call cwebp in a loop. 

i=0

while (( $i<=100 ))
do
	cwebp -q $i -m 6 -print_psnr -short bird.png -o bird.webp &>> data6.txt
	cwebp -q $i -m 4 -print_psnr -short bird.png -o bird.webp &>> data4.txt
	cwebp -q $i -m 0 -print_psnr -short bird.png -o bird.webp &>> data0.txt
	i=$(( i+1 ))
done
