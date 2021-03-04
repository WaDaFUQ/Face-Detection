import os
import cv2 as cv
import numpy as np
from PIL import Image

recognizer =  cv.face.LBPHFaceRecognizer_create()
path='dataSet'

def getImagesID(path):
    imagePaths = [os.path.join(path, f) for f in os.listdir(path)]
    faces=[]
    IDs=[]

    for imagePath in imagePaths:
        faceImg = Image.open(imagePath).convert('L')
        faceNp = np.array(faceImg, 'uint8')
        ID = int(os.path.split(imagePath)[-1].split('.')[1])
        print(ID)
        faces.append(faceNp)
        IDs.append(ID)
        cv.imshow("training", faceNp)
        cv.waitKey(10)
    return IDs, faces

Ids, faces = getImagesID(path)

recognizer.train(faces, np.array(Ids))
recognizer.save('recognizer/trainingData.yml')
cv.destroyAllWindows()