# Task 1 --- Team-Mars

Thank you Team-Mars for you work!

Feedback
1. Good
    1. Introduce the task.
2. Other comments
    1. It is better to leave the scripts in a separate file(s). List the paths (locations) to all relevant files to this task, such as the json files for configurations, the python files (or Jupyter notebooks) for scripts (implemented or modified by you), files for results, location for generated AEs, etc.
    2. Missing the experimental settings. How you precess to solve this task, what attacks (and configurations) were used, what weak defenses were used to build the ensemble model in this task, etc.
    3. No discussions regarding the results. The trend of the error rates as the ``$\epsilon$`` increases, the performance of the evaluated models, etc. Plotting AEs samples will provide more hints, for example, noisier AEs and even some messy images whose semantic meaning have been changed. Due to the small size of ensemble (it contains only ``3`` weak defenses used for demo), the effectiveness of the ensemble is significantly worse than the baseline defense (``PGD-ADT``). The ensemble model will become more robust as more weak defenses are utilized.
    4. The ``ratio`` of sumsampling has nothing to do with the ``num_of_classes``, they are two **independent** parameters.  
    5. Check the requirement for report for the missing parts. An example for your reference: ``Team-Clutch``'s report.  
