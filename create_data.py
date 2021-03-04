import cv2 as CV
import numpy as np
CamID = 0
CV.CascadeClassifier
face_casecade = CV.CascadeClassifier('haarcascade_frontalface_default.xml')
Webcam = CV.VideoCapture(CamID, CV.CAP_DSHOW)

user_id = str(input('enter your student ID:'))
user_name = str(input('enter your name:'))
write_file = user_id + " " + user_name
f = open('ID_name_Dictionary.txt', 'a')
f.write(write_file)
f.write('\n')
f.close()
    
sample_num = 0
while(True):
    ret, frame = Webcam.read()
    gray = CV.cvtColor(frame, CV.COLOR_BGR2GRAY)
    faces = face_casecade.detectMultiScale(gray, scaleFactor=1.5, minNeighbors=5)
    for(x, y, w, h) in faces:
        sample_num += 1
        CV.imwrite("dataSet/User."+str(user_id)+"."+str(sample_num)+".jpg", gray[y:y+h, x:x+w])
        CV.rectangle(frame, (x,y), (x+w, y+h), (0, 0, 255), 2)
        CV.waitKey(100)
    CV.imshow("Face", frame)    
    CV.waitKey(1)
    if(sample_num>20):
        CV.waitKey(5)
        Webcam.release()
        #cv.destroyAllWindows()
        break
    if CV.waitKey(1) & 0xFF == ord('q'):
        Webcam.release()
        CV.destroyAllWindows()
        break

