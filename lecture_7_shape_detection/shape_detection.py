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
# contours = []

for contour in contours:
    # Step 5, draw contour
    area = cv2.contourArea(contour)
    print(f"{area=}")
    cv2.drawContours(image_contours, [contour], -1, (0, 255, 0), 3)

    # Step 6: Calculate the perimeter. what's a perimeter?
    perimeter = cv2.arcLength(contour, True)

    # Step 7 : Find the corner points for each of the shape in the iamge
    approx = cv2.approxPolyDP(contour, 0.02 * perimeter, True)
    print("Number of corners: ", len(approx))
    x, y, w, h = cv2.boundingRect(approx)
    cv2.rectangle(image_contours, (x, y), (x + w, y + h), (255, 0, 0), 2)

    if object_corners := len(approx) == 3:
        object_type = "Triangle"
    elif object_corners := len(approx) == 4:
        aspect_ratio = w / float(h)
        object_type = "Square" if 0.95 <= aspect_ratio <= 1.05 else "Rectangle"
    elif object_corners := len(approx) == 5:
        object_type = "Pentagon"
    elif object_corners := len(approx) == 6:
        object_type = "Hexagon"
    else:
        object_type = "Circle"

    cv2.putText(image_contours, object_type, (x, y), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0, 0, 0), 1)

cv2.imshow("Contours", image_contours)
# cv2.imshow("Shapes", image)
# cv2.imshow("Shapes gray", image_gray)
cv2.imshow("Edge detector", canny_edge)
cv2.waitKey(0)
