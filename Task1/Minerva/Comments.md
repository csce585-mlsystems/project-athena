# Task 1 --- Team-Minerva

Thank you Team-Minerva for you work!

Feedback
1. Good
    1. Introduce the task.
    2. Experimental settings are clear.
    3. Experiment process are clear.
    4. Discussion regarding the results.
    5. Attempt to measure the effectiveness of various attacks.
2. Other comments
    1. It is better to leave the scripts in a separate file(s). List the paths (locations) to all relevant files to this task, such as the json files for configurations, the python files (or Jupyter notebooks) for scripts (implemented or modified by you), files for results, location for generated AEs, etc.
    2. Thank you for comparing the AEs from different aspects. However, it brings confusions to compare ``BIM``/``PGD`` vs ``CW`` by fixing ``$\epsilon$``. In this case, you generate ``CW`` AEs by tuning other parameters, however, not tuning ``BIM``/``PGD``. Therefore, the conclusion that ``by fixing the epsilon value, CW  is the most effective attack`` is not proper. The effectiveness of individual attacks are controlled by various set of parameters, we may need a general metrics to measure the effectiveness of attacks, which is a difficult topic requires solid background in math and machine learning, so I would suggest only comparing the effectiveness of models by attack methods in this task. For example, ``CW`` (with various ``$\epsilon$``) vs models, etc..
    3. Bar charts may be a better choice to visualize the experiment results. 
