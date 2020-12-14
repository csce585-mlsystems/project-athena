# Task 2 --- Team-Epsilon

Thank you Team-Epsilon for you work!

----------
### Feedback to the refinement
Address most comments.

1. You should not copy and paste from the project requirement. Write the report in your own words concisely.
2. The weak defenses in the ensembles used in Task 1 and Task 2 are different, and the adversarial settings in the two tasks are different, so related conclusions may not hold.
-----------
### Feedback to the initial submission
1. Good
    1. Visualize the results in figures.
    2. Introduction to ``FGSM``, ``PGD``, and ``EOT``.
    3. Provide the reason of doing experiment on smaller scale sample by approximating the computational cost. Great job!
    4. Experimental settings are clear.
2. Other Comments
    1. Write the introduction to the task briefly **in your own words**. Do not copy and paste the long paragraphs from the requirement.
    2. Missing the introduction (and citation) to ``TQDM`` --- the module/technique to approximate the execution time.
    3. It is better to leave the scripts in a separate file(s). List the paths (locations) to all relevant files to this task, such as the json files for configurations, the python files (or Jupyter notebooks) for scripts (implemented or modified by you), files for results, location for generated AEs, etc.
    4. Experimental setting. What are the weak defenses in the target ensemble --- the ensemble you used to generated the AEs? 
    5. Because the main purpose is to evaluate the robustness of various models, it is better to compare various models in the same figure --- easier to tell which model is more robust against what attack variants. If there are too many variants to plot in a single figure, category the AE variants by attacks then distribution types. That is, a figure for ``FGSM`` + ``rotation`` distribution, one for ``FGSM`` + ``translation``, and so on.  
