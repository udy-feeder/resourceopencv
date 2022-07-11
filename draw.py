import cv2 as cv
import numpy as np
# paint the image a different color
blank= np.zeros((500,500,3), dtype='uint8')
# cv.imshow('Black', blank)

# blank[:] = (255,255,255)
# cv.imshow('White', blank)

# blank[:] = (0,255,0)
# cv.imshow('Green', blank)

# draw a rectangle
cv.rectangle(blank, (0,0), (250,250), (255,255,255), thickness=2)
# If you want to fill the rectangle, you can use the value which is less than 0 for thickness
# or maybe using cv.FILLED
# regarding the parameter of points, instead of using coordinates, you can use blank.shape[0 or 1]//the value which you want to fill
# cv.rectangle(blank, (0,0), (blank.shape[1]//2, blank.shape[0]//2), (0,255,0), thickness=2)
cv.imshow('Rectangle', blank)


# draw the circle
cv.circle(blank, (250,250), 250, (255,255,255), thickness=2)
cv.imshow('Circle', blank)

# draw the line
cv.line(blank, (0,0), (250,250), (255,255,255), thickness=2)
cv.imshow('Line', blank)
# Write text on the image
cv.putText(blank, 'Hello World', (250,250), cv.FONT_HERSHEY_SIMPLEX, 1, (255,255,255), thickness=2)
cv.imshow('Text', blank)
cv.waitKey(0)