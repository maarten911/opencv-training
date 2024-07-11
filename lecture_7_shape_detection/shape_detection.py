import cv2
import numpy as np

image = cv2.imread("../images/shapes.png")

# Step 1: Convert to grayscale
image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Step 2: Apply canny edge detector to detect the edges
lower_threshold = 100
upper_threshold = 120
canny_edge = cv2.Canny(image_gray, lower_threshold, upper_threshold)

# Step 3: Find the contours
image_contours = image.copy()
contours, hierarchy = cv2.findContours(canny_edge, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
cv2.drawContours(image_contours, contours, -1, (0, 255, 0), 3)
print("Number of shapes: ", len(contours))

for contour in contours:
    # Step 5, draw contour
    area = cv2.contourArea(contour)
    print(f"{area=}")
    cv2.drawContours(image_contours, [contour], -1, (0, 255, 0), 3)

    # Step 6: Calculate the perimeter. what's a perimeter?
    perimeter = cv2.arcLength(contour, True)

    # Step 7 : Find the corner points for each of the shape in the iamge
    approx = cv2.approxPolyDP(contour, 0.02 * perimeter, True)

    # TODO: Start here

cv2.imshow("Contours", image_contours)
# cv2.imshow("Shapes", image)
# cv2.imshow("Shapes gray", image_gray)
cv2.imshow("Edge detector", canny_edge)
cv2.waitKey(0)
