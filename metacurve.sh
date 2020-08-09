#! /bin/bash
START=$(date +%s)

function anim_process(){
    local quality=0
    while (( $quality<=100 )); do
        cwebp -q $quality -print_psnr -short ${logfiles[$ind_pic]} -o $param/out.webp &>> $param/data$ind_pic.txt
        quality=$(( quality+1 ))
    done
    echo "${logfiles[$ind_pic]} $timestamp" &>> $param/frames.txt

  	~/step255-2020/build/thumbnailer $param/frames.txt $param/anim.webp $param/points.txt
    python3 vdata.py $param $param/plot.png
}

for param in "$@"
do
    shopt -s globstar
	rm $param/*.txt

    shopt -s nullglob
	logfiles=($param/*.png)
	num_pic=${#logfiles[@]}
   	num_pic=$(( num_pic-1 ))
    
    ind_pic=0
	timestamp=100
    while (( $ind_pic<=$num_pic )); do
        anim_process &
        ind_pic=$(( ind_pic+1 ))
        timestamp=$(( timestamp+100 ))
    done
    wait
done

END=$(date +%s)
DIFF=$(( $END - $START ))
echo "---------- $DIFF seconds ----------"
