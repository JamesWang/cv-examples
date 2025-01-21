"""
Introduction to thresholding techniques
"""

# Import required packages:
from functools import partial

from utils.helper import prepare_image, init_then_display_orig_img
from utils.sample_img import build_sample_image
from utils.show_img import thresholding_and_show, show_img_with_matplotlib, init_display

show_img_with = partial(show_img_with_matplotlib, m=7, n=1)

if __name__ == "__main__":
    # Create the dimensions of the figure and set title and color:
    th_array = [0, 50, 100, 150, 200, 250]
    orig_img, gray_image = prepare_image(
        build_sample_image,
    )

    init_then_display_orig_img(
        title='Thresholding introduction',
        show_orig_img=lambda: show_img_with(orig_img, f"img with tones of gray - left to right: {th_array}", 1)
    )

    thresholding_and_show(threshold_arr=th_array, image=gray_image, show_img=show_img_with)
