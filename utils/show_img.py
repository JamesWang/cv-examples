from typing import MutableSequence

import cv2
from matplotlib import pyplot as plt


def init_display(title):
    fig = plt.figure(figsize=(9, 9))
    plt.suptitle(title, fontsize=14, fontweight='bold')
    fig.patch.set_facecolor('silver')


def show_img_with_matplotlib(color_img, title, pos, m, n):
    # Convert BGR image to RGB
    img_rgb = color_img[:, :, ::-1]

    _ = plt.subplot(m, n, pos)
    plt.imshow(img_rgb)
    plt.title(title)
    plt.axis('off')


def thresholding_and_show(threshold_arr: MutableSequence, image, show_img, max_val=255, th_type=cv2.THRESH_BINARY):
    # Apply cv2.threshold(image, threshold, max_val, threshold_type) with different thresholding values:
    # max_val only applies to binary and binary_inv, and 255 - white

    for idx, threshold in enumerate(threshold_arr):
        _, thresh_img = cv2.threshold(image, threshold, max_val, th_type)
        # Plot the images:
        show_img(cv2.cvtColor(thresh_img, cv2.COLOR_GRAY2BGR), f"threshold = {threshold}", 2 + idx)

    # Show the Figure:
    plt.show()
