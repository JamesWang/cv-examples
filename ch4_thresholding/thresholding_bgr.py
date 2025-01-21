"""
Thresholding color images
"""

# Import required packages:
from functools import partial

import cv2
from matplotlib import pyplot as plt

# Create the dimensions of the figure and set title and color:
from utils.helper import prepare_image, deferred_img_loader, init_then_display_orig_img
from utils.show_img import show_single_channel

show_img_with = partial(show_single_channel, m=1, n=3)

if __name__ == '__main__':
    orig_img, gray_image = prepare_image(deferred_img_loader('../images/cat.jpg'))
    init_then_display_orig_img(
        title='Thresholding BGR images',
        show_orig_img=lambda: show_img_with(orig_img, "gray img", 1)
    )

    # Apply cv2.threshold():
    ret1, thresh1 = cv2.threshold(
        src=orig_img,
        thresh=120,
        maxval=255,
        type=cv2.THRESH_BINARY
    )

    show_img_with(thresh1, "threshold (120) BGR image", 2)

    # Apply cv2.threshold() on each channel then merge, should be same effect:
    bgr_thresh = None
    for idx, c in enumerate(cv2.split(orig_img)):
        _, thresh = cv2.threshold(src=c, thresh=120, maxval=255, type=cv2.THRESH_BINARY)
        if bgr_thresh is not None:
            bgr_thresh = cv2.merge((bgr_thresh, thresh))
        else:
            bgr_thresh = thresh

    # Plot the created images
    show_img_with(bgr_thresh, "threshold (120) each channel and merge", 3)

    # Show the Figure:
    plt.show()
