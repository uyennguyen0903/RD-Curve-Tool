#! /bin/bash

function anim_process(){
    	mkdir ./Animations/anim$i
	~/libwebp/build/anim_dump -folder ./Animations/anim$i ./Animations/anim$i.webp
	~/libwebp/build/anim_dump -tiff -folder ./Animations/anim$i ./Animations/anim$i.webp
   	 identify -format '%w %h' ./Animations/anim$i/dump_0000.tiff &> ./Animations/Data/RD_data$i.txt
	echo "" &>> ./Animations/Data/RD_data$i.txt
	rm -rf ./Animations/anim$i/*.tiff
    
        shopt -s nullglob
	logfiles=(./Animations/anim$i/*.png)
	local num_pic=${#logfiles[@]}
   	num_pic=$(( num_pic-1))
    	if (( $num_pic>25 )); then
		num_pic=25
	fi

    	local ind_pic=0
	local timestamp=100
	while (( $ind_pic<=$num_pic )); do
		local quality=0
		while (( $quality<=100 )); do
            		if (( $ind_pic<10 )); then
    				cwebp -q $quality -m 4 -print_psnr -short ./Animations/anim$i/dump_000$ind_pic.png -o ./Animations/anim$i/dump_000$ind_pic.webp &>> ./Animations/Data/RD_data$i.txt
    			else
                		cwebp -q $quality -m 4 -print_psnr -short ./Animations/anim$i/dump_00$ind_pic.png -o ./Animations/anim$i/dump_00$ind_pic.webp &>> ./Animations/Data/RD_data$i.txt
            		fi
			quality=$(( quality+1 ))
		done
        	if (( $ind_pic<10 )); then
			echo "./Animations/anim$i/dump_000$ind_pic.webp $timestamp" &>> ./Animations/anim$i/frames$i.txt			
		else
			echo "./Animations/anim$i/dump_00$ind_pic.webp $timestamp" &>> ./Animations/anim$i/frames$i.txt
		fi
        	ind_pic=$(( ind_pic+1 ))
		timestamp=$(( timestamp+100 ))
	done 

  	#~/step255-2020/build/thumbnailer ./Animations/anim$i/frames$i.txt ./Animations/Data/output$i.webp ./Animations/Data/points$i.txt

	shopt -s globstar
	rm ./Animations/anim$i/*.png
}


shopt -s nullglob
logfiles=(./Animations/*.webp)
num_anim=${#logfiles[@]}

i=1

mkdir ./Animations/Data

while (( $i<=$num_anim ))
do
   	 anim_process &
   	 i=$(( i+1 ))
done

wait
echo "Done!!!"
