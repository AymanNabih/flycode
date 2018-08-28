'''Train a two-layer neural network on the CIFAR10 small images dataset.

It gets to around 48% validation accuracy at 50 epochs.
'''

import keras
from keras.datasets import cifar10
from keras.models import Sequential, load_model
from keras.layers import Dense, Flatten
from keras.optimizers import RMSprop
from keras.callbacks import ModelCheckpoint

batch_size = 128
epochs = 5
num_unit = 200

num_classes = 10
img_dim = 32
img_channels = 3
input_size = img_dim * img_dim * img_channels
input_shape = (img_dim, img_dim, img_channels)

# The data, split between train and test sets:
(x_train, y_train), (x_test, y_test) = cifar10.load_data()

x_train = x_train.astype('float32')
x_test = x_test.astype('float32')
x_train /= 255
x_test /= 255
print('x_train shape:', x_train.shape)
print('x_test shape:', x_test.shape)

# Convert class vectors to binary class matrices.
y_train = keras.utils.to_categorical(y_train, num_classes)
y_test = keras.utils.to_categorical(y_test, num_classes)
print('y_train shape:', y_train.shape)
print('y_test shape:', y_test.shape)

use_bias = False

model = Sequential()
model.add(Flatten(input_shape=input_shape))
model.add(Dense(num_unit, activation='relu', use_bias=use_bias))
model.add(Dense(num_classes, activation='softmax', use_bias=use_bias))

model.summary()

model.compile(loss='categorical_crossentropy',
              optimizer='rmsprop',
              metrics=['accuracy'])
model_checkpoint = ModelCheckpoint('./keras_cifar10_trained.model', save_best_only=True, verbose=1)

history = model.fit(x_train, y_train, validation_data=(x_test, y_test),
                    batch_size=batch_size, epochs=epochs,
                    callbacks=[model_checkpoint], verbose=1)

model = load_model('./keras_cifar10_trained.model')

# Score trained model.
scores = model.evaluate(x_test, y_test, verbose=1)
print('Test loss:', scores[0])
print('Test accuracy:', scores[1])

import numpy as np

#xs = np.array([1,2])
#ys= np.array([1,2])
xs = np.linspace(10, 220, 15) # nn_hidden
ys = np.linspace(1, 127, 15) # batch_size

reps = 5

zs = np.zeros([reps, xs.shape[0], ys.shape[0]])
epochs = 25

import time

t0 = time.time()
for k in range(reps):
    for i,x in enumerate(xs):
        for j,y in enumerate(ys):
            history = model.fit(x_train, y_train, validation_data=(x_test, y_test),
                                batch_size=batch_size, epochs=epochs,
                                callbacks=[model_checkpoint], verbose=1)
            zs[k,i,j] = np.max(history.history['val_acc'])
tf = time.time()
t_min = (tf-t0)/60
print("Time per rep: " + str(t_min) + " min")

Z = zs.reshape(reps, xs.shape[0]*xs.shape[0])
np.savetxt('Z.csv', Z, delimiter=',', fmt='%.04f')






