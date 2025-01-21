import string

import cv2

from utils.show_img import init_display


def deferred_img_loader(filename):
    return lambda: cv2.imread(filename)


def prepare_image(image_load):
    # Load the image and convert it to grayscale:
    image = image_load()
    if image is not None:
        gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        # Plot the grayscale images and the histograms:
        return image, gray_image
    raise Exception('Failed to load image')


def init_then_display_orig_img(title: string, show_orig_img):
    init_display(title=title)
    show_orig_img()

