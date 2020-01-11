from tensorflow import keras
from tensorflow.keras.datasets import mnist
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout
from tensorflow.keras.optimizers import RMSprop

# import a bunch of practice data 
(mnist_train_images, mnist_train_labels), (mnist_test_images, mnist_test_labels) = mnist.load_data()

train_images = mnist_train_images.reshape(60000, 784)
test_images = mnist_test_images.reshape(10000, 784)
train_images = train_images.astype('float32')
test_images = test_images.astype('float32')
train_images /= 255
test_images /= 255

print(train_images[0])

train_labels = keras.utils.to_categorical(mnist_train_labels, 10)
test_labels = keras.utils.to_categorical(mnist_test_labels, 10)

import matplotlib.pyplot as plt

# show what the data looks like
def display_sample(num):
    #Print the one-hot array of this sample's label 
    print(train_labels[num])  
    #Print the label converted back to a number
    label = train_labels[num].argmax(axis=0)
    #Reshape the 768 values to a 28x28 image
    image = train_images[num].reshape([28,28])
    plt.title('Sample: %d  Label: %d' % (num, label))
    plt.imshow(image, cmap=plt.get_cmap('gray_r'))
    plt.show()
    
#display_sample(1234)

# create an input of 784 features into 512 nodes, and then into 10 nodes (the output layer) with softmax applied 
model = Sequential()
model.add(Dense(512, activation='relu', input_shape=(784,)))
model.add(Dense(10, activation='softmax'))

model.summary()

# optimizer and loss function? TODO: Figure out what this is 
model.compile(loss='categorical_crossentropy',
              optimizer=RMSprop(),
              metrics=['accuracy'])

print("TEST")
print(train_images[0])
print("TEST")
print(train_labels[0])
print("TEST")

print(len(train_images))
print(len(train_labels))

# fit the model to the training data 
history = model.fit(train_images, train_labels,
                    batch_size=100,
                    epochs=3,
                    verbose=2,
                    shuffle=True,
                    validation_data=(test_images, test_labels))

# evaluate the model on new images 
score = model.evaluate(test_images, test_labels, verbose=0)
print('Test loss:', score[0])
print('Test accuracy:', score[1])

for x in range(1000):
    test_image = test_images[x,:].reshape(1,784)
    print(test_image)
    print("New")
    predicted_cat = model.predict(test_image).argmax()
    label = test_labels[x].argmax()
    print(label)
    if (predicted_cat != label):
        plt.title('Prediction: %d Label: %d' % (predicted_cat, label))
        print(test_image.reshape([28,28]))
        plt.imshow(test_image.reshape([28,28]), cmap=plt.get_cmap('gray_r'))
        plt.show()
