import cv2
# 0: Take the webcam at id 0
cap = cv2.VideoCapture(0)
cap.set(3, 640)  # Width
cap.set(4, 480)  # Height
cap.set(10, 100)  # Brightness


while cap.isOpened():
    succes, frame = cap.read()
    if succes:
        cv2.imshow("Cats", frame)
        # Waitkey 0: QWait for user to go to next frame
        if cv2.waitKey(0) & 0xFF == ord('q'):
            break

    else:
        break

cap.release()
cv2.destroyAllWindows()
