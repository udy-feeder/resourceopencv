import cv2 as cv
import numpy as np

img = cv.imread('Photos/cats.jpg')
cv.imshow('Original', img)

blanks = np.zeros(img.shape[:2], dtype=np.uint8)
cv.imshow('Blank', blanks)

mask = cv.circle(blanks, (img.shape[1] // 2, img.shape[0] // 2), img.shape[0] // 2, (255, 255, 255), -1)
cv.imshow('Mask', mask)

masked = cv.bitwise_and(img,img, mask=mask)
cv.imshow('Masked', masked)

# # the same code 
# img = cv.imread('Photos/cats.jpg')
# cv.imshow('Original', img)

# blanks = np.zeros(img.shape, dtype=np.uint8)
# cv.imshow('Blank', blanks)

# mask = cv.circle(blanks, (img.shape[1] // 2, img.shape[0] // 2), img.shape[0] // 2, (255, 255, 255), -1)
# cv.imshow('Mask', mask)

# masked = cv.bitwise_and(img,mask)
# cv.imshow('Masked', masked)


cv.waitKey(0)