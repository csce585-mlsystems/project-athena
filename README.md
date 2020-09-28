# project
This is the course project for CSCE585. Students will build their machine learning systems based on the provided infrastructure --- Athena.

# Overview
This project assignment is a group assignment. Each group of students will design and build an adversarial machine learning system on top of the provided framework (Athena []) then evaluate their work accordingly.  The project will be evaluated on a benchmark dataset MNIST []. This project will focus on supervised machine learning tasks, in which all the training data are labeled. Moreover, we consider only evasion attacks in this project, which happens at the test phase (i.e., the targeted model has been trained and deployed).

Each team will finish three tasks independently --- two adversarial machine learning tasks and a competition task.

# Submission
Each team should submit all materials that enable an independent group to replicate the results, which includes but not least:
Code. Submit the code onto the GitHub repo.

1. The experimental results. For example, for attack tasks, submit the crafted AEs, the logs for experiments, and any necessary results. For defense tasks, submit the built defenses, the logs for experiments, and any necessary results.
2. A simple report. Submit reports in the form of Jupyter notebooks on the GitHub repo.
  2.1 Contribution of each individual member.
  2.2 Approaches implemented. Briefly introduce the approaches you choose and implement to solve the task.
  2.3 Experimental settings. Basically, this includes everything that is needed for an independent group to replicate the results. For example, for an attacker's task, report the attack configurations (the attack method's arguments, etc.), the successful rate of the generated adversarial examples (or the models' error rate against the generated adversarial examples), and the like; for a defender's task, report the defense configurations, the effectiveness of the built defenses against the benign samples and adversarial examples. Check for the individual task for more details.
  2.4 Write the report in your own words instead of copying and pasting from an article or others' work. 
  2.5 Cite all related works.
3. Only one submission is necessary for each team.

# All about teams
1. The class (32 students) will be divided into ten groups; each consists of 3 or 4 students. 
2. One can recruit his/her team members or join a team on piazza.
3. Name your team.
4. Claim for task 2. We have multiple options for task 2 with bonus varying from 10% to 20%. Each option allows limited groups, so each team must claim their task 2 (first come, first served).
5. Ying will use a note on piazza to collect the claims for task 2.

# What are given
1. Source code of Athena framework.
2. 73 CNN models (1 undefended model + 72 weak defenses) and 73 SVM models (1 undefended model + 72 weak defenses) that were trained on MNIST. The vanilla Athena, built on the 72 CNN weak defenses, is the Athena we attack and enhance in this project. The 73 SVM models are only for the "Hybrid Athena" task (an option of Task 2).
3. Adversarial examples that were crafted in the context of zero-knowledge threat model. We will refer to these adversarial examples as the baseline adversarial examples in this probject.
4. Configurations of all weak defenses.
5. Configurations of all baseline adversarial examples.
6. Simple tutorials regarding (1) how to load a model (a weak defense or an ensemble) and evaluate it, (2) how generate adversarial examples in the context of zero-knowledge and white-box threat models.
7. (Maybe) A simple example of reports.

# Task 1 [30% + 5%]
**Generate adversarial examples in the context of the zero-knowledge threat model.**

This task is an essential warm-up task for all groups, aiming to help students get familiar with the Athena framework and necessary background regarding the adversarial machine learning tasks.

In this task, students will generate adversarial examples in the context of the zero-knowledge threat model (Section III.D, Athena paper) using 2 to 3 different attack methods. You can generate the adversarial examples using the attacks provided by Athena or new attacks by extending Athena. For the groups who implement a new attack, we consider 5% of additional points as a bonus. Each group should aim for at most one new attack. 

1. Generate adversarial examples based on the undefended model. That is, the attack's targeted model is the undefended model. 
2. Generate adversarial examples using 2 to 3 different attack methods. For each type of attack, generate a couple of variants. By variants, we mean to tune the attack's parameters that are documented as a part of the code. For example, for FGSM attack, generate adversarial examples with various epsilons (e.g., 0.1, 0.15, 0.2, etc.).
3. Evaluate the generated adversarial examples on the undefended model, the vanilla Athena, and PGD-ADT (all these models will be provided). 
3.1 (Must) Evaluate the adversarial examples in terms of the successful rate.
3.2 (Option) Evaluate the adversarial examples using any proper measure. In this case, introduce the additional measures.
4. Perform necessary analysis if there are any.
5. Report your solution(s), experimental results, and analysis.
5.1 Brief the attacks used to generate adversarial examples.
5.2 Experimental settings for each attack.
5.3 Evaluation results in term of the successful rate of the crafted adversarial examples. 

## The attacks implemented by Athena [30%]:
1. FGSM
2. BIM (l2- and linf- norms)
3. CW (l2- and linf- norms)
4. JSMA
5. PGD
6. MIM
7. One-Pixel (extremely slow, not recommended)
8. Spatial Transform
9. Hop-Skip-Jump
10. ZOO

## Other possible attacks [5%]:
1. Obfuscated Gradient
2. etc.

**Note:** You are encouraged to explore for new attacks not listed. Some good resources are related studies in recent years, NIPS adversarial competitions, and surveys in adversarial machine learning.

# Task 2 [50% + 10 - 20%]
There are multiple options for task 2 with various bonuses. Each team should pick one and only one for the task 2 assignment. Each optional task 2 allows limited groups, so first come, first served. We will post a note on piazza to collect the claims. A random assignment will be assigned by us if any team that does not claim for task 2 assignment before task 1 is due.

## Option 1 [50% + 10%] (<= 3 groups)
**White-box attack the vanilla Athena**

In this task, students aim to generate adversarial examples based on the vanilla Athena in the context of the white-box threat model (Section III.F in Athena paper) and then evaluate the effectiveness of the crafted adversarial examples. Each group should aim to generate the adversarial examples using at most 2 attacks. For each attack, generate around five variants by varying tunable parameters. Evaluate the successful rate of the crafted adversarial examples on the vanilla Athena. Compare the adversarial examples generated in Task 2 with those generated in Task 1 and the baseline adversarial examples provided by us.

### Report:
1. Introduce the approaches that are used in the task.
2. Experimental settings --- the values of the tunable parameters for each variant.
3. Evaluation results and necessary analysis.
4. Contribution of individual team members.
5. Citations to all related works.

### Possible solutions:
1. Optimization-based approach: accumulated loss. Reference: Towards Robust Neural Networks via Random Self-ensemble. Xuanqing Liu, Minhao Cheng, Huan Zhang, Cho-Jui Hsieh. ECCV 2018.
2. Synthesizing adversarial examples. Reference: Synthesizing Robust Adversarial Examples, A. Athalye et al., ICML 2018

**Note:** You are encouraged to explore new approaches not listed.

## Option 2 [50% + 15%/20%] (<= 3 groups)
**Learn a strategy model**

Students aim to build a model in this task, which takes the predictions from weak defenses as the input and produces the final label for the input image. That is, rather than using a fixed ensemble strategy (MV, AVEP, etc.), students train a model to utilize the predictions from weak defenses. Each group should aim to implement one approach. Evaluate your defenses against the benign samples, the adversarial examples generated in Task 1, and the baseline adversarial examples.

### Report:
1. Introduce the approaches that are used in the task.
2. Experimental settings --- the values of the tunable parameters for each variant.
3. Evaluation and necessary analysis.
4. Contribution of individual team members.
5. Citations to all related works.

### Possible solutions:
1. [+15%] A machine learning model f(predictions) = y' that is trained on the training set D = {(predictions, y)}.
2. [+20%] Adaptive Multi-Column Deep Neural Networks with Application to Robust Image Denoising. Forest Agostinelli, Michael R. Anderson, and Honglak Lee. NIPS 2018.
3. [+20%] Knowledge distillation? (TBD. Ying will check if this is feasible.) Distilling the Knowledge in a Neural Network. Geoffrey Hinton, Oriol Vinyals, and Jeff Dean. ICLR 2015.

**Note:** You are encouraged to explore new approaches not listed.

### Option 3 [50% + 15%] (<= 3 groups)
**Probabilistic Athena**

Students aim to build an ensemble from a library of probabilistic models (such as Bayesian Neural Networks) in this task. Each group should aim to build a library of 10 to 20 weak defenses and then build the ensembles from the library. Evaluate your defenses against the benign samples, the adversarial examples generated in Task 1, and the baseline adversarial examples.

### Report:
1. Introduce the approaches that are used in the task.
2. Experimental settings --- the values of the tunable parameters for each variant. 
3. Evaluation of defenses' effectiveness and necessary analysis.
4. Contribution of individual team members.
5. Citations to all related works.

**Note:** You are encouraged to explore new approaches not listed.

### Option 4 [50% + 10%/20%] (<= 3 groups)
**Hybrid Athena**
Students aim to build a hybrid ensemble from a library of diverse types of weak defenses in this task. Students should aim to build a couple of ensemble variants with various sizes.

Two major approaches:
1. [10%] Randomly select n weak defenses from the library for the ensemble.
2. [20%] Select n weak defenses via some search-based approaches. For example,
Greedy search for n weak defenses that gives the maximal/minimal value according to a specific metric (e.g., entropy, ensemble diversity, etc.)
### Report:
1. Introduce the approaches that are used in the task.
2. Experimental settings --- the values of the tunable parameters for each variant.
3. Evaluation of defenses' effectiveness and necessary analysis.
4. Contribution of individual team members.
5. Citations to all related works.

**Note:** You are encouraged to explore new approaches not listed.

# Task 3 [20%]
**Competition task**

Students should aim to seek insights and/or theoretical explanations of why and why not the approach is effective.

Cross evaluation of task 1 and task 2 between all groups will be run by us (or we will provide scripts for students to perform the cross-evaluation). Evaluation results will be provided to the whole class. After the cross-evaluation, each team should aim to perform necessary analysis on the evaluation results and investigate why your approaches are effective (or ineffective) against some approach.

### Report:
1. Introduce the analysis methods that are used in the task.
2. Analysis results and insights. Possible enhancements, future works. etc.
3. Architecture of your machine learning system (for the whole project).
4. Contribution of individual team members.
5. Citations to all related works.
