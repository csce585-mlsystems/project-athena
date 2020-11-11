"""
Code pieces for collecting raw values from WDs on the input(s).
@author: Ying Meng (y(dot)meng201011(at)gmail(dot)com)
"""

import sys
sys.path.append("../")

import argparse
import numpy as np
import os
import time

from utils.model import load_pool, load_lenet
from utils.file import load_from_json
from utils.metrics import error_rate, get_corrections
from models.athena import Ensemble, ENSEMBLE_STRATEGY


def collect_raw_prediction(trans_configs, model_configs, data_configs, use_logits=False):
    """

    :param trans_configs:
    :param model_configs:
    :param data_configs:
    :param use_logits: Boolean. If True, the model will return logits value (before ``softmax``),
                    return probabilities, otherwise.
    :return:
    """
    # load the pool and create the ensemble
    pool, _ = load_pool(trans_configs=trans_configs,
                        model_configs=model_configs,
                        active_list=True,
                        use_logits=use_logits,
                        wrap=True
                        )
    athena = Ensemble(classifiers=list(pool.values()),
                      strategy=ENSEMBLE_STRATEGY.MV.value)

    # load test data
    # load the benign samples
    bs_file = os.path.join(data_configs.get('dir'), data_configs.get('bs_file'))
    x_bs = np.load(bs_file)
    # test with a small subset
    x_bs = x_bs[:2]

    # collect raw predictions
    raw_preds = athena.predict(x=x_bs, raw=True)
    print(">>> Shape of raw predictions ({}): {}\n{}".format("logits" if use_logits else "probability",
                                                             raw_preds.shape,
                                                             raw_preds))
    print()

    # get the final predictions
    preds = athena.predict(x=x_bs) # raw is False by default
    print(">>> Shape of predictions ({}): {}\n{}".format("logits" if use_logits else "probability",
                                                         preds.shape,
                                                         preds))


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="")

    """
    configurations under ``configs/demo`` are for demo.
    """

    parser.add_argument('-t', '--trans-configs', required=False,
                        default='../configs/demo/athena-mnist.json',
                        help='Configuration file for transformations.')
    parser.add_argument('-m', '--model-configs', required=False,
                        default='../configs/demo/model-mnist.json',
                        help='Folder where models stored in.')
    parser.add_argument('-d', '--data-configs', required=False,
                        default='../configs/demo/data-mnist.json',
                        help='Folder where test data stored in.')
    parser.add_argument('-o', '--output-root', required=False,
                        default='results',
                        help='Folder for outputs.')
    parser.add_argument('--debug', required=False, default=True)

    args = parser.parse_args()

    print('------AUGMENT SUMMARY-------')
    print('TRANSFORMATION CONFIGS:', args.trans_configs)
    print('MODEL CONFIGS:', args.model_configs)
    print('DATA CONFIGS:', args.data_configs)
    print('OUTPUT ROOT:', args.output_root)
    print('DEBUGGING MODE:', args.debug)
    print('----------------------------\n')

    # parse configurations (into a dictionary) from json file
    trans_configs = load_from_json(args.trans_configs)
    model_configs = load_from_json(args.model_configs)
    data_configs = load_from_json(args.data_configs)

    # collect probabilites
    collect_raw_prediction(trans_configs=trans_configs,
                           model_configs=model_configs,
                           data_configs=data_configs)
    # collect logits
    collect_raw_prediction(trans_configs=trans_configs,
                           model_configs=model_configs,
                           data_configs=data_configs,
                           use_logits=True)