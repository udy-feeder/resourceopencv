import cv2 as cv
# Reading image from file
img = cv.imread('Photos/cat_large.jpg')
cv.imshow('Cat', img)
cv.waitKey(0)

# Reading videos from file
import cv2 as cv
capture = cv.VideoCapture('Videos/dog.mp4') 
# Video from file. If the path is changed to 0 or 1, it will be the webcam
while True:
    isTrue, frame = capture.read()
    cv.imshow('Video', frame)
    if cv.waitKey(20) & 0xFF == ord('d'):
        break
capture.release()
cv.destroyAllWindows()
