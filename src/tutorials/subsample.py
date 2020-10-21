"""
An example for getting a random subsample of benign samples.
@author: Ying Meng (y(dot)meng201011(at)gmail(dot)com)
"""

import argparse
import numpy as np
import os

from utils.data import subsampling
from utils.file import load_from_json


if __name__=="__main__":
    parser = argparse.ArgumentParser(description="")

    """
    configurations under ``configs/demo`` are for demo.
    """

    parser.add_argument('-d', '--data-configs', required=False,
                        default='../configs/demo/data-mnist.json',
                        help='Folder where test data stored in.')
    parser.add_argument('-o', '--output-root', required=False,
                        default='../../results',
                        help='Folder for outputs.')
    parser.add_argument('--debug', required=False, default=True)
    args = parser.parse_args()

    data_configs = load_from_json(args.data_configs)
    # load the benign samples
    bs_file = os.path.join(data_configs.get('dir'), data_configs.get('bs_file'))
    x_bs = np.load(bs_file)
    img_rows, img_cols = x_bs.shape[1], x_bs.shape[2]

    # load the corresponding true labels
    label_file = os.path.join(data_configs.get('dir'), data_configs.get('label_file'))
    labels = np.load(label_file)

    # get random subsamples
    # for MNIST, num_classes is 10
    # files "subsamples-mnist-ratio_0.1-xxxxxx.npy" and "sublabels-mnist-ratio_0.1-xxxxxx.npy"
    # will be generated and saved at "/results" folder, where "xxxxxx" are timestamps.
    subsamples, sublabels = subsampling(data=x_bs,
                                        labels=labels,
                                        num_classes=10,
                                        filepath=args.output_root,
                                        filename='mnist')
