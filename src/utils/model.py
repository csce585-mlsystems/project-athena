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


def load_pool(trans_configs, model_configs, use_logits=False, wrapper=None):
    pool = {}
    trans_list = {}

    num_trans = trans_configs.get("num_transformations")
    for i in range(num_trans):
        key = "configs{}".format(i)
        trans = trans_configs.get(key).get("description")

        model_file = model_configs.get("wd_prefix") + trans + model_configs.get("wd_postfix")
        model_file = os.path.join(model_configs.get("dir"), model_file)

        wd = load_lenet(model_file, use_logits=use_logits, wrapper=wrapper)
        pool[trans_configs.get(key).get("id")] = wd
        trans_list[trans_configs.get(key).get("id")] = trans_configs.get(key).get("description")

    print('>>> Loaded {} models.'.format(len(pool.keys())))
    return pool, trans_list


def load_lenet(file, use_logits=False, wrapper=None, wrapper_configs=None):
    print('>>> Loading model [{}]...'.format(file))
    with CustomObjectScope({"GlorotUniform": glorot_uniform()}):
        model = load_model(file)

    if wrapper is None:
        if use_logits:
            model = _convert2logits(model)
    else:
        if wrapper_configs is None:
            raise ValueError("wrapper_configs cannot be none for a wrapper.")
        model = wrapper(model, wrapper_configs)

    return model


def _convert2logits(model):
    return Model(inputs=model.input,
                 outputs=model.get_layer(model.layers[-2].name).output)

