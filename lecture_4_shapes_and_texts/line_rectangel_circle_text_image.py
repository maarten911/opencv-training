import cv2
import numpy as np

# Greyscale if we have no channels

image = np.zeros((512, 512, 3))
# Color blue
image[:] = 255, 0, 0

# Draw a line
line_start = (0,0)
line_end = (image.shape[1], image.shape[0])
line_color = (0, 255, 0)
line_thickness = 3
cv2.line(image, line_start, line_end, line_color, line_thickness)

# Draw a rectangle
thickness = cv2.FILLED
cv2.rectangle(image, (0,0), (250, 350), (0, 0, 255), thickness)

# Draw a circle
cv2.circle(image, (100, 100), 50, (100, 100, 100), 5)

# Write text
cv2.putText(image, "text", (300, 100), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 150, 0), 1)

cv2.imshow("Output image", image)
cv2.waitKey(0)

