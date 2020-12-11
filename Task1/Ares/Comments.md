## Task 1 -- Team Ares

Thanks Team-Ares for your work!

---------
### Feedback to the refinement
Comments have been address except those regarding ``JSMA`` and ``PGD``.


---------
### Feedback to initial submission
1. Good
    1. The report for ``BIM`` attack.
    2. Experimental settings are clear.
    3. Provided brief description/observations/conclusion for the results.
2. Other comments
    1. Missing the brief introduction to the attacks you used in task 1. For example, what is ``BIM`` and how it works.
    2. **``BIM ($\epsilon=0.1$)`` attack**. The adversary converges at ``maxiter=70``. As we can see that the error rates of the evaluated models won't change as we continue increasing the ``maxiter``. So, a better strategy is to select combinations of ``2-3`` different ``$\epsilon$``s and ``2-3`` different ``maxiter``. For example, ``($\epsilon$: 0.1, maxiter: 50)``, ``($\epsilon$: 0.1, maxiter: 100)``, ``($\epsilon$: 0.75, maxiter: 50)``, ``($\epsilon$: 0.75, maxiter: 100)``, etc. An ``$\epsilon$`` of ``0.1`` is very small (for this attack), as we can see that the perturbations in the AEs are barely noticed. If you try a larger ``$\epsilon$``, you will see noisier AEs.
    3. **``CW`` attacks**. The sample size is too small --- only contains ``10`` samples, therefore, the evaluation results cannot properly reflect the effectiveness of the attack (and defense). For example, if we generate AE for a single sample, then you will get an error rate of either ``100%`` (the attack is very strong and the defense is weak) or ``0%`` (the attack does not work and the defense is very strong). For the ``l2``-norm variant, the default setting for ``maxiter``, which is ``10``, is a little bit small for the attack to converge. You can try a bigger one. For ``l-infinity``-norm variant, the ``$\epsilon$`` of ``0.3`` may be too large. If you plot some sample AEs as you did for ``BIM``, you might see some messy images that are easily detected by human.
    4. **``JSMA`` attack**. No experiment results were provided. The predicted shape is ``10`` as there are ``10`` categories (for the ``10`` digits) in ``MNIST`` dataset. We've already known this when we selected this dataset. Try to provide something like ``BIM``.
    5. **``PGD`` attack**. The sample size is too small --- only contains ``10`` samples, therefore, the evaluation results cannot properly reflect the effectiveness of the attack (and defense). For example, if we generate AE for a single sample, then you will get an error rate of either ``100%`` (the attack is very strong and the defense is weak) or ``0%`` (the attack does not work and the defense is very strong). Most of the ``$\epsilon$``s are too large. If you would plot some sample AEs, you may see noisy images.
    6. Missing citations. For example, the works for ``BIM``, ``CW``, ``JSMA``, and ``PGD`` attacks.
    
