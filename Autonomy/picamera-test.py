import time
import picamera
import numpy as np
import cv2

with picamera.PiCamera() as camera:
#    time.sleep(2)
#    output = np.empty((240,320,3),dtype=np.uint8)
    camera.resolution = (640,480)
    camera.start_preview()
    time.sleep(1)
    camera.capture('output.jpg','rgb')
    camera.stop_preview()

img = cv2.imread("test.png")
print(img)

