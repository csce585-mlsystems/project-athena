"""
Implement white-box attacks on top of IBM ART.
@author: Ying Meng (y(dot)meng201011(at)gmail(dot)com)
"""

import numpy as np
import torch

from art.attacks.evasion.fast_gradient import FastGradientMethod
from art.attacks.evasion.carlini import CarliniL2Method, CarliniLInfMethod
from art.attacks.evasion.projected_gradient_descent import ProjectedGradientDescent
from art.attacks.evasion.deepfool import DeepFool
from art.attacks.evasion.saliency_map import SaliencyMapMethod
from art.attacks.evasion.iterative_method import BasicIterativeMethod
from art.attacks.evasion.spatial_transformation import SpatialTransformation
from art.attacks.evasion.hop_skip_jump import HopSkipJump
from art.attacks.evasion.zoo import ZooAttack

from attacks.utils import WHITEBOX_ATTACK as ATTACK


def generate(model, data_loader, attack_args, device=None):
    if device is None:
        device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

    images, labels = data_loader
    attack = attack_args.get('attack').lower()

    if attack == ATTACK.FGSM.value:
        return _fgsm(model, images, labels, attack_args)
    elif attack == ATTACK.CW.value:
        return _cw(model, images, labels, attack_args)
    elif attack == ATTACK.PGD.value:
        return _pgd(model, images, labels, attack_args)
    elif attack == ATTACK.BIM.value:
        return _bim(model, images, labels, attack_args)
    elif attack == ATTACK.JSMA.value:
        return _jsma(model, images, labels, attack_args)
    elif attack == ATTACK.DF.value:
        return _df(model, images, labels, attack_args)
    elif attack == ATTACK.MIM.value:
        return _mim(model, images, labels, attack_args)
    elif attack == ATTACK.OP.value:
        return _op(model, images, labels, attack_args)
    elif attack == ATTACK.HOP_SKIP_JUMP.value:
        raise _hop_skip_jump(model, images, labels, attack_args)
    elif attack == ATTACK.SPATIAL_TRANS.value:
        return _spatial(model, images, labels, attack_args)
    elif attack == ATTACK.ZOO.value:
        return _zoo(model, images, labels, attack_args)
    else:
        raise ValueError('{} is not supported.'.format(attack))


def _fgsm(model, data, labels, attack_args):
    print('>>> Generating FGSM examples.')
    eps = attack_args.get('eps', 0.3)

    targeted = attack_args.get('targeted', False)
    num_random_init = attack_args.get('num_random_init', 0)
    minimal = attack_args.get('minimal', False)

    attacker = FastGradientMethod(model, eps=eps, eps_step=eps, targeted=targeted,
                                  num_random_init=num_random_init, minimal=minimal)
    return attacker.generate(data, labels)


def _cw(model, data, labels, attack_args):
    norm = attack_args.get('norm').lower()

    lr = attack_args.get('lr')
    max_iter = attack_args.get('max_iter', 10)

    # use default values for the following arguments
    confidence = attack_args.get('confidence', 0.0)
    targeted = attack_args.get('targeted', False)
    init_const = attack_args.get('init_const', 0.01)
    max_halving = attack_args.get('max_halving', 5)
    max_doubling = attack_args.get('max_doubling', 5)

    if norm == 'l2':
        print('>>> Generating CW_l2 examples.')
        binary_search_steps = attack_args.get('binary_search_steps', 10)

        attacker = CarliniL2Method(classifier=model, confidence=confidence, targeted=targeted, learning_rate=lr,
                                   binary_search_steps=binary_search_steps, max_iter=max_iter,
                                   initial_const=init_const, max_halving=max_halving,
                                   max_doubling=max_doubling)

    elif norm == 'linf':
        print('>>> Generating CW_linf examples.')
        eps = attack_args.get('eps', 0.3)
        attacker = CarliniLInfMethod(classifier=model, confidence=confidence, targeted=targeted, learning_rate=lr,
                                     max_iter=max_iter, max_halving=max_halving, max_doubling=max_doubling, eps=eps)
    else:
        raise ValueError('Support `l2` and `linf` norms. But found {}'.format(norm))

    return attacker.generate(data, labels)


