# Task 2 --- Team-Minerva

Thank you Team-Minerva for you work!

Feedback:
1. Good
    1. Great report that contains most required sessions.
    2. Experiment settings are clear.
    3. Results are well-presented. Thanks!
    4. Evaluation on the computational cost. Thanks!
2. To improve
    1. The settings for some attacks are too small. For example, ``$\epsilon$``s for ``BIM-eps0.01``, ``BIM-eps0.05``, ``PGD-eps0.05``, and ``PGD-eps0.075`` are too small. Even the ``UM`` is not fooled by such AEs (Figure 1.3). If you plot some AE samples and corresponding benign samples, you may see that the AEs are barely perturbed.
    2. What is the ``Full Ensemble...`` in ``Figure 1.3``?
    3. In figures ``1.4``, ``1.5``, ``1.6``, and ``1.7``, there are duplicated ``x-axis`` labels (e.g., 3 ``3-17``s), distinguish them. There are some jumps in the curve of ``BIM-eps0.01``, those could be some interesting observations worth further investigate. If you could not finish the investigation, they worth to be highlighted.
    4. Missing discussion regarding the experiment results and analysis.
    5. Leave scripts and experiment logs in corresponding files and list the path such materials in the report.
    6. Provide the list of weak defenses of your hybrid ensemble variants. Leave this in a separate configuration file(s) and list the path to such files in the report.
    7. Missing introduction to the attacks (you can copy those from your ``Task1`` report if you have them in it). 