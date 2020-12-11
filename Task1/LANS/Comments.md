# Task 1 --- Team-LANS

Thank you Team-LANS for you work!

-----------------
### Feedback to the refinement
Great improvement, thanks!

-------
### Feedback to the initial submission (to ``Report.jpynb``)
1. Good
    1. Experiment steps are clear.
    2. Introduction to attacks.
    3. Observations and discussions to the results.
2. Other comments
    1. List the paths (locations) to all relevant files to this task, such as the json files for configurations, the python files (or Jupyter notebooks) for scripts (implemented or modified by you), files for results, location for generated AEs, etc.
    2. The experimental settings. How you precess to solve this task, what attacks (and configurations) were used, what weak defenses were used to build the ensemble model in this task, etc.
    3. Sample AEs cannot display properly (check the path to the images).
    4. With small ``$\epsilon$`` the attack will generate weak AEs. For example, with ``$\epsilon`` of ``0.01`` (or ``0.05``), ``FGSM`` is unlikely to launch a successful attack --- only ``0.6%`` (``6%``) of the generated AEs can fool the undefended model.
    5. Due to the small size of ensemble (it contains only ``3`` weak defenses used for demo), the effectiveness of the ensemble is significantly worse than the baseline defense (``PGD-ADT``). The ensemble model will become more robust as more weak defenses are utilized.

    
