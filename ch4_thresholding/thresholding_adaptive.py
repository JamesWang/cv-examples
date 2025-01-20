"""
Adaptive thresholding
"""

# Import required packages:
from functools import partial

import cv2
from matplotlib import pyplot as plt

from utils.helper import prepare_image, loader
from utils.show_img import show_img_with_matplotlib
from collections import namedtuple

Params = namedtuple('Param', 'method type block_size C')

show_img_with = partial(show_img_with_matplotlib, m=2, n=3)


if __name__ == "__main__":
    gray_image = prepare_image(loader('../images/sudoku.png'), show_img_with, "img", title="Thresholding Adaptive")

    params = [
        Params(cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, 2)
        , Params(cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 31, 3)
        , Params(cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)
        , Params(cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 31, 3)
    ]
    show_img_with(cv2.cvtColor(gray_image, cv2.COLOR_GRAY2BGR), "gray img", 1)
    # Perform adaptive thresholding with different parameters:
    for idx, p in enumerate(params):
        thresh = cv2.adaptiveThreshold(gray_image, 255, p.method, p.type, p.block_size, p.C)
        show_img_with(
            cv2.cvtColor(thresh, cv2.COLOR_GRAY2BGR),
            f"method={p.method}, blockSize={p.block_size}, C={p.C}",
            2 + idx
        )

    # Show the Figure:
    plt.show()
