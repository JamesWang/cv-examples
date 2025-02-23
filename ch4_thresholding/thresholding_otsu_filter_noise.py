from functools import partial

import cv2
from matplotlib import pyplot as plt

from utils.helper import prepare_image, deferred_img_loader, init_then_display_orig_img
from utils.show_img import show_img_with_matplotlib, show_hist_with_matplotlib_gray

show_img_with = partial(show_img_with_matplotlib, m=3, n=2)
show_hist_with_gray = partial(show_hist_with_matplotlib_gray, m=3, n=2)

if __name__ == "__main__":
    orig_img, gray_image = prepare_image(deferred_img_loader('../images/leaf-noise.png'))

    init_then_display_orig_img(
        title="Otsu's binarization algorithm applying a Gaussian filter",
        show_orig_img=lambda: show_img_with(orig_img, "Original Image", 1)
    )
    show_img_with(cv2.cvtColor(gray_image, cv2.COLOR_GRAY2BGR), "gray img with noise", 2)

    # ----------------------------------------------------------------------------------------
    # Calculate the histogram
    hist = cv2.calcHist([gray_image], [0], None, [256], [0, 256])
    # Otsu's binarization algorithm:
    ret1, th1 = cv2.threshold(gray_image, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

    show_hist_with_gray(hist, "GrayScale Hist", pos=3, color='m', t=ret1)
    show_img_with(
        cv2.cvtColor(th1, cv2.COLOR_GRAY2BGR),
        "Otsu's binarization (before applying a Gaussian filter)",
        4
    )
    # ----------------------------------------------------------------------------------------
    #  Blurs the image using a Gaussian filter to eliminate noise
    gray_image_blurred = cv2.GaussianBlur(gray_image, (25, 25), 0)
    # Calculate histogram after filtering:
    hist2 = cv2.calcHist([gray_image_blurred], [0], None, [256], [0, 256])
    # Otsu's binarization algorithm:
    ret2, th2 = cv2.threshold(gray_image_blurred, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    show_hist_with_gray(hist2, "GrayScale Hist", pos=5, color='m', t=ret2)

    show_img_with(
        cv2.cvtColor(th2, cv2.COLOR_GRAY2BGR),
        "Otsu's binarization (after applying a Gaussian filter)",
        6
    )
    # ----------------------------------------------------------------------------------------

    # Show the Figure:
    plt.show()
