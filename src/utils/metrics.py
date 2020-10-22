"""
Implement metrics that estimates a model's effectiveness.
@author: Ying Meng (y(dot)meng201011(at)gmail(dot)com)
"""

import numpy as np


def error_rate(y_pred, y_true, correct_on_bs=None):
    '''
    Compute the error rate
    :param y_pred: predictions
    :param y_true: ground truth
    :param correct_on_bs: indices of corresponding benign samples that
            are correctly classified by the undefended model.
    :return: the error rate
    '''
    if len(y_pred.shape) > 1:
        y_pred = np.asarray([np.argmax(p) for p in y_pred])

    if len(y_true.shape) > 1:
        y_true = np.asarray([np.argmax(p) for p in y_true])

    amount = y_pred.shape[0] if correct_on_bs is None else len(correct_on_bs)

    # Count the number of inputs which successfully fool the model.
    # that is f(x') != f(x).
    if correct_on_bs is not None:
        num_fooled = np.sum([1. for i in range(amount) if (i in correct_on_bs) and (y_pred[i] != y_true[i])])
    else:
        num_fooled = np.sum([1. for i in range(amount) if (y_pred[i] != y_true[i])])

    score = float(num_fooled / amount)
    return score


def get_corrections(y_pred, y_true):
    """
    Collect the indices of the images that are miscalssified.
    :param y_pred: predictions.
    :param y_true: ground truth
    :return:
    """
    y_true = np.asarray(y_true)
    y_pred = np.asarray(y_pred)

    if len(y_pred.shape) > 1:
        y_pred = np.asarray([np.argmax(p) for p in y_pred])
    if len(y_true.shape) > 1:
        y_true = np.asarray([np.argmax(p) for p in y_true])

    corrections = [i for i in range(y_true.shape[0]) if y_pred[i]==y_true[i]]

    return corrections