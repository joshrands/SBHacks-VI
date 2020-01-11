import tensorflow as tf
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

    new_img = np.array(img)
    image = new_img.reshape([57,32])
#    plt.title('Sample: %d  Label: %d' % (num, label))
    plt.imshow(image, cmap=plt.get_cmap('gray_r'))
    plt.show()

def getFlattenArray(img):
    # flatten image 
    in_arr = np.array(img)
    out_arr = in_arr.flatten()
    out_arr = out_arr.tolist()

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

#        cv2.imshow("Frame", resized)
#        display_sample(gray, width, height)
        # Press Q on keyboard to  exit
        if cv2.waitKey(25) & 0xFF == ord('q'):
            break

        flat_img = getFlattenArray(resized)
        print(len(flat_img))
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
getFramesFromVideo("./attack/parker3.mp4", 1)
getFramesFromVideo("./attack/parker3.mp4", 1)
getFramesFromVideo("./attack/parker4.mp4", 1)
getFramesFromVideo("./gooch/parker1.mp4", 0)
getFramesFromVideo("./gooch/parker2.mp4", 0)
getFramesFromVideo("./gooch/parker3.mp4", 0)
getFramesFromVideo("./gooch/parker4.mp4", 0)

model = Sequential()
model.add(Dense(512, activation='relu', input_shape=(1824,)))
model.add(Dense(2, activation='softmax'))

model.summary()

# optimizer and loss function? TODO: Figure out what this is 
model.compile(loss='categorical_crossentropy',
              optimizer=RMSprop(),
              metrics=['accuracy'])

# shuffle train data
for i in range(len(train_data)-1, 0, -1): 
      
    # Pick a random index from 0 to i  
    j = random.randint(0, i + 1)  
    
    # Swap arr[i] with the element at random index  
    train_data[i], train_data[j] = train_data[j], train_data[i]  


# split data into train and test data
print("Length = " + str(len(train_data)))
split = int(len(train_data) * 0.8)
print("Split at " + str(split))
test_data = train_data[split:]
train_data = train_data[:split]

# split train_data into train_x and train_y
x_train = []
y_train = []
for pair in train_data:
    x_train.append(pair[0])
    y_train.append(pair[1])

x_test = []
y_test = []
for pair in test_data:
    x_test.append(pair[0])
    y_test.append(pair[1])

#print(train_data)
#x_train, y_train = map(list,zip(*train_data))
#x_train = x_train.tolist()
#y_train = np.asarray(y_train, dtype=np.uint8)

# create test data 


#print(x_train)
#print(y_train)
import os

checkpoint_path = "checkpoints/v1.ckpt"
checkpoint_dir = os.path.dirname(checkpoint_path)

# Create a callback that saves the model's weights
cp_callback = tf.keras.callbacks.ModelCheckpoint(filepath=checkpoint_path,
                                                 save_weights_only=True,
                                                 verbose=1)


# fit the model to the training data 
history = model.fit(x_train, y_train,
                    batch_size=100,
                    epochs=5,
                    verbose=2,
                    shuffle=True,
                    callbacks=[cp_callback],
                    validation_data=(x_test, y_test))

# evaluate the model on new images 
score = model.evaluate(x_test, y_test, verbose=0)
print('Test loss:', score[0])
print('Test accuracy:', score[1])

model.save("model-v2.h5")

#saver = tf.compat.v1.train.Saver()
#sess = tf.Session()
#sess.run(tf.global_variables_initializer())
#saver.save(sess, 'heart_attack_v1')

for x in range(len(test_data)):
    test_image = [test_data[x][0]]
#    print(test_image)
#    print(len(test_image))
    predicted = model.predict(test_image).argmax()
    label = 0
    if (test_data[x][1][1] == 1):
        label = 1

    if (predicted != label):
#        plt.title('Prediction: %d Label: %d' % (predicted, label))
#        plt.imshow(test_data[x][0], cmap=plt.get_cmap('gray_r'))
#        plt.show()
        display_sample(test_data[x][0],0,0)

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
