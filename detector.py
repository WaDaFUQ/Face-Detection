import cv2 as CV
import numpy as np

CamID = 0
face_casecade = CV.CascadeClassifier('haarcascade_frontalface_default.xml') #openCV裡，選取人臉範圍的套件
Webcam = CV.VideoCapture(CamID, CV.CAP_DSHOW)
recognizer = CV.face.LBPHFaceRecognizer_create()
recognizer.read("recognizer\\trainingData.yml")

id=0
font = CV.FONT_HERSHEY_SIMPLEX #文字字型
color = (255, 255, 255) #文字顏色
stroke = 2 
run=1

    

while(run):
    ret, frame = Webcam.read()
    gray = CV.cvtColor(frame, CV.COLOR_BGR2GRAY) 
    faces = face_casecade.detectMultiScale(gray, 1.3, 5)
    
    for(x, y, w, h) in faces:
        CV.rectangle(frame, (x, y), (x+w, y+h), (0, 0, 255), 2)
        id, conf = recognizer.predict(gray[y:y+h, x:x+w])

                
        name_id_dict = {}
        with open('ID_name_Dictionary.txt', 'r') as name_file:
            for line in name_file:
                (ID, name) = line.split()
                name_id_dict[int(ID)] = name
        print(id, conf)
        
        for ID in name_id_dict.keys():
            if(int(ID)==id):
                if(conf<120):
                    result = str(name_id_dict[ID])
                    break
                else:
                    result = "unknown"
            else:
                result = "unknown"

        CV.putText(frame, str(result), (x,y+h), font, 1, color, stroke)
        CV.imshow('Face', frame)

        if CV.waitKey(20) & 0xFF == ord('q'):
            Webcam.release()
            CV.destroyAllWindows()
            run = 0
            break
    

print("Terminate!")