# RD-Curve-Tool

Tool to draw RD-curves, download high resolution videos from Youtube, extract and resize frames from videos. 

## Extract frames tool

Extract and resize frames from video.

**Prerequisite**

- [OpenCV](https://opencv.org)

**Usage**

`python3 dump_frames.py video_path num_frame dst_dir new_width new_height`

**Examples**

`python3 dump_frames.py ./eve_online.mp4 100 ./Frames 320 180`

## Youtube video downloader

Download high resolution videos from Youtube.

**Prerequisite**

- pytube

**Usage**

`python3 downloader.py url_1 url_2 .. url_n`

## RD-curves drawing tool

Draw meta curves (lossy, lossless or near-lossless) for several directories containing images with.

**Prerequisites**

- [libwebp](https://github.com/webmproject/libwebp)
- [matplotlib](https://matplotlib.org/users/installing.html)

**Usage**

**1. Tool written in Python:**

- Draw RD-curves with lossy compression:

`python3 lossy.py dir_1 dir_2 ... dir_n`

- Draw RD-curves with lossless compression:

`python3 lossless.py dir_1 dir_2 ... dir_n`

- Draw RD-curves with near-lossless compression:

`python3 near-lossless.py dir_1 dir_2 ... dir_n`

- Draw mixed curves (lossy and near-lossless) for each frame of animation stored in a directory (*lossy.py and near-lossless.py must be doned before running this file*):

`python3 draw-mixed-curves.py dir_name`

**2. Tool written in Bash:**

`./metacurve.sh dir_1 dir_2 ... dir_n`

You can also draw data files generated by `metacurve.sh` with `plot_metacurve.sce`.

## Examples

### `lossy.py`

`python3 lossy.py ./anim`

![Lossy example](/examples/lossy.png)

### `lossless.py`

`python3 lossless.py ./anim`

![Lossless example](/examples/lossless.png)

### `lossless.py`

`python3 near-lossless.py ./anim`

![Near-lossless example](/examples/near-lossless.png)

### `draw-mixed-curves.py`

`python3 draw-mixed-curves.py ./anim`

![Mixed-curves example](/examples/frame3.png)

