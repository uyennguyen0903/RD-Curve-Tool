# RD-Curve-Tool

Tool to draw RD-curves and metacurves, download high resolution videos from Youtube, extract and resize frames from videos. 

## RD-curves drawing tool
Draw multiple metacurves for severals directories containing images.

**Prerequistes**
- [libwebp](https://github.com/webmproject/libwebp)
- [matplotlib](https://matplotlib.org/users/installing.html)

**Usage**
1. Tool written in Python: 

`python3 metacurve.py dir_1 dir_2 ... dir_n`

2. Tool written in Bash:

`./metacurve.sh dir_1 dir_2 ... dir_n`

## Extract frames tool
Extract and resize frames from video.

**Prerequistes**
- [OpenCV](https://opencv.org)

**Usage**

`python3 dump_frames.py video_path num_frame dst_dir new_width new_height`

**Examples**
`python3 dump_frames.py ./eve_online.mp4 100 ./Frames 320 180`

## Youtube video downloader
Download high resolution videos from Youtube.

**Usage**

**Prerequistes**
- pytube

`python3 downloader.py url_1 url_2 url_3 ..`



