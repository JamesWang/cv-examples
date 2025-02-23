import cv2

if __name__ == '__main__':
    image = cv2.imread("../images/leaf.png", 0)
    canny_image = cv2.Canny(image, 200, 300)
    """
        1. De-noise with Gaussian Filter
        2. Calculate gradients
        3. Applies Non-maximum suppression on edges
        4. Double threshold on all the detected edges to eliminate false positive
        5. Analyzes all the edges and their connection to each other (keep real edges and discard the weak ones)
    """
    cv2.imshow("Canny", canny_image)
    cv2.waitKey()
    cv2.destroyAllWindows()
