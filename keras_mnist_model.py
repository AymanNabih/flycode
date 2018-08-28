import keras
from keras.datasets import mnist
from keras.models import Sequential
from keras.layers import Dense, Dropout, Flatten
from keras.optimizers import RMSprop
from keras.callbacks import ModelCheckpoint

num_classes = 10
img_dim = 28
img_channels = 1
input_size = img_dim * img_dim * img_channels
#input_shape = (img_dim, img_dim, img_channels)

batch_size = 10
epochs = 25
num_unit = 20

# the data, split between train and test sets
(x_train, y_train), (x_test, y_test) = mnist.load_data()

x_train = x_train.reshape(x_train.shape[0], input_size)
x_test = x_test.reshape(x_test.shape[0], input_size)
#x_train = x_train.reshape(x_train.shape[0], 28,28,1)
#x_test = x_test.reshape(x_test.shape[0], 28,28,1)
x_train = x_train.astype('float32')
x_test = x_test.astype('float32')
x_train /= 255
x_test /= 255
print('x_train shape:', x_train.shape)
print('x_test shape:', x_test.shape)

# convert class vectors to binary class matrices
y_train = keras.utils.to_categorical(y_train, num_classes)
y_test = keras.utils.to_categorical(y_test, num_classes)
print('y_train shape:', y_train.shape)
print('y_test shape:', y_test.shape)

use_bias = False

model = Sequential()
model.add(Dense(num_unit, activation='relu', use_bias=use_bias, input_shape=(input_size,)))
# acc is lower:
#model.add(Dense(num_unit, activation='relu', use_bias=use_bias, input_shape=input_shape))
#model.add(Flatten())
model.add(Dense(num_classes, activation='softmax', use_bias=use_bias))

model.summary()

model.compile(loss='categorical_crossentropy',
              optimizer='rmsprop',
              metrics=['accuracy'])

model_checkpoint = ModelCheckpoint('./keras_mnist_trained.model', save_best_only=True, verbose=1)

history = model.fit(x_train, y_train, validation_data=(x_test, y_test),
                    batch_size=batch_size, epochs=epochs,
                    callbacks=[model_checkpoint], verbose=2)

score = model.evaluate(x_test, y_test, verbose=0)
print('Test loss:', score[0])
print('Test accuracy:', score[1])


