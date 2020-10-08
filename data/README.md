1. Here are the baseline adversarial examples that were generated in the context of zero\-knowledge threat model. The targeted model is the undefended model in the Vanilla Athena (models/cnn/model\-mnist\-cnn\-clean.h5).

2. Baseline adversarial examples were generated using various attacks. For each attack, 5 variants were crafted by injecting perturbations with various magnitudes into an input.

3. Each ".npy" file consists of 10K adversarial exmaples from the MNSIT test data, with corresponding benign samples in "test\_BS\-mnist\-clean.npy" and oracle labels in "test\_Label\-mnist\-clean.npy".

4. A file of adversarial examples was named in the pattern of "test\_AE\-\<dataset\>\-\<model_type>\-\<targeted\_model\>\-\<attack\>\_\<attack\_parameters\>.npy", where dataset is "mnist", model_type is "cnn", and targeted_model is "clean" in this project. The "attack" is one of fgsm, cw (l2\-norm), bim (l2\- and linf\-norms), jsma, mim, one\-pixel, pgd, and deepfool.
