import cv2

if __name__ == '__main__':
    cv2.namedWindow('Canny')
    image = cv2.imread("../images/leaf.png", 0)

    """
        1. De-noise with Gaussian Filter
        2. Calculate gradients
        3. Applies Non-maximum suppression on edges
        4. Double threshold on all the detected edges to eliminate false positive
        5. Analyzes all the edges and their connection to each other (keep real edges and discard the weak ones)
    """
    def empty(z):
        pass

    cv2.createTrackbar('Threshold 1', 'Canny', 50, 100, empty)
    cv2.createTrackbar('Threshold 2', 'Canny', 150, 300, empty)
    while True:
        p1 = cv2.getTrackbarPos('Threshold 1', 'Canny')
        p2 = cv2.getTrackbarPos('Threshold 2', 'Canny')
        canny_image = cv2.Canny(image, p1, p2, L2gradient=False)
        cv2.imshow("Canny", canny_image)

        # handle close window by press ESC
        if cv2.waitKey(1) == 27:
            break
        # handle close window by click X
        if cv2.getWindowProperty('Canny', cv2.WND_PROP_VISIBLE) < 1:
            break

    cv2.destroyAllWindows()
