from keras.models import Sequential, load_model
from keras.preprocessing.image import ImageDataGenerator
from keras.layers import Dense, Activation, Conv2D, MaxPooling2D, Dropout, Flatten
from keras.utils.np_utils import to_categorical
from .utils import loadData, listToJsonDict
from math import inf
from PIL import Image
import numpy as np
import os
import keras

batch_size = 30
num_classes = 195
epochs = 200
size = (60, 60)

def createCNN():

    (x_train, y_train), (x_test, y_test) = loadData()
    y_train = to_categorical(y_train, num_classes)
    y_test = to_categorical(y_test, num_classes)
    x_train = x_train.astype('float32')
    x_test = x_test.astype('float32')

    model = Sequential()
    model.add(Conv2D(60, (5, 5),
                     input_shape=(60, 60, 3),
                     ))
    model.add(Activation('relu'))
    model.add(MaxPooling2D(pool_size=(3, 3)))
    model.add(Dropout(0.25))
    model.add(Flatten())
    model.add(Dense(1800))
    model.add(Activation('tanh'))
    model.add(Dropout(0.25))
    model.add(Dense(num_classes))
    model.add(Activation('softmax'))

    model.compile(loss='categorical_crossentropy',
              optimizer=keras.optimizers.SGD(lr=0.0001, decay=1e-6),
              metrics=['accuracy'])
    
    datagen = ImageDataGenerator(
        rotation_range=5,
        width_shift_range=0.05,
        height_shift_range=0.05)

    datagen.fit(x_train)
    model.fit_generator(datagen.flow(x_train, y_train,
                                     batch_size=batch_size),
                        epochs=epochs,
                        validation_data=(x_test, y_test),
                        workers=8)

    model.save('../static/model.h5')

    scores = model.evaluate(x_test, y_test, verbose=1)
    print('Test loss:', scores[0])
    print('Test accuracy:', scores[1])
    
def restartLearning():

    model = load_model('../static/model.h5')
    (x_train, y_train), (x_test, y_test) = loadData()
    y_train = to_categorical(y_train, num_classes)
    y_test = to_categorical(y_test, num_classes)
    x_train = x_train.astype('float32')
    x_test = x_test.astype('float32')

    datagen = ImageDataGenerator(
        rotation_range=5,
        width_shift_range=0.05,
        height_shift_range=0.05)

    datagen.fit(x_train)
    model.fit_generator(datagen.flow(x_train, y_train,
                                     batch_size=batch_size),
                        epochs=epochs,
                        validation_data=(x_test, y_test),
                        workers=8)

    model.save('../static/model.h5')

    scores = model.evaluate(x_test, y_test)

    return scores

def predict(sample, top=4):

    image = sample.convert("RGB").resize(size)

    model = load_model('/Users/jongyoonlee/Documents/Projects/Vex/Vex/backend/static/model.h5')
    guesses = model.predict(np.array([np.array(image)]))[0]
    best = [(-inf, num_classes)] * top

    for i in range(len(guesses)):
        if (guesses[i], i) > best[0]:
            best[0] = (guesses[i], i)
            best.sort()

    return listToJsonDict(list(map(lambda a: a[1], best))[::-1])

def main():
    #createCNN()
    #restartLearning()
    pass

if __name__ == "__main__":
    main()
