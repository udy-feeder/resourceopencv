import cv2 as cv
import numpy as np

black = np.zeros((400, 400), dtype=np.uint8)

rectangle = cv.rectangle(black.copy(), (100, 100), (300, 300), 255, -1)
circle = cv.circle(black.copy(), (200, 200), 100, 255, -1)

cv.imshow("Rectangle", rectangle)
cv.imshow("Circle", circle)

# bitwise And
bitwise_and = cv.bitwise_and(rectangle, circle)
cv.imshow("Bitwise And", bitwise_and)

# bitwise Or
bitwise_or = cv.bitwise_or(rectangle, circle)
cv.imshow("Bitwise Or", bitwise_or)

# bitwise Xor
bitwise_xor = cv.bitwise_xor(rectangle, circle)
cv.imshow("Bitwise Xor", bitwise_xor)

# bitwise Not
bitwise_not = cv.bitwise_not(circle)
cv.imshow("Bitwise Not", bitwise_not)

cv.waitKey(0)