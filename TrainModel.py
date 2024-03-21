import cv2
import os
import numpy as np

dataPath = '/home/sirius/PycharmProjects/FaceRecognition/Data'
peopleList = os.listdir(dataPath)
print('People list: ', peopleList)


def main():
    labels = []
    facesData = []
    label = 0

    for nameDir in peopleList:
        personPath = dataPath + '/' + nameDir
        print('Reading images')

        for fileName in os.listdir(personPath):
            print('Reading image: ', nameDir + '/' + fileName)
            labels.append(label)
            facesData.append(cv2.imread(personPath + '/' + fileName, 0))
            image = cv2.imread(personPath + '/' + fileName, 0)

        label += 1

    face_recognizer = cv2.face.LBPHFaceRecognizer_create()
    print("Training...")
    face_recognizer.train(facesData, np.array(labels))

    face_recognizer.write('FacesModel.xml')
    print('Model trained successfully')


if __name__ == "__main__":
    main()