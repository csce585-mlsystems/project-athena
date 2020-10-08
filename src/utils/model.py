"""

@author: Ying Meng (y(dot)meng201011(at)gmail(dot)com)
"""

import argparse
import numpy as np
import os
import json

from keras.models import load_model, Model
from keras.utils import CustomObjectScope
from keras.initializers import glorot_uniform

from models.keras import WeakDefense


def load_pool(trans_configs, model_configs, use_logits=False, wrap=False):
    pool = {}
    trans_list = {}

    num_trans = trans_configs.get("num_transformations")
    for i in range(num_trans):
        key = "configs{}".format(i)
        trans = trans_configs.get(key).get("description")

        model_file = model_configs.get("wd_prefix") + trans + model_configs.get("wd_postfix")
        model_file = os.path.join(model_configs.get("dir"), model_file)

        wd = load_lenet(model_file, trans_configs=trans, use_logits=use_logits, wrap=wrap)
        pool[trans_configs.get(key).get("id")] = wd
        trans_list[trans_configs.get(key).get("id")] = trans_configs.get(key).get("description")

    print('>>> Loaded {} models.'.format(len(pool.keys())))
    return pool, trans_list


def load_lenet(file, trans_configs=None, use_logits=False, wrap=False):
    """
    Load a LeNet model (implemented in keras).
    :param file: str or path. The full-path file name to the trained model.
    :param trans_configs: dictionary. The corresponding transformation settings.
    :param use_logits: boolean. Use the logits or the probabilities.
    :param wrap: boolean. True, if want to wrap the model into a weak defense in Athena.
    :return:
    """
    print('>>> Loading model [{}]...'.format(file))
    with CustomObjectScope({"GlorotUniform": glorot_uniform()}):
        model = load_model(file)

    if wrap:
        if trans_configs is None:
            # load the undefended model by default
            trans_configs = {
                "type": "clean",
                "subtype": "",
                "id": 0,
                "description": "clean"
            }
        model = WeakDefense(model=model, trans_configs=trans_configs, use_logits=use_logits)
    else:
        if use_logits:
            model = _convert2logits(model)

    return model


def _convert2logits(model):
    return Model(inputs=model.input,
                 outputs=model.get_layer(model.layers[-2].name).output)

