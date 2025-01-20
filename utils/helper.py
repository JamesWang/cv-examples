import cv2
import numpy as np
from matplotlib import pyplot as plt

from utils.show_img import init_display


def loader(filename):
    return lambda: cv2.imread(filename)


def prepare_image(image_loader, show_image_with, message, title):
    init_display(title)
    # Load the image and convert it to grayscale:
    image = image_loader()

    # np.float32(image) - convert image to float32 array first
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Plot the grayscale images and the histograms:
    show_image_with(
        cv2.cvtColor(gray_image, cv2.COLOR_GRAY2BGR),
        message,
        1
    )
    return gray_image
