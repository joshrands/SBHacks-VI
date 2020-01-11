import tensorflow as tf
from tensorflow import keras
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout
from tensorflow.keras.optimizers import RMSprop

import cv2
import time
import numpy as np
import random

def getFlattenArray(img):
    # flatten image 
    in_arr = np.array(img)
    out_arr = in_arr.flatten()
    out_arr = out_arr.tolist()

    return out_arr

model = keras.models.load_model("model-cnn-v1.h5")
cap = cv2.VideoCapture(4)

# grab picture from webcam every second and run through model
count = 0
while cap.isOpened():
    ret, frame = cap.read()
    if ret == True:
        # Display the resulting frame
        cv2.imshow('Frame',frame)

    #    print(len(frame[0]),len(frame[1]))

#        scale_percent = 3
#        width = int(frame.shape[1] * scale_percent / 100)
#        height = int(frame.shape[0] * scale_percent / 100)
        dim = (57, 32)

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        resized = cv2.resize(gray, dim, interpolation = cv2.INTER_AREA)
        resized = resized.tolist()

        final_in = []
        for row in resized:
            new_row = []
            for val in row:
                new_row.append([float(val) / 255.0])
            final_in.append(new_row)  
    #        cv2.imshow("Frame", resized)
    #        display_sample(gray, width, height)
        # Press Q on keyboard to  exit

   #    print(len(flat_img))

        predicted = model.predict([final_in]).argmax()
#        print(predicted)
        count += 1
        if (predicted == 1):
            print("Heart attack!")
        elif (count % 20 == 0):
            print("You good")

        time.sleep(0.1)

#    cv2.destroyAllWindows()
