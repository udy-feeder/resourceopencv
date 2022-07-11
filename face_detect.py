import cv2 as cv

img = cv.imread('Photos/group 2.jpg')
cv.imshow('people', img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('People_Gray', gray)

haar_cascade = cv.CascadeClassifier('haar_face.xml')
faces_rectangle = haar_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=3)

print('Number of faces: ', len(faces_rectangle))
print('Faces rectangle: ', faces_rectangle)

for (x, y, w, h) in faces_rectangle:
    cv.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
cv.imshow('Person_Detected', img)
# Increasing minNeighbors increases the accuracy of the detection
# Hard cascades are not the most effective way to detect faces

cv.waitKey(0)