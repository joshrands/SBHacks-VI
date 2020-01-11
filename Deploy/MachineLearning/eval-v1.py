import tensorflow as tf
from tensorflow import keras
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout
from tensorflow.keras.optimizers import RMSprop

import cv2
import time
import numpy as np
import random
import os
import matplotlib.pyplot as pl

checkpoint_path = "checkpoints/v1.ckpt"
checkpoint_dir = os.path.dirname(checkpoint_path)

def getFlattenArray(img):
    # flatten image
    in_arr = np.array(img)
    out_arr = in_arr.flatten()
    out_arr = out_arr.tolist()

    return out_arr

# scaling images 
scale_percent = 3
train_data = []

def getFramesFromVideo(file_name, attack):
    print("Getting frames from " + file_name)
    cap = cv2.VideoCapture(file_name)

    if (cap.isOpened()== False): 
        print("Error opening video stream or file")

    success,image = cap.read()
    count = 0
    while success:
#        cv2.imshow(image)
#        print(getFlattenArray(image))
        width = int(image.shape[1] * scale_percent / 100)
        height = int(image.shape[0] * scale_percent / 100)
        dim = (width, height)
 
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

        resized = cv2.resize(gray, dim, interpolation = cv2.INTER_AREA)

#        cv2.imshow("Frame", resized)
#        display_sample(gray, width, height)
        # Press Q on keyboard to  exit
        if cv2.waitKey(25) & 0xFF == ord('q'):
            break

        flat_img = getFlattenArray(resized)
#        print(len(flat_img))
#        for data in img_data:
#            print(data)

        if (attack == 1):
            train_data.append([flat_img, [0, 1]])
        else:
            train_data.append([flat_img, [1, 0]])

        #cv2.imwrite("frame%d.jpg" % count, image)     # save frame as JPEG file      
        success,image = cap.read()
#        print('Read a new frame: ', success)
        count += 1

    print("Read " + str(count) + " frames")

getFramesFromVideo("./attack/parker1.mp4", 1)
#getFramesFromVideo("./attack/parker3.mp4", 1)
#getFramesFromVideo("./attack/parker3.mp4", 1)
#getFramesFromVideo("./attack/parker4.mp4", 1)
getFramesFromVideo("./gooch/parker1.mp4", 0)
#getFramesFromVideo("./gooch/parker2.mp4", 0)
#getFramesFromVideo("./gooch/parker3.mp4", 0)
#getFramesFromVideo("./gooch/parker4.mp4", 0)

def display_sample(img, width, height):
    #Print the one-hot array of this sample's label 
#    print(train_labels[num])  
    #Print the label converted back to a number
#    label = train_labels[num].argmax(axis=0)
    #Reshape the 768 values to a 28x28 image

    new_img = np.array(img)
    image = new_img.reshape([57,32])
#    plt.title('Sample: %d  Label: %d' % (num, label))
    plt.imshow(image, cmap=plt.get_cmap('gray_r'))
    plt.show()

# Create a basic model instance
model = keras.models.load_model("model-v2.h5")

# Loads the weights
#model.load_weights(checkpoint_path)

# Re-evaluate the model
#loss,acc = model.evaluate(test_imag,  test_labels, verbose=2)
#print("Restored model, accuracy: {:5.2f}%".format(100*acc))

for x in range(len(train_data)):
    test_image = [train_data[x][0]]
#    print(test_image)
#    print(len(test_image))
    predicted = model.predict(test_image).argmax()
    label = 0
    if (train_data[x][1][1] == 1):
        label = 1

    if (predicted != label):
#        plt.title('Prediction: %d Label: %d' % (predicted, label))
#        plt.imshow(test_data[x][0], cmap=plt.get_cmap('gray_r'))
#        plt.show()
        display_sample(train_data[x][0],0,0)

print("Data complete.")
