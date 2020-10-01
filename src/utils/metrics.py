"""
Implement metrics that estimates a model's effectiveness.
@author: Ying Meng (y(dot)meng201011(at)gmail(dot)com)
"""

import numpy as np


def error_rate(y_pred, y_true, incorrect_ids=None):
    '''
    Compute the error rate
    :param y_pred: predictions
    :param y_true: ground truth
    :param incorrect_ids: indices of corresponding benign samples that
            are misclassified by the undefended model.
    :return: the error rate
    '''
    num_incorrect = 0 if incorrect_ids is None else len(incorrect_ids)
    amount = (y_pred.shape[0] - num_incorrect)
    if len(y_pred.shape) > 1:
        y_pred = [np.argmax(p) for p in y_pred]

    if len(y_true.shape) > 1:
        y_true = [np.argmax(p) for p in y_true]

    if incorrect_ids is not None:
        correct = np.sum([1. for i in range(amount) if (i not in incorrect_ids) and (y_pred[i] == y_true[i])])
    else:
        correct = np.sum([1. for i in range(amount) if (y_pred[i] == y_true[i])])

    score = float((amount - correct) / amount)
    # print('*** score:', amount, correct, score)
    return score

