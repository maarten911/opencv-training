import cv2

cap = cv2.VideoCapture(0)
faceCascade = cv2.CascadeClassifier("../haarcascades/haarcascade_frontalcatface.xml")

while True:
    ret, frame = cap.read()

    faces = faceCascade.detectMultiScale(frame, 1.1, 4)
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)
    cv2.imshow("Output stream", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
