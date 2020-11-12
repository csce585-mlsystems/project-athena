"""
A sample to evaluate model on dataset
@author: Ying Meng (y(dot)meng201011(at)gmail(dot)com)
"""

import argparse
import numpy as np
import os
import random
import time
from matplotlib import pyplot as plt, image

from utils.model import load_pool, load_lenet
from utils.file import load_from_json
from utils.metrics import error_rate, get_corrections
from models.athena import Ensemble, ENSEMBLE_STRATEGY
from models.image_processor import transform


def evaluate(trans_configs, model_configs,
             data_configs, save=True, output_dir='../../results'):
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
    # Load the baseline defense (PGD-ADT model)
    baseline = load_lenet(file=model_configs.get('pgd_trained'), trans_configs=None,
                                  use_logits=False, wrap=False)

    # get the undefended model (UM)
    file = os.path.join(model_configs.get('dir'), model_configs.get('um_file'))
    undefended = load_lenet(file=file,
                            trans_configs=trans_configs.get('configs0'),
                            wrap=True)
    print(">>> um:", type(undefended))

    # load weak defenses into a pool
    pool, _ = load_pool(trans_configs=trans_configs,
                        model_configs=model_configs,
                        active_list=True,
                        wrap=True)
    # create an AVEP ensemble from the WD pool
    wds = list(pool.values())
    print(">>> wds:", type(wds), type(wds[0]))
    ensemble = Ensemble(classifiers=wds, strategy=ENSEMBLE_STRATEGY.AVEP.value)

    # load the benign samples
    bs_file = os.path.join(data_configs.get('dir'), data_configs.get('bs_file'))
    x_bs = np.load(bs_file)
    img_rows, img_cols = x_bs.shape[1], x_bs.shape[2]

    # load the corresponding true labels, take just the first 1000
    label_file = os.path.join(data_configs.get('dir'), data_configs.get('label_file'))
    labels = np.load(label_file)
    labels = labels[:1000]

    # get indices of benign samples that are correctly classified by the targeted model
    print(">>> Evaluating UM on [{}], it may take a while...".format(bs_file))
    pred_bs = undefended.predict(x_bs)
    corrections = get_corrections(y_pred=pred_bs, y_true=labels)
    print(output_dir)
    if save:
        if output_dir is None:
            raise ValueError("Cannot save to a none path.")
        # save with a random name
        f = os.path.join(output_dir, "minerva_AE-results2.txt")
        out_file = open(f, 'a')
        out_file.write('\n\n')
        out_file.write('--------------------------------------NEW RANDOM TEST--------------------------------------\n')
        out_file.write('|                                                                                         |\n')
        out_file.write('|  NEW TEST DATA WITH THE FOLLOWING RANDOM WD\'S                                           |\n')
        out_file.write(str(list(trans_configs.get('active_wds'))) + '\n')

    # Evaluate AEs.
    ae_list = data_configs.get('ae_files')
    for _ in range(len(ae_list)):
        results = {}
        ae_file = os.path.join(data_configs.get('dir'), ae_list[_])
        print(ae_list[_])
        print(ae_file)
        x_adv = np.load(ae_file)

        # evaluate the undefended model on the AE
        print(">>> Evaluating UM on [{}], it may take a while...".format(ae_file))
        pred_adv_um = undefended.predict(x_adv)
        err_um = error_rate(y_pred=pred_adv_um, y_true=labels, correct_on_bs=corrections)
        # track the result
        results['UM'] = err_um

        # evaluate the ensemble on the AE
        print(">>> Evaluating ensemble on [{}], it may take a while...".format(ae_file))
        pred_adv_ens = ensemble.predict(x_adv)
        err_ens = error_rate(y_pred=pred_adv_ens, y_true=labels, correct_on_bs=corrections)
        # track the result
        results['Ensemble'] = err_ens

        # evaluate the baseline on the AE
        print(">>> Evaluating baseline model on [{}], it may take a while...".format(ae_file))
        pred_adv_bl = baseline.predict(x_adv)
        err_bl = error_rate(y_pred=pred_adv_bl, y_true=labels, correct_on_bs=corrections)
        # track the result
        results['PGD-ADT'] = err_bl

        out_file.write(">>> Evaluations on [{}]:\n{}\n".format(ae_file, results))


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="")

    """
    configurations under ``configs/demo`` are for demo.
    """

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
                        default='../../results',
                        help='Folder for outputs.')
    parser.add_argument('--debug', required=False, default=True)
    parser.add_argument('-s', '--save-results', required=False, default=True, help='Save output or not')

    args = parser.parse_args()

    print('------AUGMENT SUMMARY-------')
    print('TRANSFORMATION CONFIGS:', args.trans_configs)
    print('MODEL CONFIGS:', args.model_configs)
    print('DATA CONFIGS:', args.data_configs)
    print('OUTPUT ROOT:', args.output_root)
    print('DEBUGGING MODE:', args.debug)
    print('SAVING OUTPUT:', args.save_results)
    print('----------------------------\n')

    # parse configurations (into a dictionary) from json file
    trans_configs = load_from_json(args.trans_configs)
    model_configs = load_from_json(args.model_configs)
    data_configs = load_from_json(args.data_configs)

    # do 10 times
    for _ in range(10):
        # pick random number of wd's
        num = random.randint(1, 72)
        wd_ids = []
        for _ in range(num):
            temp = random.randint(1, 72)
            while temp in wd_ids:
                temp = random.randint(1, 72)

            wd_ids.append(temp)
        trans_configs['active_wds'] = wd_ids

        # -------- test transformations -------------
        evaluate(trans_configs=trans_configs,
                 model_configs=model_configs,
                 data_configs=data_configs,
                 save=args.save_results,
                 output_dir=args.output_root)
