"""

@author: Ying Meng (y(dot)meng201011(at)gmail(dot)com)
"""

import argparse
import numpy as np
import os

from utils.model import load_pool
from utils.file import load_from_json, dump_to_json
from models.image_processor import transform


def test(trans_configs, model_configs,
         data_configs, output_dir):
    import matplotlib.pyplot as plt

    pool, _ = load_pool(trans_configs=trans_configs, model_configs=model_configs)
    data_file = os.path.join(data_configs.get('dir'), data_configs.get('bs_file'))
    label_file = os.path.join(data_configs.get('dir'), data_configs.get('label_file'))
    data_bs = np.load(data_file)
    labels = np.load(label_file)
    print('SHAPES:', data_bs.shape, labels.shape)

    for id, model in pool.items():
        if id == 0: # skip the undefended model
            continue

        key = 'configs{}'.format(id)
        trans_args = trans_configs.get(key)
        print('TRANS CONFIG:', trans_args)
        data_trans = transform(data_bs[:50], trans_args)

        pred = model.predict(data_trans)
        img_idx = 30
        img = data_trans[img_idx].reshape((28, 28))
        plt.imshow(img, cmap='gray')
        title = '{}, {}'.format(trans_args.get('description'), np.argmax(pred[img_idx]))
        plt.title(title)
        plt.show()
        plt.close()


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="")

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

    trans_configs = load_from_json(args.trans_configs)
    model_configs = load_from_json(args.model_configs)
    data_configs = load_from_json(args.data_configs)

    # -------- test transformations -------------
    test(trans_configs=trans_configs, model_configs=model_configs,
         data_configs=data_configs, output_dir=args.output_root)
