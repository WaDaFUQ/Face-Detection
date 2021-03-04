import cv2
import numpy as np


for i in range(10):
    Webcam = cv2.VideoCapture(i)
    print(i,Webcam.isOpened())
    # if(Webcam.isOpened):
    #     print(i)


Webcam.release()
cv2.destroyAllWindows