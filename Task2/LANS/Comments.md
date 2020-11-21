# Task 2 --- Team-LANS

Thank you Team-LANS for you work!

Feedback
1. Good
    1. Experiment steps and settings are clear.
    2. Introduction to attacks ``FGSM`` and ``PGD``.
    3. Observations and discussions to the results.
    4. Citations.
2. Other comments
    1. List the paths (locations) to all relevant files to this task, such as the json files for configurations, the python files (or Jupyter notebooks) for scripts (implemented or modified by you), files for results, location for generated AEs, etc.
    2. Improper connection between task 1 and task 2 by simply putting the evaluation results together, since individual models in the figure are evaluated on different AEs. If you want to show how the ``EOT`` affects the effectiveness of the generated ``FGSM``(or ``PGD``) AEs, the proper design is (1) for each ``$\epsilon$`` value, generate AE variants with and without ``EOT`` (2) evaluate models (UM, ensemble(s), PGD-ADT model, etc.) on the AEs generated in step (1). (3) Analyze and visualize the results.   