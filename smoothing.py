import cv2 as cv
import numpy as np

img = cv.imread('Photos/cats.jpg')
cv.imshow('Original', img)

# # Averaging
# # the center of the kernel is the average of all the pixels around it
# average = cv.blur(img, (5, 5)) # (5,5) is the kernel size
# cv.imshow('Averaging', average)
# gray = cv.cvtColor(average, cv.COLOR_BGR2GRAY)
# ret, thresh = cv.threshold(gray, 127, 255, cv.THRESH_BINARY)
# contours, hierarchy = cv.findContours(thresh, cv.RETR_LIST, cv.CHAIN_APPROX_NONE)
# print(len(contours))


# # GaussianBlur
# gaussian = cv.GaussianBlur(img, (5, 5), 0)
# cv.imshow('Gaussian', gaussian)
# gray = cv.cvtColor(gaussian, cv.COLOR_BGR2GRAY)
# ret, thresh = cv.threshold(gray, 127, 255, cv.THRESH_BINARY)
# contours, hierarchy = cv.findContours(thresh, cv.RETR_LIST, cv.CHAIN_APPROX_NONE)
# print(len(contours))


# # MedianBlur
# median = cv.medianBlur(img, 5) # 5 is the kernel size. This is the same as (5,5)
# cv.imshow('Median', median)
# gray = cv.cvtColor(median, cv.COLOR_BGR2GRAY)
# ret, thresh = cv.threshold(gray, 127, 255, cv.THRESH_BINARY)
# contours, hierarchy = cv.findContours(thresh, cv.RETR_LIST, cv.CHAIN_APPROX_NONE)
# print(len(contours))


# # BilateralBlur
# bilateral = cv.bilateralFilter(img, 15, 15,15)
# cv.imshow('Bilateral', bilateral)
# gray = cv.cvtColor(bilateral, cv.COLOR_BGR2GRAY)
# ret, thresh = cv.threshold(gray, 127, 255, cv.THRESH_BINARY)
# contours, hierarchy = cv.findContours(thresh, cv.RETR_LIST, cv.CHAIN_APPROX_NONE)
# print(len(contours))


# AverageBlur --> GaussianBlur --> MedianBlur --> BilateralBlur

cv.waitKey(0)