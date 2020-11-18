# Task 1. Generate Adversarial Examples in Zero-Knowledge Model
* Create for the task: 40%
* Bonus: 5% per new attack, at most 10%.

Check ``Section III.D`` in the ``ATHENA`` paper for generating adversarial examples in the context of the zero-knowledge model.

We only consider white-box attacks in this task.

### General process
1. Generate adversarial examples based on the undefended model.
2. Repeat step 1 to generate multiple variants of adversarial examples using various attacks.
3. Evaluate the generated adversarial examples on the undefended model, the vanilla ATHENA, and PGD-ADT model.
4. Perform necessary analysis.
5. Report your work which should includes (but not least).
    1. Introduce your task concisely.
    2. Introduce the approaches (in this case, attacks) you used in this assignment. For example, ``Section II Background and Definitions`` in the ``ATHENA`` paper.
    3. Experimental settings. For example, for an attacker's task, report the attack configurations (the attack method's arguments, etc.), the successful rate of the generated adversarial examples (or the models' error rate against the generated adversarial examples), and the like; for a defender's task, report the defense configurations, the effectiveness of the built defenses against the benign samples and adversarial examples. Check for the individual task for more details.
    4. Empirical results and analysis. Provide necessary descriptions about the results, your observations, and insights.
    5. Contribution of individual team member.
    6. Citation. Cite all related works. For example, the original paper that proposed the attacks you used in this task.
    
### Notes regarding the report
* Do not simply post the logs of your experiment.
* Present your empirical results and analysis properly. Provide necessary texts for others to understand your tables and figures. For simplicity, you can provide the observations and insights as bullets. You are appreciated if you provide descriptions in short paragraphs.
* You can refer to the ``Fig. 32`` in the ``ATHENA`` paper for adversarial parameter tuning. Experimental setting and discussion regarding attacking in the zero-knowledge model is in ``Section III.D``.
* Write the report in your own words.

### Submission
Each team should submit **all materials** that enable an independent group to replicate the results, which includes but not least:
* Scripts.
* Experiment results.
* Report. We prefer report in a Jupyter notebook, but you can also provide a PDF version.

**You can find detailed submission requirement in the ``master`` branch.**

### Grade
* Credit for the task: same credit for the team members that (1) contribute (roughly) equally to the task (2) with comparable quality. If any member contributes significantly less than others, he or she will receive 5%-10% fewer scores than others. If the quality of some part is significantly worse than others, the owner will receive 5%-10% fewer scores than others.
* Credit for bonus: the major contributor(s) will receive the highest score, others will receive ~5% less.  