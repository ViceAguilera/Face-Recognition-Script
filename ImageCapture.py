import cv2
import os
import imutils

personName = ""
dataPath = '/home/sirius/PycharmProjects/FaceRecognition/Data'

def main():
    print("Enter the name of the person: ")
    personName = input()
    personPath = os.path.join(dataPath, personName)

    if not os.path.exists(personPath):
        print("Creating path for: {}".format(personName))
        os.makedirs(personPath)

    cap = cv2.VideoCapture(0)
    face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
    count = 0

    while True:
        ret, frame = cap.read()
        if not ret:
            break
        frame = imutils.resize(frame, width=640)
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        auxFrame = frame.copy()

        faces = face_cascade.detectMultiScale(gray, 1.3, 5)

        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
            face = auxFrame[y:y + h, x:x + w]
            face = cv2.resize(face, (150, 150), interpolation=cv2.INTER_CUBIC)
            cv2.imwrite(personPath + '/face_{}.jpg'.format(count), face)
            count += 1

        cv2.imshow('frame', frame)
        if cv2.waitKey(1) & 0xFF == ord('q') or count >= 1000:
            break
    cap.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
