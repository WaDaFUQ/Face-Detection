import cv2 as cv

capture = cv.VideoCapture(0, cv.CAP_DSHOW)

while True:
    isTure, frame = capture.read()
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    cv.imshow('Gray', gray)

    if cv.waitKey(20) & 0xFF==ord('q'):
        break

capture.release()

