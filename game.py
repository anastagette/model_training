import tensorflow as tf
import librosa
import matplotlib.pyplot as plt
import numpy as np
from os import listdir
from os.path import join
import split_folders
import keras_preprocessing
from keras_preprocessing import image
from keras_preprocessing.image import ImageDataGenerator

# audio_data = '/home/anastagette/PycharmProjects/soundaudiowork/data_speech_commands_v0.02 (1)/two'
# for i in listdir(audio_data):
#     x, sr = librosa.load(join(audio_data, i), sr=8000)
#     mfccs = librosa.feature.mfcc(x).flatten()
#     print(mfccs.shape)
#     cmap = plt.get_cmap('inferno')
#     plt.figure(figsize=(4, 4))
#     plt.specgram(mfccs, NFFT=64, Fs=2, Fc=0, noverlap=4, cmap=cmap)
#     plt.axis('off')
#     plt.savefig(f'/home/anastagette/PycharmProjects/barakholka/audio_to_image/two/{i[:-3].replace(".", "")}.png')
#
# split_folders.ratio('audio_to_image', output='data_of_images')

train_dir = '/home/anastagette/PycharmProjects/barakholka/data_of_images/train'
val_dir = '/home/anastagette/PycharmProjects/barakholka/data_of_images/val'
test_dir = '/home/anastagette/PycharmProjects/barakholka/data_of_images/test'

train_generator = ImageDataGenerator().flow_from_directory(train_dir,
                                                            batch_size=8,
                                                            target_size=(4, 4),
                                                            class_mode='binary')

# image_1, label_1 = next(train_generator)
# image_1 = np.array(image_1[0], dtype=int)
# print(image_1[0, 0], label_1)
# plt.imshow(image_1)
# plt.show()

val_generator = ImageDataGenerator().flow_from_directory(val_dir,
                                                        batch_size=8,
                                                        target_size=(4, 4),
                                                        class_mode='binary')
test_generator = ImageDataGenerator().flow_from_directory(test_dir,
                                                         batch_size=8,
                                                         target_size=(4, 4),
                                                         class_mode='binary')

model = tf.keras.models.Sequential([
    tf.keras.layers.Conv2D(64, (3, 3),  input_shape=(4, 4, 3), activation='relu'),
    tf.keras.layers.MaxPooling2D(2, 2),
    # tf.keras.layers.Conv2D(64, (3, 3), activation='relu'),
    # tf.keras.layers.MaxPooling2D(2, 2),
    # tf.keras.layers.Conv2D(128, (3, 3), activation='relu'),
    # tf.keras.layers.MaxPooling2D(2, 2),
    # tf.keras.layers.Conv2D(128, (3, 3), activation='relu'),
    # tf.keras.layers.MaxPooling2D(2, 2),
    tf.keras.layers.Flatten(),
    # tf.keras.layers.Dropout(0.5),
    tf.keras.layers.Dense(512, activation='relu'),
    tf.keras.layers.Dense(3, activation='softmax')
])

model.summary()

model.compile(loss='sparse_categorical_crossentropy', optimizer='rmsprop', metrics=['accuracy'])
print(type(train_generator))

history = model.fit(train_generator)
print(model.evaluate_generator(generator=val_generator))

# acc = history.history['acc']
# val_acc = history.history['val_acc']
# loss = history.history['loss']
# val_loss = history.history['val_loss']
#
# epochs = range(len(acc))
#
# plt.plot(epochs, acc, 'r', label='Training accuracy')
# plt.plot(epochs, val_acc, 'b', label='Validation accuracy')
# plt.title('Training and validation accuracy')
# plt.legend(loc=0)
# plt.figure()
# plt.show()

test_img, test_labels = next(test_generator)
test_img = np.array(test_img[0])
test_img = np.expand_dims(test_img, 0)
print(test_img.shape)
predictions = model.predict_generator(test_img)
print(predictions)
