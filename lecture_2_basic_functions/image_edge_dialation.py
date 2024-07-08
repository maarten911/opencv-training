import cv2
filepath = "../images/cats.jpg"
image = cv2.imread(filepath)

# Higher value => Less edges detected
t_lower = 100
t_higher = 120

# Apply Canny Edge Dectector
image_canny = cv2.Canny(image, t_lower, t_higher)

# Dilation is the opposite of erosion. Erosion decreases the edge thickness
image_dialation = cv2.dilate(image_canny, (311, 311), iterations=2)
cv2.imshow("Cats", image_dialation)
cv2.waitKey(0)
