import cv2
filepath = "../images/cats.jpg"
image = cv2.imread(filepath)

image_grey = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow("Cats", image_grey)

# Press for key hit to skip
cv2.waitKey(0)
