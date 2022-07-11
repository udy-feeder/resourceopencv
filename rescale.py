import cv2 as cv
# Resizing a frame 
def resize(frame, scale=0.75):
    # videos, images, live videos
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dim = (width, height)
    return cv.resize(frame, dim, interpolation=cv.INTER_AREA)

def changeRes(width, height):
    # live video
    capture.set(3, width)
    capture.set(4, height)

#Resizing a video
# capture = cv.VideoCapture('Videos/dog.mp4')
# while True:
#     isTrue, frame = capture.read()
#     new_frame = resize(frame, scale=0.2)
#     cv.imshow('Video', frame)
#     cv.imshow('Video Resized', new_frame)
#     if cv.waitKey(20) & 0xFF == ord('d'):
#         break
# capture.release()
# cv.destroyAllWindows()

# Resizing a picture
# img = cv.imread('Photos/cat_large.jpg')
# new_img = resize(img, scale=0.2)
# cv.imshow('Cat', img)
# cv.imshow('Cat Resized', new_img)
# cv.waitKey(0)
