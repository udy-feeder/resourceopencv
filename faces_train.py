import os
import cv2 as cv
import numpy as np


DIR = r'Faces\train' # r is for raw string

# Read the name of the file
people=[]
for i in os.listdir(DIR):
    people.append(i)
print(people)

features = [] # features of the face
labels = [] # label of the face

haar_cascade = cv.CascadeClassifier('haar_face.xml')

def create_train():
    for person in people:
        path = os.path.join(DIR, person)
        label = people.index(person)

        for img in os.listdir(path):
            img_path = os.path.join(path, img)
            img_array = cv.imread(img_path)
            gray = cv.cvtColor(img_array, cv.COLOR_BGR2GRAY)
            faces = haar_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=4)
            for (x, y, w, h) in faces:
                face_array = gray[y:y+h, x:x+w]
                features.append(face_array)
                labels.append(label)


create_train()
# # Check if the data is correct
# print(f'Length of features: {len(features)}')
# print(f'Length of labels: {len(labels)}')

print('Training done ------------------------------------------------')
features = np.array(features, dtype='object')
labels = np.array(labels)

face_recognizer = cv.face.LBPHFaceRecognizer_create()
face_recognizer.train(features, labels)
face_recognizer.save('face_trained.yml')
np.save('features.npy', features)
np.save('labels.npy', labels)


