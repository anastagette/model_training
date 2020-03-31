import tensorflow as tf
from tensorflow import keras
import numpy as np
from os import listdir
import wave
import struct
import noisereduce as nr

def elements_amount(dict_label, n):
    for i in range(len(dict_label)):
        for j in listdir(dict.get(dict_label, i+1)):
            n += 1
    return n

def convertation(datalist, dict_labels):
    for j in dict_labels:
        for i in listdir(dict.get(dict_labels, j+1)):
            try:
                data_one = wave.open(i, 'r')
                frames_count = data_one.getframerate()
                data_list = struct.unpack('<' + str(frames_count) + 'h', data_one.readframes(frames_count))
                np_data_list = np.array(data_list)
                reduced_noise = nr.reduce_noise(audio_clip=np_data_list, noise_clip=np_data_list, verbose=True)
                data_one.close()
                datalist.append(reduced_noise)
            except:
                continue

numerals_dict_labels = {1: '/home/anastagette/PycharmProjects/soundaudiowork/datasets/data_speech_commands_v0.02/one',
                        2: '/home/anastagette/PycharmProjects/soundaudiowork/datasets/data_speech_commands_v0.02/two'}
big_boss_datalist = np.empty(shape=(elements_amount(numerals_dict_labels, 0), 1))
convertation(big_boss_datalist, numerals_dict_labels)
print(big_boss_datalist)

test_numerals_dict_labels = {1: '/home/anastagette/PycharmProjects/soundaudiowork/datasets/datasets_for_tests/one',
                             2: '/home/anastagette/PycharmProjects/soundaudiowork/datasets/datasets_for_tests/two'}
test_big_boss_datalist = np.empty(shape=(elements_amount(test_numerals_dict_labels, 0), 1))
convertation(test_big_boss_datalist, test_numerals_dict_labels)
print(test_big_boss_datalist)

train_sounds = big_boss_datalist
train_labels = [[1] for i in range(elements_amount(numerals_dict_labels, 0))]
train_labels = np.expand_dims(train_labels, 0).reshape(elements_amount(numerals_dict_labels, 0), 1)
model = keras.Sequential([keras.layers.Dense(128, activation='relu'),
                          keras.layers.Dense(2, activation='softmax')])
model.compile(loss=keras.losses.categorical_crossentropy,
              optimizer='adam',
              metrics=['accuracy'])
model.fit(train_sounds, train_labels)

prediction = model.predict(test_big_boss_datalist)
for i in range(elements_amount(test_numerals_dict_labels, 0)):
    print(prediction[i])