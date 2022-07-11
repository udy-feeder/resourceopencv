import cv2 as cv
import numpy as np

img = cv.imread('Photos/boston.jpg')
cv.imshow('Boston', img)

b,g,r = cv.split(img)

cv.imshow('Blue', b)
cv.imshow('Green', g)
cv.imshow('Red', r)

print(img.shape)
print(b.shape)
print(g.shape)
print(r.shape)

merged = cv.merge((b,g,r))
cv.imshow('Merged', merged)


blank = np.zeros(img.shape[:2], dtype=img.dtype)
merged = cv.merge([b,blank,blank])
cv.imshow('Merged', merged)



cv.waitKey(0)