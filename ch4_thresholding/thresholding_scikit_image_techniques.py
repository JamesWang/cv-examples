"""
Thresholding example (Otsu's binarization algorithm) using scikit-image
"""

# Import required packages:
from functools import partial

import cv2
import matplotlib.pyplot as plt
from skimage.filters import (threshold_otsu, threshold_triangle, threshold_niblack, threshold_sauvola)
from skimage import img_as_ubyte

from utils.helper import init_then_display_orig_img, deferred_img_loader, prepare_image
from utils.show_img import show_single_channel

show_img_with = partial(show_single_channel, m=2, n=3)

if __name__ == "__main__":
    orig_img, gray_image = prepare_image(deferred_img_loader('../images/sudoku.png'))

    init_then_display_orig_img(
        title="Thresholding scikit-image (Otsu, Triangle, Niblack, Sauvola)",
        show_orig_img=lambda: show_img_with(orig_img, "Original Image", 1)
    )

    show_img_with(cv2.cvtColor(gray_image, cv2.COLOR_GRAY2BGR), "gray img", 2)

    # Calculate histogram (only for visualization):
    # hist = cv2.calcHist([gray_image], [0], None, [256], [0, 256])
    for idx, threshold in enumerate([
        (lambda: threshold_sauvola(gray_image, window_size=25), "Otsu's binarization (scikit-image)"),
        (lambda: threshold_niblack(gray_image, window_size=25, k=0.8), "Niblack's binarization (scikit-image)"),
        (lambda: threshold_triangle(gray_image), "Triangle binarization (scikit-image)"),
        (lambda: threshold_sauvola(gray_image, window_size=25), "Sauvola's binarization (scikit-image)"),
    ]):
        thresh_one = threshold[0]()
        binary_one = gray_image > thresh_one
        binary_one = img_as_ubyte(binary_one)

        # Plot all the images:
        show_img_with(cv2.cvtColor(binary_one, cv2.COLOR_GRAY2BGR), threshold[1], idx + 3)
        # Show the Figure:
    plt.show()
