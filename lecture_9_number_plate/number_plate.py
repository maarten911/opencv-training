import cv2

cap = cv2.VideoCapture("../videos/demo.mp4")
numberPlateCascade = cv2.CascadeClassifier("../haarcascades/haarcascade_russian_plate_number.xml")

while True:
    ret, frame = cap.read()
    # why resize the frame?
    # 1. Faster processing
    # 2. Smaller frame size
    # 3. More accurate face detection
    frame = cv2.resize(frame, (640, 480))
    if ret:
        frame_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        number_plate = numberPlateCascade.detectMultiScale(frame_gray, 1.1, 4)
        for (x, y, w, h) in number_plate:
            cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)
        cv2.imshow("Output stream", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

