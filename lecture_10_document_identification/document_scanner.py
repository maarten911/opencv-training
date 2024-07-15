import cv2
import numpy as np

width, height = 640, 480


def preprocess(image):
    # Convert the image to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Apply Canny edge detection
    edged = cv2.Canny(gray, 350, 50)

    kernel = np.ones((5, 5), np.uint8)
    image_dilation = cv2.dilate(edged, kernel, iterations=2)
    image_erosion = cv2.erode(image_dilation, kernel, iterations=1)

    return image_erosion


def draw_contours(image):
    contours, hierarchy = cv2.findContours(image, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    biggest = None
    for cnt in contours:
        # Only keep the one where we have 4 corners
        area = cv2.contourArea(cnt)
        perimeter = cv2.arcLength(cnt, True)
        approx = cv2.approxPolyDP(cnt, 0.02 * perimeter, True)

        # For some reason this unfortunately doesn't work now.
        if object_corners := len(approx) == 4:
            rectangle = True
        if area > 2_000:
            perimeter = cv2.arcLength(cnt, True)
            approx = cv2.approxPolyDP(cnt, 0.02 * perimeter, True)

            cv2.drawContours(image_contours_ori, cnt, -1, (255,0,0), 3)
            biggest = approx

    return biggest


def warp_perspective(img, biggest):
    pts1 = np.float32(biggest)
    pts2 = np.float32([[0, 0], [width, 0], [0, height], [width, height]])
    matrix = cv2.getPerspectiveTransform(pts1, pts2)
    image_output = cv2.warpPerspective(img, matrix, (width, height))

    return image_output


image = cv2.imread("../images/documentscanner2.jpg")
image_contours_ori = image.copy()
preprocssed_image = preprocess(image)

biggest = draw_contours(preprocssed_image)
image_warped = warp_perspective(image, biggest)

cv2.imshow("Document Scanner", image)
cv2.imshow("Document Scanner Warped", image_warped)
cv2.waitKey(0)
cv2.destroyAllWindows()
