import cv2
filepath = "../images/cats.jpg"
image = cv2.imread(filepath)
image_resize = cv2.resize(image, (500, 500))
cv2.imshow("Cats_resize", image_resize)
# If you print(image.shape), you'll now get: (500, 500, 3), becuase we have 3 channels RGB)
# Press for key hit to skip
cv2.waitKey(0)
