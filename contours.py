import cv2 as cv
import numpy as np

img = cv.imread('Photos/cats.jpg')

cv.imshow('Cats', img)

blanks = np.zeros(img.shape, dtype=np.uint8)
cv.imshow('Blanks', blanks)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

blur = cv.GaussianBlur(img, (7, 7), cv.BORDER_DEFAULT)
cv.imshow('Blur', blur)

canny = cv.Canny(blur, 125, 175)
cv.imshow('Canny', canny)

# ret, thresh = cv.threshold(gray, 127, 255, cv.THRESH_BINARY) # If the pixel value is greater than 255, it is set to white. Otherwise, it is set to black.
# cv.imshow('Thresh', thresh)
# contours, hierarchy = cv.findContours(thresh, cv.RETR_LIST, cv.CHAIN_APPROX_NONE)
# print(len(contours))
# cv.drawContours(blanks, contours, -1, (0, 255, 0), -1)
# cv.imshow('Contours', blanks)


cv.waitKey(0)
