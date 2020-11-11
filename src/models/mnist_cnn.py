"""
Define and implement models for MNIST
@author: Ying Meng (y(dot)meng201011(at)gmail(dot)com)
"""

import argparse
import os

import keras

import utils.file as file
from utils.data import load_mnist
from utils.file import load_from_json
from models.image_processor import transform


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
def train(trainset, testset, trans_configs=None, training_configs=None, model_configs=None):
	if trainset is None or testset is None:
		raise ValueError("Dataset cannot be None.")

	if trans_configs is None:
		# by default, training model on clean data
		trans_configs = {
			"type": "clean",
			"subtype": "",
			"id": 0,
			"description": "clean"
		}

	if training_configs is None:
		# default training configuration
		training_configs = {
			"learning_rate": 0.001,
			"validation_rate": 0.2,
			"optimizer": keras.optimizers.Adam(lr=0.001),
			"loss": keras.losses.categorical_crossentropy,
			"metrics": "default",

		}

	if model_configs is None:
		# default model configurations
		model_configs = {
			"model_dir": "model",
			"model_name": "model-cnn-{}.h5".format(trans_configs.get("description")),
		}

	# get network
	model = cnn()

	X_train, Y_train = trainset
	X_test, Y_test = testset

	# apply transformation
	X_train = transform(X_train, trans_configs)

	learning_rate = training_configs.get("learning_rate", 0.001)
	validation_rate = training_configs.get("validation_rate", 0.2)

	optimizer = training_configs.get('optimizer', keras.optimizers.Adam(lr=learning_rate))
	loss_func = training_configs.get('loss', keras.losses.categorical_crossentropy)
	metrics = training_configs.get('metrics', 'default')

	print('Training weak defense [{}]...'.format(trans_configs.get("description")))
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
						verbose=1, validation_data=(val_examples, val_labels))

	model_dir = model_configs.get('model_dir', 'models')
	# name in pattern: model-<architecture>-<transformation>.h5
	model_name = model_configs.get("model_name", "model-cnn-{}.h5".format(trans_configs.get("description")))
	savefile = os.path.join(model_dir, model_name)
	print('Save the trained model to [{}]'.format(savefile))
	model.save(savefile)

	# evaluate the model
	scores_train = model.evaluate(train_examples, train_labels, batch_size=128, verbose=0)
	scores_val = model.evaluate(val_examples, val_labels, batch_size=128, verbose=0)

	X_test = transform(X_test, trans_configs)
	scores_test = model.evaluate(X_test, Y_test, batch_size=128, verbose=0)

	"""
	report
	"""
	print('\t\t\t loss, \t acc (BS/AE)')
	print("training set: {}".format(scores_train))
	print("validation set: {}".format(scores_val))
	print("test set: {}".format(scores_test))
	print("")

	log_dir = training_configs.get("checkpoint_folder", "checkpoints")
	savefile = savefile.replace(".h5", "")
	file.dict2csv(history.history, '{}/checkpoint-{}.csv'.format(log_dir, savefile))


if __name__=="__main__":
	parser = argparse.ArgumentParser(description="Training a CNN model on MNIST.")
	parser.add_argument("--trans-configs", required=False,
						default="../configs/experiment/athena-mnist.json")
	parser.add_argument("--train-configs", required=False,
						default=None)
	parser.add_argument("--model-configs", required=False,
						default=None)
	args = parser.parse_args()

	# load configurations
	trans_configs = load_from_json(args.trans_configs)
	if args.train_configs is not None:
		training_configs = load_from_json(args.train_configs)
	else:
		training_configs = None

	if args.model_configs is not None:
		model_configs = load_from_json(args.model_configs)
	else:
		model_configs = None

	(X_train, Y_train), (X_test, Y_test) = load_mnist()

	# train weak defenses using default configurations
	training_wd_ids = trans_configs.get("active_wds")
	for id in training_wd_ids:
		key = "configs{}".format(id)
		train(trainset=(X_train, Y_train),
			  testset=(X_test, Y_test),
			  trans_configs=trans_configs.get(key))