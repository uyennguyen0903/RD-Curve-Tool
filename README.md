# RD-Curve-Tool

Tool to visualize Rate-distortion (R-D) curves for image compression.

Additional utilities:
- R-D curve prediction for a given list of qualities of lossy encode.
- Generate data by extracting frames from high resolution YouTube videos.

# Prerequisites
- [libwebp](https://github.com/webmproject/libwebp)
- [matplotlib](https://matplotlib.org/users/installing.html)
- For building dataset:
    - [OpenCV](https://opencv.org)
    - pytube
- For R-D curve prediction:
    - scipy

## R-D curve plot

Draw meta curves (lossy, lossless or near-lossless) for multiple directories containing images with.

### Usage

#### Tool written in Python

- plot R-D curves with lossy compression:

`python3 ./plot_curve/lossy.py dir_1 dir_2 ... dir_n`

- plot R-D curves with lossless compression:

`python3 ./plot_curve/lossless.py dir_1 dir_2 ... dir_n`

- plot R-D curves with near-lossless compression:

`python3 ./plot_curve/near-lossless.py dir_1 dir_2 ... dir_n`

- plot R-D curves (lossy and near-lossless) for each frame of animation stored in a directory (*lossy.py and near-lossless.py must be doned before running this file*):

`python3 ./plot_curve/draw-mixed-curves.py anim_dir`

*The resulting R-D curves saved in the sub-folder named "Results".* 

#### Tool written in Bash:

`./plot_curve/metacurve.sh dir_1 dir_2 ... dir_n`

You can also draw data files generated by `metacurve.sh` with `plot_metacurve.sce`.

### Examples

#### `lossy.py`

`python3 ./plot_curve/lossy.py ./anim`

![Lossy example](/examples/lossy.png)

#### `draw-mixed-curves.py`

`python3 ./plot_curve/lossless.py ./anim`

![Lossless example](/examples/lossless.png)

## R-D curve prediction

Predict the R-D curve for lossy compression method from a given list of qualities. 

### Usage

`python3 ./extras/curve_fitting img_path math_model quality_1 quality_2 ... quality_n`

`math_model` available in this tool is:
- `poly` : polynomial model psnr = c_1 + c_2 * size + c_3 * size^2 + ... + c_n * size^(n-1)
- `log` : logarithmic model psnr = a * log(b * size) + c

If the given list of qualities is empty, the tool will choose 7 points on R-D curve for curve-fitting process.

In this tool, the Levenberg-Marquardt algorithm is used to predict the curves by minimizing the sum of squares of non-linear functions (`leastsq`).

### Example

`python3 ./extras/curve_fitting.py ./examples/anim/frame100.png poly 0 50 75 88 94 97 100`

![Poly model example](/examples/frame100curve_fit.png)

`python3 ./extras/curve_fitting.py ./examples/anim/frame100.png log 0 50 90 92 100`

![log model example](/examples/frame100curve_fit_log.png)
## Generate data

### Usage

Download high resolution videos from YouTube.

`python3 ./extras/downloader.py url_1 url_2 .. url_n`

Extract and resize frames from video.

`python3 ./extras/dump_frames.py video_path num_frame dst_dir new_width new_height`

### Examples

`python3 ./extras/downloader.py https://youtu.be/FUiu-cdu6mA`

`python3 ./extras/dump_frames.py ./eve_online.mp4 100 ./Frames 320 180`


*Last updated : 09/20/2020.*