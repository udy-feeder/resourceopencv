import cv2 as cv

img = cv.imread('Photos/cats.jpg')
cv.imshow('Original', img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

# Simple thresholding
threshold, thresh = cv.threshold(gray, 150, 255, cv.THRESH_BINARY) # cv.THRESH_BINARY_INV is the inverse of cv.THRESH_BINARY
cv.imshow('Threshold', thresh)

# Adaptive thresholding
addaptive_thresh = cv.adaptiveThreshold(gray, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY, 15, 1)
cv.imshow('Adaptive Threshold', addaptive_thresh)


cv.waitKey(0)