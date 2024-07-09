

import cv2
import numpy as np


cv2.namedWindow("Trackbars")
cv2.resizeWindow("Trackbars", 640, 240)

cv2.createTrackbar("Hue Min", "Trackbars", 0, 179)
cv2.createTrackbar("Hue Max", "Trackbars", 179, 179)
cv2.createTrackbar("Sat Min", "Trackbars", 0, 255)
cv2.createTrackbar("Sat Max", "Trackbars", 255, 255)
cv2.createTrackbar("Val Min", "Trackbars", 0, 255)
cv2.createTrackbar("Val Max", "Trackbars", 255, 255)

while True:
    image = cv2.imread("../images/cats.png")
    imageHSV=cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    h_min = cv2.getTrackbarPos("Hue Min", "Trackbars")
    h_max = cv2.getTrackbarPos("Hue Max", "Trackbars")
    s_min = cv2.getTrackbarPos("Sat min", "Trackbars")
    s_max = cv2.getTrackbarPos("Sat max", "Trackbars")
    v_min = cv2.getTrackbarPos("Val min", "Trackbars")
    v_max = cv2.getTrackbarPos("Val max", "Trackbars")
    lower = np.array([h_min, s_min, v_min])
    upper = np.array([h_max, s_max, v_max])
    mask = cv2.inRange(imageHSV, lower, upper)

    cv2.imshow("original Image", image)
    cv2.imshow("HSV Image", imageHSV)
    cv2.imshow("Mask Image", mask)
    cv2.waitKey(1)