def _pgd(model, data, labels, attack_args):
    eps = attack_args.get('eps', 0.3)
    eps_step = attack_args.get('eps_step', eps/10.)
    max_iter = attack_args.get('max_iter', 10)

    # default
    norm = _get_norm_value(attack_args.get('norm', 'linf'))
    targeted = attack_args.get('targeted', False)
    num_random_init = attack_args.get('num_random_init', 0)
    random_eps = attack_args.get('random_eps', False)

    attacker = ProjectedGradientDescent(classifier=model, norm=norm, eps=eps, eps_step=eps_step,
                                        max_iter=max_iter, targeted=targeted,
                                        num_random_init=num_random_init, random_eps=random_eps)
    return attacker.generate(data, labels)


def _bim(model, data, labels, attack_args):
    eps = attack_args.get('eps', 0.3)
    eps_step = attack_args.get('eps_step', eps/10.)
    max_iter = attack_args.get('max_iter', 100)

    targeted = attack_args.get('targeted', False)
    attacker = BasicIterativeMethod(classifier=model, eps=eps, eps_step=eps_step,
                                    max_iter=max_iter, targeted=targeted)
    return attacker.generate(data, labels)


def _jsma(model, data, labels, attack_args):
    theta = attack_args.get('theta', 0.15)
    gamma = attack_args.get('gamma', 0.5)

    attacker = SaliencyMapMethod(classifier=model, theta=theta, gamma=gamma)
    return attacker.generate(data, labels)


def _df(model, data, labels, attack_args):
    max_iter = attack_args.get('max_iter', 100)
    eps = attack_args.get('eps', 0.01)
    nb_grads = attack_args.get('nb_grads', 10)

    attacker = DeepFool(classifier=model, max_iter=max_iter, epsilon=eps, nb_grads=nb_grads)
    return attacker.generate(data, labels)


def _mim(model, data, labels, attack_args):
    raise NotImplementedError


def _op(model, data, labels, attack_args):
    raise NotImplementedError


def _spatial(model, data, labels, attack_args):
    max_translation = attack_args.get('max_translation', 0.2)
    num_translations = attack_args.get('num_translations', 1)
    max_rotation = attack_args.get('max_rotation', 10)
    num_rotations = attack_args.get('num_rotations', 1)

    attacker = SpatialTransformation(classifier=model,
                                     max_translation=max_translation, num_translations=num_translations,
                                     max_rotation=max_rotation, num_rotations=num_rotations)
    return attacker.generate(data, labels)


def _hop_skip_jump(model, data, labels, attack_args):
    norm = _get_norm_value(attack_args.get('norm', 'l2'))
    max_iter = attack_args.get('max_iter', 50)
    max_eval = attack_args.get('max_eval', 10000)
    init_eval = attack_args.get('init_eval', 100)
    init_size = attack_args.get('init_size', 100)

    targeted = attack_args.get('targeted', False)
    attacker = HopSkipJump(classifier=model, targeted=targeted, norm=norm,
                           max_iter=max_iter, max_eval=max_eval,
                           init_eval=init_eval, init_size=init_size)

    return attacker.generate(data, labels)


def _zoo(model, data, labels, attack_args):
    lr = attack_args.get('learning_rate', 0.01)
    max_iter = attack_args.get('max_iter', 10)
    binary_search_steps = attack_args.get('binary_search_steps', 1)

    confidence = attack_args.get('confidence', 0.0)
    targeted = attack_args.get('targeted', False)
    init_const = attack_args.get('init_const', 1e-3)
    abort_early = attack_args.get('abort_early', True)
    use_resize = attack_args.get('use_resize', True)
    use_importance = attack_args.get('use_importance', True)
    nb_parallel = attack_args.get('nb_parallel', 128)
    variable_h = attack_args.get('variable_h', 1e-4)

    attacker = ZooAttack(classifier=model, confidence=confidence, targeted=targeted,
                         learning_rate=lr, max_iter=max_iter, binary_search_steps=binary_search_steps,
                         initial_const=init_const, abort_early=abort_early, use_resize=use_resize,
                         use_importance=use_importance, nb_parallel=nb_parallel, variable_h=variable_h)

    return attacker.generate(data, labels)


def _get_norm_value(norm):
    norm = norm.lower()
    if norm == 'linf':
        value = np.inf
    elif norm == 'l2':
        value = 2
    else:
        raise ValueError('Support `l2` and `linf` norms. But found {}.'.format(norm))

    return value
