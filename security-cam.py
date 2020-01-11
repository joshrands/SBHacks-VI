# Run this script on a laptop with the web cam for detecting heart attacks.
# The laptop will deploy the autonomous AED system when the attack is detected 

# Step 1: Use ML and CV to detect heart attack
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout
from tensorflow.keras.optimizers import RMSprop

import cv2
import time
import numpy as np
import random

# load model from saved location
model = keras.models.load_model("./Deploy/MachineLearning/model-cnn-v1.h5")

video_input = input("Enter web cam input: ")
cap = cv2.VideoCapture(video_input)

# grab picture from webcam every 0.1 seconds and run through model
count = 0
consecutive_count = 0
count_threshold = 5
while cap.isOpened() and consecutive_count < count_threshold:
    ret, frame = cap.read()
    if ret == True:
        # Display the resulting frame
#        cv2.imshow('Frame',frame)

        # hardcoded dimensions of frame because hackathon
        dim = (57, 32)

        # grayscale the image
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        resized = cv2.resize(gray, dim, interpolation = cv2.INTER_AREA)
        resized = resized.tolist()

        # convert to cnn input format
        final_in = []
        for row in resized:
            new_row = []
            for val in row:
                new_row.append([float(val) / 255.0])
            final_in.append(new_row)  

        predicted = model.predict([final_in]).argmax()
#        print(predicted)
        count += 1
        if (predicted == 1):
            print("Heart attack detected")
            consecutive_count += 1
        elif (count % 20 == 0):
            print("You good")
            consecutive_count = 0

        time.sleep(0.1)

print("EMERGENCY HEART ATTACK")
print("Dispatching autonomous AED...")

# Step 2: Get localization information? Quadrant? 

