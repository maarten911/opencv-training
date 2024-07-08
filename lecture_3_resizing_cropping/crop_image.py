import cv2
filepath = "../images/cats.jpg"
image = cv2.imread(filepath)

# First parameter is the y-axis, second parameter is the x-axis
# The first element is the x-axis in computer vision, because you follow the
# row-order, similar to accessing elements in a 2D array.
image_cropped = image[100:400, 100:400]
cv2.imshow("Cats_resize", image_cropped)
cv2.waitKey(0)
