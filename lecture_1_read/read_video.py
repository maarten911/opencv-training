import cv2
filepath = "../videos/screen_recording.mov"
cap = cv2.VideoCapture(filepath)

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
