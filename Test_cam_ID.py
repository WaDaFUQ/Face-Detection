import cv2 as cv
import numpy as np


for i in range(10):
    Webcam = cv.VideoCapture(i)
    print(i,Webcam.isOpened())
    # if(Webcam.isOpened):
    #     print(i)


Webcam.release()
cv.destroyAllWindows