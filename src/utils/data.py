"""

@author: Ying Meng (y(dot)meng201011(at)gmail(dot)com)
"""

import os
import random
import time

import keras
import numpy as np
from keras.datasets import mnist as MNIST
from keras.datasets import cifar100 as CIFAR100

from torchvision import datasets, transforms
import torch
from torch.utils.data import DataLoader, TensorDataset

#random.seed(1000)


def channels_last(data):
    """
    Check if the image is in the shape of (?, img_rows, img_cols, nb_channels).
    :param data:
    :return: True if channel info is at the last dimension, False otherwise.
    """
    # the images can be color images or gray-scales.
    assert data is not None

    if len(data.shape) > 4 or len(data.shape) < 3:
        raise ValueError('Incorrect dimensions of data (expected 3 or 4): {}'.format(data.shape))
    else:
        return (data.shape[-1] == 3 or data.shape[-1] == 1)


def channels_first(data):
    """
    Check if the image is in the shape of (?, nb_channels, img_rows, img_cols).
    :param data:
    :return: True if channel info is at the first dimension, False otherwise.
    """
    # the images can be color images or gray-scales.
    assert data is not None

    if len(data.shape) > 4 or len(data.shape) < 3:
        raise ValueError('Incorrect dimensions of data (expected 3 or 4): {}'.format(data.shape))
    elif len(data.shape) > 3:
        # the first dimension is the number of samples
        return (data.shape[1] == 3 or data.shape[1] == 1)
    else:
        # 3 dimensional data
        return (data.shape[0] == 3 or data.shape[0] == 1)


def set_channels_first(data):
    if channels_last(data):
        if len(data.shape) == 4:
            data = np.transpose(data, (0, 3, 1, 2))
        else:
            data = np.transpose(data, (2, 0, 1))
    return data


def set_channels_last(data):
    if channels_first(data):
        if len(data.shape) == 4:
            data = np.transpose(data, (0, 2, 3, 1))
        else:
            data = np.transpose(data, (1, 2, 0))
    return data


def get_dataloader(data, labels, batch_size=128, shuffle=False, **kwargs):
    dataset = TensorDataset(torch.Tensor(data), torch.LongTensor(labels))
    dataloader = DataLoader(dataset, batch_size=batch_size, shuffle=shuffle, **kwargs)

    return dataloader


def subsampling(data, labels, ratio=0.1, output=None):
    """
    Subsampling dataset.
    :param data: numpy array. the population dataset to sample from.
    :param labels: numpy array. the corresponding true labels of the population dataset.
    :param ratio: float. the ratio to sample.
    :param output: string or path. the path to save subsampled data and labels.
    :return:
    """
    if data is None or labels is None:
        raise ValueError("`data` and `labels` cannot be None.")

    if ratio <= 0 or ratio > 1:
        raise ValueError("Expect a ratio greater than `0` and no more `1`, but found {}.".format(ratio))

    total = data.shape[0]
    subsize = int(total * ratio)

    # subsampling
    subsample_idx = random.sample(population=[i for i in range(total)],
                                  k=subsize)
    subsamples = np.asarray([data[i] for i in subsample_idx])
    sublabels = np.asarray([labels[i] for i in subsample_idx])

    if output is not None:
        # save the subsamples
        rand_idx = time.monotonic()
        file = os.path.join(output, 'subsamples-ratio_{}-{}.npy'.format(ratio, rand_idx))
        np.save(file=file, arr=subsamples)
        file = os.path.join(output, 'sublabels-ratio_{}-{}.npy'.format(ratio, rand_idx))
        np.save(file=file, arr=sublabels)

    return subsamples, sublabels
