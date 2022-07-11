import cv2 as cv
import numpy as np

img = cv.imread('Photos/cat.jpg')
cv.imshow('Cat', img)

# # Converting to grayscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

# # Blurring the image
blur = cv.GaussianBlur(img, (101,101), cv.BORDER_DEFAULT)
cv.imshow('Blur', blur)

# # Edge Cascade
canny = cv.Canny(img, 125, 175)
cv.imshow('Canny', canny)

# # Diilating the image
kernel = np.ones((5,5), np.uint8)
dilate = cv.dilate(canny, kernel, iterations=1)
cv.imshow('Dilate', dilate)


# # Eroding the image
kernel = np.ones((5,5), np.uint8)
erode = cv.erode(dilate, kernel, iterations=1)
cv.imshow('Erode', erode)

# # Resizing the image
# new_img = cv.resize(img, (0,0), fx=2, fy=2)
# cv.imshow('Resize', new_img)

# # Cropping the image
new_img = img[0 : img.shape[0] , img.shape[1]//2 : img.shape[1] ]
cv.imshow('Cropped', new_img)
cv.waitKey(0)