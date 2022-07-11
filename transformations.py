import cv2 as cv
import numpy as np

img =cv.imread('Photos/lady.jpg')

cv.imshow('Lady', img)

# # Translation
def translate(img,x,y):
    transMat = np.float32([[1,0,x],[0,1,y]])
    dimension = (img.shape[1], img.shape[0])
    return cv.warpAffine(img, transMat, dimension)

# # -x --> Left
# # +x --> Right
# # -y --> Up
# # +y --> Down

translated = translate(img, -100, -100)
cv.imshow('Translated', translated)

# Rotation
def rotate(img, angle, rotPoint=None):
    (height, width) = img.shape[:2]
    if rotPoint is None:
        rotPoint = (width // 2, height // 2)
    rotMat = cv.getRotationMatrix2D(rotPoint, angle, 1.0)
    dimension = (width, height)
    return cv.warpAffine(img, rotMat, dimension)
rotated = rotate(img, -90)
cv.imshow('Rotated', rotated)

# # Resizing
# resized = cv.resize(img, (0,0), fx=2, fy=2, interpolation=cv.INTER_CUBIC)
# cv.imshow('Resized', resized)

# # Flipping
# flip = cv.flip(img, 0)
# cv.imshow('Flipped', flip)

# # Cropping
# cropped = img[200:400, 300:400]
# cv.imshow('Cropped', cropped)



cv.waitKey(0)