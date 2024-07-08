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
