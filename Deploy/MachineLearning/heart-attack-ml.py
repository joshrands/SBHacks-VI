from tensorflow import keras
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout
from tensorflow.keras.optimizers import RMSprop

import cv2
import time
import numpy as np
import random

train_data = []

import matplotlib.pyplot as plt

def display_sample(img, width, height):
    #Print the one-hot array of this sample's label 
#    print(train_labels[num])  
    #Print the label converted back to a number
#    label = train_labels[num].argmax(axis=0)
    #Reshape the 768 values to a 28x28 image

    image = img.reshape([width,height])
#    plt.title('Sample: %d  Label: %d' % (num, label))
    plt.imshow(image, cmap=plt.get_cmap('gray_r'))
    plt.show()

def getFlattenArray(img):
    # flatten image 
    in_arr = np.array(img)
    out_arr = in_arr.flatten()

    return out_arr

# scaling images 
scale_percent = 3

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

        cv2.imshow("Frame", resized)
#        display_sample(gray, width, height)
        # Press Q on keyboard to  exit
        if cv2.waitKey(25) & 0xFF == ord('q'):
            break

        flat_img = getFlattenArray(resized)
        print(len(flat_img))
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
getFramesFromVideo("./gooch/parker2.mp4", 0)
getFramesFromVideo("./gooch/parker3.mp4", 0)
getFramesFromVideo("./gooch/parker4.mp4", 0)

model = Sequential()
model.add(Dense(512, activation='relu', input_shape=(784,)))
model.add(Dense(10, activation='softmax'))

#print(train_data)
#    print(in_arr)
#    print("Output:")
#    print(out_arr)

    # convert image to float
#    out_arr = out_arr.tolist()
#    out_arr = [float(i) / 255.0 for i in out_arr]
#    print(out_arr)

# read our data from the attack and gooch directories 
#img = cv2.imread("frame.png")

#getFlattenArray(img)

#cv2.imshow("frame", img)
#cv2.destroyAllWindows()
