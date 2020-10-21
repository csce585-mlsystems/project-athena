"""
This is a sample to apply transformation on images.
@author: Ying Meng (y(dot)meng201011(at)gmail(dot)com)
"""

import argparse
import numpy as np
import os
import time
from matplotlib import pyplot as plt, image

from utils.model import load_pool
from utils.file import load_from_json
from models.image_processor import transform


def test(trans_configs, model_configs,
         data_configs, save=False, output_dir=None):
    """
    Apply transformation(s) on images.
    :param trans_configs: dictionary. The collection of the parameterized transformations to test.
        in the form of
        { configsx: {
            param: value,
            }
        }
        The key of a configuration is 'configs'x, where 'x' is the id of corresponding weak defense.
    :param model_configs:  dictionary. Defines model related information.
        Such as, location, the undefended model, the file format, etc.
    :param data_configs: dictionary. Defines data related information.
        Such as, location, the file for the true labels, the file for the benign samples,
        the files for the adversarial examples, etc.
    :param save: boolean. Save the transformed sample or not.
    :param output_dir: path or str. The location to store the transformed samples.
        It cannot be None when save is True.
    :return:
    """
    # load weak defenses into a pool
    pool, _ = load_pool(trans_configs=trans_configs, model_configs=model_configs)
    # load the benign samples
    data_file = os.path.join(data_configs.get('dir'), data_configs.get('bs_file'))
    data_bs = np.load(data_file)
    img_rows, img_cols = data_bs.shape[1], data_bs.shape[2]
    # load the corresponding true labels
    label_file = os.path.join(data_configs.get('dir'), data_configs.get('label_file'))
    labels = np.load(label_file)
    print('SHAPES:', data_bs.shape, labels.shape)

    # test the loaded weak defenses one by one
    for id, model in pool.items():
        if id == 0: # skip the undefended model, which does not transform the image
            continue

        key = 'configs{}'.format(id)
        trans_args = trans_configs.get(key)
        print('TRANS CONFIG:', trans_args)
        # transform a small subset
        data_trans = transform(data_bs[:50], trans_args)
        # predict the transformed images by the corresponding model (weak defense)
        pred = model.predict(data_trans)

        # plotting a sample
        img_idx = 30
        img = data_trans[img_idx].reshape((img_rows, img_cols))
        plt.imshow(img, cmap='gray')
        title = '{}, {}'.format(trans_args.get('description'), np.argmax(pred[img_idx]))
        plt.title(title)
        plt.show()
        plt.close()

        # save the transformed sample as required
        if save:
            if output_dir is None:
                raise ValueError("Cannot save images to a none path.")
            file = os.path.join(output_dir, "{}.png".format(time.monotonic()))
            image.imsave(file, img)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="")

    parser.add_argument('-t', '--trans-configs', required=False,
                        default='../configs/experiment/athena-mnist.json',
                        help='Configuration file for transformations.')
    parser.add_argument('-m', '--model-configs', required=False,
                        default='../configs/experiment/model-mnist.json',
                        help='Folder where models stored in.')
    parser.add_argument('-d', '--data-configs', required=False,
                        default='../configs/experiment/data-mnist.json',
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

    # -------- test transformations -------------
    test(trans_configs=trans_configs, model_configs=model_configs,
         data_configs=data_configs, save=False, output_dir=args.output_root)
