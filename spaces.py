import cv2 as cv
import matplotlib.pyplot as plt

img = cv.imread('Photos/boston.jpg')
cv.imshow('Bostons', img)

# # BGR to grayscale
# gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# cv.imshow('Gray', gray)

# # BGR to HSV
# hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
# cv.imshow('HSV', hsv)

# # BGR to LAB
# lab = cv.cvtColor(img, cv.COLOR_BGR2LAB)
# cv.imshow('LAB', lab)

# # Display RGB image
# plt.imshow(img)
# plt.show()

# # BGR to RGB
# rgb = cv.cvtColor(img, cv.COLOR_BGR2RGB)
# plt.imshow(rgb)
# plt.show()



# cv.waitKey(0)