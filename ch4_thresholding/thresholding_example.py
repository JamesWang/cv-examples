"""
Simple thresholding applied to a real image
"""

# Import required packages:
from functools import partial

from utils.helper import prepare_image, loader
from utils.show_img import show_img_with_matplotlib, thresholding_and_show


show_img_with = partial(show_img_with_matplotlib, m=3, n=3)

if __name__ == "__main__":
    th_array = [60, 70, 80, 90, 100, 110, 120, 130]
    image = prepare_image(loader('../images/sudoku.png'), show_img_with, "img", title="Thresholding example")
    thresholding_and_show(threshold_arr=th_array, image=image, show_img=show_img_with)

