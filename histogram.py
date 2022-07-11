import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np

img = cv.imread('Photos/cats.jpg')
cv.imshow('Original', img)

blanks = np.zeros(img.shape[:2], dtype=np.uint8)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

circle = cv.circle(blanks, (img.shape[1] // 2, img.shape[0] // 2), img.shape[0] // 2, 255, -1)
cv.imshow('Mask', circle)
mask = cv.bitwise_and(gray, gray, mask=circle)
# # Grayscale histogram
# hist = cv.calcHist([gray], [0], mask, [256], [0, 256])

# plt.figure()
# plt.title('Grayscale Histogram')
# plt.xlabel('Bins')
# plt.ylabel('# of Pixels')
# plt.plot(hist)
# # plt.xlim([0, 256])
# plt.show()

# Color histogram
plt.figure()
plt.title('Colors Histogram')
plt.xlabel('Bins')
plt.ylabel('# of Pixels')
color = ('b', 'g', 'r')
for i, col in enumerate(color):
    hist = cv.calcHist([img], [i], None, [256], [0, 256])
    plt.plot(hist, color=col)
    plt.xlim([0, 256])
plt.show()


cv.waitKey(0)