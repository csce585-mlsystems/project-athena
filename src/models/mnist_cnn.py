"""
Define and implement models for MNIST
@author: Ying Meng (y(dot)meng201011(at)gmail(dot)com)
"""

from __future__ import absolute_import, division, print_function

import os
import random

import keras
# from keras import layers, models

import utils.file as file
from utils.transformation_configs import *
from models.image_processor import transform

random.seed(1000)

# -------------------------------------
# Network Architecture
# -------------------------------------
def cnn(input_shape=(28, 28, 1), nb_classes=10):
	struct = [
		keras.layers.Conv2D(filters=32, kernel_size=(3, 3), input_shape=input_shape, activation='relu'),
		keras.layers.MaxPooling2D(pool_size=(2, 2)),

		keras.layers.Conv2D(filters=64, kernel_size=(3, 3), activation='relu'),
		keras.layers.MaxPooling2D(pool_size=(2, 2)),

		keras.layers.Flatten(),
		keras.layers.Dense(64 * 64),
		keras.layers.Dropout(rate=0.4),
		keras.layers.Dense(nb_classes, activation='softmax'),
	]

	model = keras.models.Sequential()
	for layer in struct:
		model.add(layer)

	print(model.summary())

	return model


# -------------------------------------
# Train a weak defense
# -------------------------------------
def train(trainset, testset, processor=None, **kwargs):
	# get network
	model = cnn()

	X_train, Y_train = trainset
	X_test, Y_test = testset

	# apply transformation
	X_train = transform(X_train, processor)

	learning_rate = 0.001
	validation_rate = 0.2

	optimizer = kwargs.get('optimizer', keras.optimizers.Adam(lr=learning_rate))
	loss_func = kwargs.get('loss', keras.losses.categorical_crossentropy)
	metrics = kwargs.get('metrics', 'default')

	print('Training weak defense [{}]...'.format(processor.description))
	print('>>> optimizer: {}'.format(optimizer))
	print('>>> loss function: {}'.format(loss_func))
	print('>>> metrics: {}'.format(metrics))

	nb_examples, img_rows, img_cols, nb_channels = X_train.shape

	nb_training = int(nb_examples * (1. - validation_rate))
	train_examples = X_train[:nb_training]
	train_labels = Y_train[:nb_training]
	val_examples = X_train[nb_training:]
	val_labels = Y_train[nb_training:]

	"""
	compile data
	"""
	if ('default' == metrics):
		model.compile(optimizer=optimizer, loss=loss_func, metrics=['accuracy'])
	else:
		model.compile(optimizer=optimizer, loss=loss_func, metrics=['accuracy', metrics])

	# train the model
	history = model.fit(train_examples, train_labels,
						batch_size=64, epochs=20,
						verbose=2, validation_data=(val_examples, val_labels))

	model_dir = kwargs.get('model_dir', 'models')
	save_file = kwargs.get('model_name', 'demo')
	postfix = kwargs.get('model_format', '.h5')
	model.save(os.path.join(model_dir, save_file + postfix))
	print('Saved the model to file [{}]'.format(os.path.join(model_dir, save_file + postfix)))

	# evaluate the model
	scores_train = model.evaluate(train_examples, train_labels, batch_size=128, verbose=0)
	scores_val = model.evaluate(val_examples, val_labels, batch_size=128, verbose=0)

	X_test = transform(X_test, processor)
	scores_test = model.evaluate(X_test, Y_test, batch_size=128, verbose=0)

	"""
	report
	"""
	print('\t\t\t loss, \t acc (BS/AE)')
	print('training set: {}'.format(scores_train))
	print('validation set: {}'.format(scores_val))
	print('test set: {}'.format(scores_test))
	print('')

	log_dir = kwargs.get('checkpoint_folder', 'checkpoints')
	save_file = save_file.replace(postfix, '')
	file.dict2csv(history.history, '{}/checkpoint-{}.csv'.format(log_dir, save_file))

