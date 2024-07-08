import cv2
import numpy as np
image = cv2.imread("../images/cards.png")
width, height = 500, 500

# pts_source = np.float32([[111, 219], [287, 188], [154, 482], [352, 440]])
pts_source = np.float32([[702, 150], [1129, 417], [286, 694], [720, 996]])
pts_target = np.float([[0, 0], [width, 0], [0, height], [width, height]])
matrix = cv2.getPerspectiveTransform(pts_source, pts_target)

image_warped = cv2.warpPerspective(image, matrix, (width, height))

cv2.imshow("Cards", image)
cv2.imshow("Cards", image_warped)
cv2.waitKey(0)
