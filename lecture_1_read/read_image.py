import cv2
filepath = "../images/cats.jpg"
image = cv2.imread(filepath)
cv2.imshow("Cats", image)

# Press for key hit to skip
cv2.waitKey(0)
