from tensorflow import keras
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout
from tensorflow.keras.optimizers import RMSprop

import cv2
import time
import numpy as np
import random

train_data = []

def getFlattenArray(img):
    # flatten image 
    in_arr = np.array(img)
    out_arr = in_arr.flatten()

    return out_arr

def getFramesFromVideo(file_name, attack):
    print("Getting frames from " + file_name)
    cap = cv2.VideoCapture(file_name)

    success,image = cap.read()
    count = 0
    while success:
#        cv2.imshow(image)
#        print(image[0])
#        print(getFlattenArray(image))
        flat_img = getFlattenArray(image)
#        for data in img_data:
#            print(data)

        train_data.append([flat_img, attack])

        #cv2.imwrite("frame%d.jpg" % count, image)     # save frame as JPEG file      
        success,image = cap.read()
#        print('Read a new frame: ', success)
        count += 1

    print("Read " + str(count) + " frames")

getFramesFromVideo("./attack/parker1.mp4", 1)
getFramesFromVideo("./attack/parker2.mp4", 1)
getFramesFromVideo("./attack/parker3.mp4", 1)
getFramesFromVideo("./attack/parker4.mp4", 1)
getFramesFromVideo("./gooch/parker1.mp4", 0)
getFramesFromVideo("./attack/parker2.mp4", 0)
getFramesFromVideo("./attack/parker3.mp4", 0)
getFramesFromVideo("./attack/parker4.mp4", 0)



#print(train_data)
#    print(in_arr)
#    print("Output:")
#    print(out_arr)

    # convert image to float
#    out_arr = out_arr.tolist()
#    out_arr = [float(i) / 255.0 for i in out_arr]
#    print(out_arr)

# read our data from the attack and gooch directories 
img = cv2.imread("frame.png")

getFlattenArray(img)

cv2.imshow("frame", img)
cv2.destroyAllWindows()
