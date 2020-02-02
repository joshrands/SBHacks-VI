import cv2
import numpy as np
 
# Create a VideoCapture object and read from input file
# If the input is the camera, pass 0 instead of the video file name
img = cv2.imread("ObjectDetection/output.jpg")

resized = cv2.resize(img, (114,64), interpolation = cv2.INTER_AREA)

# Display the resulting frame
cv2.imshow('image',resized)
cv2.waitKey(0)

frame_gray = cv2.cvtColor(resized, cv2.COLOR_BGR2GRAY)
ret, thresh = cv2.threshold(frame_gray, 127, 255, 0)
contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

print(len(contours))
cv2.drawContours(resized, contours, -1, (0,255,0), 3)
cv2.imshow('image',resized)
cv2.waitKey(0)

# Closes all the frames
cv2.destroyAllWindows()
