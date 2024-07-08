import cv2
filepath = "../images/cats.jpg"
image = cv2.imread(filepath)

image_blur = cv2.GaussianBlur(image,(31, 31), 0)
cv2.imshow("Cats", image_blur)

# Press for key hit to skip
cv2.waitKey(0)
