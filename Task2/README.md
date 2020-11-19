# Task 2. Extension of ATHENA

## Option 1. Optimization-based white-box attack
* Create for the task: 60%.
* Bonus: 10% per new attack, at most 20%.

Check ``Section IV.F`` in the ``ATHENA`` paper for attacking in the context of the white-box model.

### General process
1. Generate adversarial examples based on an ensemble model (the target ensemble).
2. Repeat step 1 to generate multiple variants of adversarial examples using various attacks.
3. Evaluate the generated adversarial examples on the undefended model, the target ensemble, the vanilla ATHENA, and PGD-ADT model.
4. Perform necessary analysis.
5. Report your work which should includes (but not least).
    1. Introduce your task concisely.
    2. Introduce the approaches (in this case, attacks) you used in this assignment. For example, ``Section II Background and Definitions`` in the ``ATHENA`` paper.
    3. Experimental settings. For example, for an attacker's task, report the attack configurations (the attack method's arguments, etc.), the successful rate of the generated adversarial examples (or the models' error rate against the generated adversarial examples), and the like; for a defender's task, report the defense configurations, the effectiveness of the built defenses against the benign samples and adversarial examples. Check for the individual task for more details.
    4. Empirical results and analysis. Provide necessary descriptions about the results, your observations, and insights.
    5. Contribution of individual team member.
    6. Citation. Cite all related works. For example, the original paper that proposed the attacks you used in this task.

**Note**
* Make sure the experimental setting is reasonable that brings some insights. For example, (1) generating multiple AE variants using various attack configuration (as mentioned in the tutorial, you can vary the adversary in many different dimensions, for example, attack parameters, distribution parameters. Please refer to the tutorial for tunable parameters.), and/or (2) generating AEs with various weak defenses accessed by the attacker (for example, the attacker generates AEs based on 10%, 20%, ..., 100% of the weak defenses in the ensemble). Refer to the ATHENA paper (White-box threat model section) for details.
* Consider the computational cost (it is expensive than Task 1), you can generate AEs for a smaller subset (refer to Task1). If you do so, please submit the subset of samples and the corresponding true labels.


## Option 2. Learning-based strategy
* Credit for the task: 60%.
* Bonus: 20%.

### General process
1. Build and train a learning-based model, as an alternative to fixed strategy (MV, AVEP, etc.), which produces the final prediction on the input.
2. Evaluate several baseline AE variants (i.e., the AEs we provided under the ``data`` folder) on the ``Undefended Model``, the ``ensemble using the learning-based strategy``, the ``ensemble using a fixed strategy (MV or AVEP)``, and the ``PGD-ADT`` model.
3. Perform necessary analysis.
4. Report (check ``Task1`` or ``Option 1`` for details)

## Option 4. Hybrid ATHENA
* Credit for the task: 60%.
* Bonus: 10% for random synthesis of ensemble; 20% for learning-based or search-based synthesis of ensemble.

### General process
1. Load all weak defenses into a candidate pool.
2. Select some weak defenses and build a hybrid ensemble upon them.
3. Evaluate the hybrid ensemble on some baseline AEs (i.e., the AEs we provided under the ``data`` folder).
4. Repeat steps 2 and 3 to build and evaluate several hybrid ensemble variants.
5. Perform necessary analysis.
6. Report (check ``Task1`` or ``Option 1`` for details)

----
## Notes regarding the report
* Do not simply post the logs of your experiment.* Present your empirical results and analysis properly. Provide necessary texts for others to understand your tables and figures. For simplicity, you can provide the observations and insights as bullets. You are appreciated if you provide descriptions in short paragraphs.
* Write the report in your own words.

## Submission
Each team should submit **all materials** that enable an independent group to replicate the results, which includes but not least:
* Scripts.
* Experiment results.
* Report. We prefer report in a Jupyter notebook, but you can also provide a PDF version.

**You can find detailed submission requirement in the ``master`` branch.**

## Grade
* Credit for the task: same credit for the team members that (1) contribute (roughly) equally to the task (2) with comparable quality. If any member contributes significantly less than others, he or she will receive 5%-10% fewer scores than others. If the quality of some part is significantly worse than others, the owner will receive 5%-10% fewer scores than others.
* Credit for bonus: the major contributor(s) will receive the highest score, others will receive ~5% less.  

------
| Team | Option |
|:----:|:------:|
|Ares|Option 2|
|Clutch|Option 1|
|Epsilon|Option 1|
|Horus|Option 1|
|JiR|Option 2|
|LANS|Option 1|
|Mars|Option 2|
|Minerva|Option 4|
|doubleE|Option 1|