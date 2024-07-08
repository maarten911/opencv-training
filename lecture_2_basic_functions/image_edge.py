import cv2
filepath = "../images/cats.jpg"
image = cv2.imread(filepath)

# Higher value => Less edges detected
t_lower = 100
t_higher = 120

# Apply Canny Edge Dectector
edge = cv2.Canny(image, t_lower, t_higher)
cv2.imshow("Cats", edge)
cv2.waitKey(0)
