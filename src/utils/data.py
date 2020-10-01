"""

@author: Ying Meng (y(dot)meng201011(at)gmail(dot)com)
"""

import os
import random

import keras
import numpy as np
from keras.datasets import mnist as MNIST
from keras.datasets import cifar100 as CIFAR100

from torchvision import datasets, transforms
import torch
from torch.utils.data import DataLoader, TensorDataset

random.seed(1000)


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
