"""
A sample to generate adversarial examples.
@author: Ying Meng (y(dot)meng201011(at)gmail(dot)com)
"""

import argparse
import numpy as np
import os
import time
from matplotlib import pyplot as plt

from utils.model import load_lenet
from utils.file import load_from_json
from attacks.attack import generate
import metrics


def generate_ae(model, data, labels, attack_configs, save=False, output_dir=None):
    """
    Generate adversarial examples
    :param model: WeakDefense. The targeted model.
    :param data: array. The benign samples to generate adversarial for.
    :param labels: array or list. The true labels.
    :param attack_configs: dictionary. Attacks and corresponding settings.
    :param save: boolean. True, if save the adversarial examples.
    :param output_dir: str or path. Location to save the adversarial examples.
        It cannot be None when save is True.
    :return:
    """
    img_rows, img_cols = data.shape[1], data.shape[2]
    num_attacks = attack_configs.get("num_attacks")
    data_loader = (data, labels)

    if len(labels.shape) > 1:
        labels = np.array([np.argmax(p) for p in labels])
        # might have to convert this to an array

    # generate attacks one by one
    for id in range(num_attacks):
        key = "configs{}".format(id)
        config = attack_configs.get(key)
        data_adv = generate(model=model,
                            data_loader=data_loader,
                            attack_args=attack_configs.get(key)
                            )

        # predict the adversarial examples
        predictions = model.predict(data_adv)
        predictions = np.array([np.argmax(p) for p in predictions])

        error_rate = metrics.error_rate_single(predictions, labels)
        print(config.get('description') + ' Error Rate: ' + str(error_rate))


        # # plotting some examples
        num_plotting = min(data.shape[0], 3)
        for i in range(num_plotting):
            img = data_adv[i].reshape((img_rows, img_cols))
            plt.imshow(img, cmap='gray')
            title = '{}: {}->{}'.format(attack_configs.get(key).get("description"),
                                        labels[i],
                                        predictions[i]
                                        )
            plt.title(title)
            plt.show()
            plt.close()

        # save the adversarial example
        if save:
            if output_dir is None:
                raise ValueError("Cannot save images to a none path.")
            # save with a random name
            file = os.path.join(output_dir, "minerva_AE-{}.npy".format(config.get('description')))
            print("Save the adversarial examples to file [{}].".format(file))
            np.save(file, data_adv)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="")

    parser.add_argument('-m', '--model-configs', required=False,
                        default='../configs/experiment/model-mnist.json',
                        help='Folder where models stored in.')
    parser.add_argument('-d', '--data-configs', required=False,
                        default='../configs/experiment/data-mnist.json',
                        help='Folder where test data stored in.')
    parser.add_argument('-a', '--attack-configs', required=False,
                        default='../configs/experiment/attack-zk-mnist.json',
                        help='Folder where test data stored in.')
    parser.add_argument('-o', '--output-root', required=False,
                        default='../configs/experiment/results',
                        help='Folder for outputs.')
    parser.add_argument('--debug', required=False, default=True)

    args = parser.parse_args()

    print("------AUGMENT SUMMARY-------")
    print("MODEL CONFIGS:", args.model_configs)
    print("DATA CONFIGS:", args.data_configs)
    print("ATTACK CONFIGS:", args.attack_configs)
    print("OUTPUT ROOT:", args.output_root)
    print("DEBUGGING MODE:", args.debug)
    print('----------------------------\n')

    # parse configurations (into a dictionary) from json file
    model_configs = load_from_json(args.model_configs)
    data_configs = load_from_json(args.data_configs)
    attack_configs = load_from_json(args.attack_configs)

    # load the targeted model
    model_file = os.path.join(model_configs.get("dir"), model_configs.get("um_file"))
    target = load_lenet(file=model_file, wrap=True)

    # load the benign samples
    data_file = os.path.join(data_configs.get('dir'), data_configs.get('bs_file'))
    data_bs = np.load(data_file)

    # load the corresponding true labels
    label_file = os.path.join(data_configs.get('dir'), data_configs.get('label_file'))
    labels = np.load(label_file)

    # generate adversarial examples for a small subset
    data_bs = data_bs[:1000]
    labels = labels[:1000]
    generate_ae(model=target, data=data_bs, labels=labels, attack_configs=attack_configs)
