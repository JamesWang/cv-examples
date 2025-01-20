"""
Introduction to thresholding techniques
"""

# Import required packages:
from functools import partial

from utils.helper import prepare_image
from utils.sample_img import build_sample_image
from utils.show_img import thresholding_and_show, show_img_with_matplotlib, init_display


show_img_with = partial(show_img_with_matplotlib, m=7, n=1)

if __name__ == "__main__":
    # Create the dimensions of the figure and set title and color:
    th_array = [0, 50, 100, 150, 200, 250]
    image = prepare_image(
        build_sample_image,
        show_img_with,
        f"img with tones of gray - left to right: {th_array}",
        title="Thresholding introduction")
    thresholding_and_show(threshold_arr=th_array, image=image, show_img=show_img_with)
