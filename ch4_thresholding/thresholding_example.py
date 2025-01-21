"""
Simple thresholding applied to a real image
"""

# Import required packages:
from functools import partial

from utils.helper import prepare_image, deferred_img_loader, init_then_display_orig_img
from utils.show_img import show_img_with_matplotlib, thresholding_and_show


show_img_with = partial(show_img_with_matplotlib, m=3, n=3)

if __name__ == "__main__":
    th_array = [60, 70, 80, 90, 100, 110, 120, 130]
    orig_img, gray_image = prepare_image(deferred_img_loader('../images/sudoku.png'))

    init_then_display_orig_img(
        title="Thresholding example",
        show_orig_img=lambda: show_img_with(orig_img, "gray img", 1)
    )

    thresholding_and_show(threshold_arr=th_array, image=gray_image, show_img=show_img_with)

