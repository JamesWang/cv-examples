import cv2
import numpy as np

if __name__ == "__main__":
    image = cv2.pyrDown(cv2.imread("../images/leaf.png", cv2.IMREAD_UNCHANGED))
    ret, thresh = cv2.threshold(cv2.cvtColor(image.copy(), cv2.COLOR_BGR2GRAY), 127, 255, cv2.THRESH_BINARY)

    contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    img = cv2.drawContours(image, contours[1:], -1, (255, 0, 0), 2)
    cv2.imshow("contours", img)
    cv2.waitKey()
    cv2.destroyAllWindows()
