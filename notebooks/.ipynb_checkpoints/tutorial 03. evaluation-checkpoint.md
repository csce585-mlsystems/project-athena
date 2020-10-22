# Evaluating models on generated adversarial examples.

If you would like to generate adversarial examples for a subset.
## Sample a random subset from the benign sample.
A function ``subsampling(data, labels, num_classes, ...)`` is provided to sample a random subset from the ``data`` and the corresponding ``labels``.

Check the example in script ``tutorials.subsamples.py``

Once you generated your own subsamples, maintain them in the json file (similar to ``data-mnist.json``) and use these new dataset for your experiment.
**Since we are subsampling benign samples, your ``bs_file`` will be the subsampled data and ``label_file`` will be the subsampled labels.**

## Generate and save the adversarial examples
Maintain the adversarial settings in ``attack-zk-mnist.json``, by adding new ``configs_x`` (and update the ``num_attacks``). You can refer to ``attacks.attack.py`` for the tunable parameters for each attack.

e.g., a json file to generate adversarial examples using FGSM and PGD attack. (has been updated in ``configs/demo/attack-zk-mnist.json``)

> { \
>     "num_attacks": 2, \
>      "configs0": { \
>          "attack": "fgsm", \
>          "description": "FGSM_eps0.25", \
>          "eps": 0.25 \
>      }, \
>      "configs1": { \
>         "attack": "pgd", \
>         "description": "PGD_eps0.25", \
>         "eps": 0.25 \
>      } \
>} 

After your adversarial examples have been generated, maintain them in a json file (similar to ``data-mnist.json``) and evaluate them.

## Evaluate the generated adversarial examples.
An example in ``tutorial.eval_model.py`` presents the full process of evaluating the undefended model (the targeted model in task 1), an AVEP ensemble, and the PGD-ADT model on an AE variant.

In the tutorial, I use ``configs/demo/athena-mnist.json`` to maintain the weak defenses in the ensemble, which is not the configuration for the full pool in Athena paper. The full pool is maintained in file ``configs/experiment/athena-mnist.json``.

**Please update the json files that are used for your experiments if you maintain your data in a different file.**
