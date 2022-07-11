import cv2 as cv
import numpy as np

img = cv.imread('Photos/cats.jpg')
cv.imshow('Cats', img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

# Laplacian
lap = cv.Laplacian(gray, cv.CV_64F)
lap = np.uint8(np.absolute(lap))
cv.imshow('Laplacian', lap) # absolute is used to make the image positive

# Sobel
sobelX = cv.Sobel(gray, cv.CV_64F, 1, 0)
sobelY = cv.Sobel(gray, cv.CV_64F, 0, 1)
sobelX = np.uint8(np.absolute(sobelX))
sobelY = np.uint8(np.absolute(sobelY))
sobelCombined = cv.bitwise_or(sobelX, sobelY)
cv.imshow('Sobel X', sobelX)
cv.imshow('Sobel Y', sobelY)
cv.imshow('Sobel Combined', sobelCombined)
# bitwise_and is similar as Laplacian

# canny
canny = cv.Canny(gray, 100, 200)
cv.imshow('Canny', canny)
# Canny is basically a more advanced version of Sobel




cv.waitKey(0)