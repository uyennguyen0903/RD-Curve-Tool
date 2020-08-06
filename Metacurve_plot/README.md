# Metacurve_plot

Display multiple metacurves for a directory containing several WebP animations.

The tool dumps each WebP animation into frames using **anim_dump** API and then calls **cwebp** API in a loop to display metacurves with -q in range [0..100].

The resulting data containing PSNR and sizes of frames for each animations is saved in the directory ./Animations/Data.

## Prerequistes
- [libwebp](https://github.com/webmproject/libwebp)
- [Scilab](https://www.scilab.org/)
- [imagemagick](https://packages.ubuntu.com/search?keywords=imagemagick)

## Usage
1. Create a directory named Animations containing several WebP animations.
2. Run `./gen_metacurve.sh`
3. Plot the resulting data with **plot_metacurve.sce**
