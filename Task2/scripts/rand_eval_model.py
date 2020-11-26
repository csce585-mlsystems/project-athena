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

def evaluate(trans_configs, trans_configs2, model_configs,
             data_configs, save=True, output_dir='../results'):
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
    cnn_configs = model_configs.get('cnn')
    file = os.path.join(cnn_configs.get('dir'), cnn_configs.get('um_file'))
    undefended = load_lenet(file=file,
                            trans_configs=trans_configs.get('configs0'),
                            wrap=True)
    print(">>> um:", type(undefended))

    # load weak defenses into a pool
    cnn_pool, _ = load_pool(trans_configs=trans_configs,
                        model_configs=cnn_configs,
                        active_list=True,
                        wrap=True)
    # create an AVEP ensemble from the WD pool
    cnns = list(cnn_pool.values())

    # load SVM weak defenses into a pool
    # tiny pool: 3 weak defenses
    svm_configs = model_configs.get('svm')
    svm_pool, _ = load_pool(trans_configs=trans_configs2,
                            model_configs=svm_configs,
                            active_list=True,
                            wrap=True)

    svms = list(svm_pool.values())

    wds = cnns
    wds.extend(svms)
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

    if save:
        if output_dir is None:
            raise ValueError("Cannot save to a none path.")
        # save with a random name
        f = os.path.join(output_dir, "minerva_AE_rand_eval_results.txt")
        out_file = open(f, 'a')
        out_file.write('--------------------------------------NEW RANDOM TEST--------------------------------------\n')
        out_file.write('|                                                                                         |\n')
        out_file.write('|  NEW TEST DATA WITH THE FOLLOWING {c} RANDOM CNN\'S AND {s} RANDOM SVM\'S                   \
          |\n'.format(c=len(cnns), s=len(svms)))
        out_file.write('CNNs: {c}\n'.format(c=list(trans_configs.get('active_wds'))))
        out_file.write('SVMS: {s}\n'.format(s=list(trans_configs2.get('active_wds'))))
        out_file.write('\n\n')

    # Evaluate AEs.
    ae_list = data_configs.get('ae_files')
    start = time.time()
    for _ in range(len(ae_list)):
        ae_start = time.time()
        results = {}
        ae_file = os.path.join(data_configs.get('dir'), ae_list[_])
        x_adv = np.load(ae_file)

        # evaluate the undefended model on the AE
        # print(">>> Evaluating UM on [{}], it may take a while...".format(ae_file))
        # pred_adv_um = undefended.predict(x_adv)
        # err_um = error_rate(y_pred=pred_adv_um, y_true=labels, correct_on_bs=corrections)
        # # track the result
        # results['UM'] = err_um

        # evaluate the ensemble on the Hybrid
        print(">>> Evaluating ensemble on [{}], it may take a while...".format(ae_file))
        pred_adv_ens = ensemble.predict(x_adv)
        err_ens = error_rate(y_pred=pred_adv_ens, y_true=labels, correct_on_bs=corrections)
        # track the result
        results['Ensemble'] = err_ens

        ae_end = time.time()
        ae_final = ae_end - ae_start

        # evaluate the baseline on the AE
        # print(">>> Evaluating baseline model on [{}], it may take a while...".format(ae_file))
        # pred_adv_bl = baseline.predict(x_adv)
        # err_bl = error_rate(y_pred=pred_adv_bl, y_true=labels, correct_on_bs=corrections)
        # # track the result
        # results['PGD-ADT'] = err_bl

        out_file.write(">>> Evaluations on [{}]:\n{}\n".format(ae_file, results))
        out_file.write('AE test took {t} seconds\n'.format(t=str(ae_final)))

    end = time.time()
    final = end - start
    out_file.write('Full test suite took {t} seconds\n'.format(t=str(final)))
    out_file.close()


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="")

    """
    configurations under ``configs/demo`` are for demo.
    """

    parser.add_argument('-t', '--trans-configs', required=False,
                        default='../configs/athena-mnist.json',
                        help='Configuration file for transformations.')
    parser.add_argument('-t2', '--trans-configs2', required=False,
                        default='../configs/svm-mnist.json',
                        help='Configuration file for transformations.')
    parser.add_argument('-m', '--model-configs', required=False,
                        default='../configs/hybrid-mnist.json',
                        help='Folder where models stored in.')
    parser.add_argument('-d', '--data-configs', required=False,
                        default='../configs/data-minerva-mnist.json',
                        help='Folder where test data stored in.')
    parser.add_argument('-o', '--output-root', required=False,
                        default='../results',
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
    trans_configs2 = load_from_json(args.trans_configs2)
    model_configs = load_from_json(args.model_configs)
    data_configs = load_from_json(args.data_configs)

    # do 10 times
    for _ in range(10):
        # get random number 0-20 and pick that many wd's from cnn
        cnn_num = random.randint(0, 20)
        cnn_ids = []
        for _ in range(cnn_num):
            temp = random.randint(1, 72)
            while temp in cnn_ids:
                temp = random.randint(1, 72)
            cnn_ids.append(temp)
        cnn_ids.sort()
        trans_configs['active_wds'] = cnn_ids

        # do for svm's as well
        svm_num = 20 - cnn_num
        svm_ids = []
        for _ in range(svm_num):
            temp = random.randint(1, 70)
            while temp in svm_ids:
                temp = random.randint(1, 70)
            svm_ids.append(temp)
        svm_ids.sort()
        trans_configs2['active_wds'] = svm_ids

        # -------- test transformations -------------
        evaluate(trans_configs=trans_configs,
                 trans_configs2=trans_configs2,
                 model_configs=model_configs,
                 data_configs=data_configs,
                 save=args.save_results,
                 output_dir=args.output_root)
