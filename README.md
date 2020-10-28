# Project Athena
This is the course project for [CSCE585](https://pooyanjamshidi.github.io/mls/). Students will build their machine learning systems based on the provided infrastructure --- [Athena](https://softsys4ai.github.io/athena/).

# Overview
This project assignment is a group assignment. Each group of students will design and build an adversarial machine learning system on top of the provided framework ([Athena](https://softsys4ai.github.io/athena/)) then evaluate their work accordingly.  The project will be evaluated on a benchmark dataset [MNIST](http://yann.lecun.com/exdb/mnist/). This project will focus on supervised machine learning tasks, in which all the training data are labeled. Moreover, we consider only evasion attacks in this project, which happens at the test phase (i.e., the targeted model has been trained and deployed).

Each team should finish three tasks independently --- two core adversarial machine learning tasks and a competition task.

# Submission
Each team should submit all materials that enable an independent group to replicate the results, which includes but not least:

* **Code**. Submit the code in your project GitHub repo. In order to do that, the team leader should first create a project GitHub repo for your team by forking the class project GitHub repo then add all your team members to the team repo. All scripts should be maintained in the `src` folder properly. 
* The **experimental results**. For example, for attack tasks, submit the crafted AEs, the logs for experiments, and any necessary results. For defense tasks, submit the built defenses, the logs for experiments, and any necessary results.
* **Jupyter notebooks**. Submit reports in the form of Jupyter notebooks on the GitHub repo.
  * *Contribution* of each individual member.
  * *Approaches* implemented. Briefly introduce the approaches you choose and implement to solve the task.
  * *Experimental settings*. Basically, this includes everything that is needed for an independent group to replicate the results. For example, for an attacker's task, report the attack configurations (the attack method's arguments, etc.), the successful rate of the generated adversarial examples (or the models' error rate against the generated adversarial examples), and the like; for a defender's task, report the defense configurations, the effectiveness of the built defenses against the benign samples and adversarial examples. Check for the individual task for more details.
  * Write the report in *your own words* instead of copying and pasting from an article or others' work. Make sure you emphesize on important findings and intuitions behind any design choice you made.
  * *Cite* all related works.
* **Only one submission** is necessary for each team. 
* **Organize the submissions** The submissions for tasks (except scripts, which should be in `src`) should be organized as fowllows:
  * In your project root, create folders `Task1`, `Task1`, and `Task3` for your task1, task2, task3 respectively.
  * In each of the task folder, create (i) a `data` folder for all the adversarial examples generated for the task assignment; (ii) a `models` folder for all the new models you created and trained for the task assignment; (iii) a `results` folder for experiment outputs (if there are any).
  * The report document for the task should locate at the root of the task folder.
  * Here is an example:
  ```
  Task1
    |-- data
    |     |-- AE-FGSM_eps0.3.npy
    |     |-- AE-PGD_eps0.45.npy
    |     |-- BS.npy
    |     |-- Labels.npy
    |-- models
    |     |-- BayesianNN-MNIST-clean.npy
    |     |-- BayesianNN-MNIST-rotate_90.npy
    |-- results
    |     |-- evaluation-error_rate-AE-FGSM_eps0.3.csv
    |-- report_task1.ipynb
  ```
* **IMPORTANT**: Please make sure you tag the commit that delivers each task, e.g.: `git tag -a task1 -m "Team XYZ Task 1"`. Once you tag your commit, please make sure you let us know where your repository leaves via the associated turn in issue in the [project-athena](https://github.com/csce585-mlsystems/project-athena/). E.g., [Task 1](#23).

# All about teams
* The class (32 students) will be divided into ten groups; each consists of 3 or 4 students.
* One can recruit her/his team members via GitHub issues or via Piazza.
* Name your team in the associated GitHub issue designated for teams.
* Claim for task 2. We have multiple options for task 2 with bonus varying from 10% to 20%. Each option allows limited groups, so each team must claim their task 2 (first come, first served).
* We will use [this note](https://piazza.com/class/ke221xlfhpq783?cid=25) on piazza to collect the claims for task 2.
* We also allow for **external teams** or **external individuals** who are not students in the CSCE 585 class.

# What are given
* Source code of Athena framework. 
* 73 CNN models (1 undefended model + 72 weak defenses) and 73 SVM models (1 undefended model + 72 weak defenses) that were trained on MNIST. The vanilla version of Athena, built on the 72 CNN weak defenses, is the Athena we attack and enhance in this project. The 73 SVM models are only for the "Hybrid Athena" task (an option of Task 2).
* Adversarial examples that were crafted in the context of zero-knowledge threat model. We will refer to these adversarial examples as the baseline adversarial examples in this probject. 
* Configurations of all weak defenses. 
* Configurations of all baseline adversarial examples. 
* Simple tutorials regarding (1) how to load a model (a weak defense or an ensemble) and evaluate it, (2) how generate adversarial examples in the context of zero-knowledge and white-box threat models.
* (Maybe) A simple example of reports. 


# Task 1. Generate adversarial examples
* Objective: Generate adversarial examples in the context of the zero-knowledge threat model.
* Due: 11:59:59 PM, Oct. 25
* Credits: 30% + bonus (5%)

This task is an essential warm-up task for all groups, aiming to help students get familiar with the Athena framework and necessary background regarding the adversarial machine learning tasks.

In this task, students will generate adversarial examples in the context of the zero-knowledge threat model (Section III.D, Athena paper) using 2 to 3 different attack methods. You can generate the adversarial examples using the attacks provided by Athena or new attacks by extending Athena. For the groups who implement a new attack, we consider 5% of additional points as a bonus. Each group should aim for at most one new attack. 

* Generate adversarial examples based on the undefended model. That is, the attack's targeted model is the undefended model. 
* Generate adversarial examples using 2 to 3 different attack methods. For each type of attack, generate a couple of variants. By variants, we mean to tune the attack's parameters that are documented as a part of the code. For example, for FGSM attack, generate adversarial examples with various epsilons (e.g., 0.1, 0.15, 0.2, etc.).
* Evaluate the generated adversarial examples on the undefended model, the vanilla Athena, and [PGD-ADT](https://arxiv.org/pdf/1706.06083.pdf) (all these models will be provided). 
  * (Must-Have) Evaluate the adversarial examples in terms of the successful rate.
  * (Optional) Evaluate the adversarial examples using any proper measure. In this case, introduce the additional measures.
* Perform necessary analysis if there are any.
* Report your solution(s), experimental results, and analysis.
  * Brief the attacks used to generate adversarial examples.
  * Experimental settings for each attack.
  * Evaluation results in term of the successful rate of the crafted adversarial examples. 

## The attacks implemented by Athena [30%]:
1. [FGSM](https://arxiv.org/abs/1412.6572)
2. [BIM (l2- and linf- norms)](https://arxiv.org/abs/1607.02533)
3. [CW (l2- and linf- norms)](https://ieeexplore.ieee.org/abstract/document/7958570)
4. [JSMA](https://ieeexplore.ieee.org/abstract/document/7467366)
5. [PGD](https://arxiv.org/pdf/1706.06083.pdf)
6. [MIM](https://openaccess.thecvf.com/content_cvpr_2018/papers/Dong_Boosting_Adversarial_Attacks_CVPR_2018_paper.pdf)
7. [DeepFool](https://www.cv-foundation.org/openaccess/content_cvpr_2016/papers/Moosavi-Dezfooli_DeepFool_A_Simple_CVPR_2016_paper.pdf)
8. [One-Pixel](https://arxiv.org/pdf/1710.08864.pdf) (black-box attack, not suitable for this task)
9. [Spatially Transformed Attack](https://arxiv.org/abs/1801.02612)
10. [Hop-Skip-Jump](https://arxiv.org/abs/1904.02144) (black-box attack, not suitable for this task)
11. [ZOO](https://arxiv.org/abs/1708.03999)

## Other possible attacks [5%]:
1. [Obfuscated Gradient](https://arxiv.org/pdf/1802.00420.pdf)
2. [DDA (Distributionally Adversarial Attack)](https://www.aaai.org/ojs/index.php/AAAI/article/view/4061)
3. [ENA (Elastic-net Attack)](https://arxiv.org/abs/1709.04114)
4. [GAN-based Attacks](https://arxiv.org/abs/1801.02610)
3. etc.

**Note:** You are encouraged to explore for new attacks not listed. Some good resources are related studies in recent years, NIPS adversarial competitions, and surveys in adversarial machine learning.

# Task 2. Extension of ATHENA
* Due: 11:59:59 PM, Nov. 15
* Credits: 50% + bonus (10% -- 20%)

There are multiple options for task 2 with various bonuses. Each team should pick one and only one for the task 2 assignment. Each optional task 2 allows limited groups, so first come, first served. We will post a note on piazza to collect the claims. A random assignment will be assigned by us if any team that does not claim for task 2 assignment before task 1 is due. Claim your task 2 [here](https://piazza.com/class/ke221xlfhpq783?cid=24).

## Option 1. Optimazation-based white-box attack
* Task: Generate adversarial examples for the Vanilla ATHENA, using optimaztion-based white-box attack.
* Number of groups: not limited
* Bonus: 10%

In this task, students aim to generate adversarial examples based on the vanilla Athena in the context of the white-box threat model (Section III.F in Athena paper) and then evaluate the effectiveness of the crafted adversarial examples. Each group should aim to generate the adversarial examples using at most 2 attacks. For each attack, generate around 5 variants by varying tunable parameters. Evaluate the successful rate of the crafted adversarial examples on the vanilla Athena. Compare the adversarial examples generated in Task 2 with those generated in Task 1 and the baseline adversarial examples provided by us.

### Report:
1. Introduce the approaches that are used in the task.
2. Experimental settings --- the values of the tunable parameters for each variant.
3. Evaluation results and necessary analysis.
4. Contribution of individual team members.
5. Citations to all related works.

### Possible solutions (already implemented in ATHENA):
```
1. Xuanqing Liu, Minhao Cheng, Huan Zhang, Cho-Jui Hsieh. Towards Robust Neural Networks via Random Self-ensemble. ECCV 2018.
2. Anish Athalye, Logan Engstrom, Andrew Ilyas, Kevin Kwok. Synthesizing Robust Adversarial Examples. ICML 2018
```

**Note:** You are encouraged to explore new approaches not listed.

## Option 2. Learning-based strategy
* Task: Build a learning-based strategy.
* Number of groups: no more than 3 groups.
* Bonus: 20%

Students aim to build a model in this task, which takes the predictions from weak defenses as the input and produces the final label for the input image. That is, rather than using a fixed ensemble strategy (MV, AVEP, etc.), students train a model to utilize the predictions from weak defenses. Each group should aim to implement one approach. Evaluate your defenses against the benign samples, the adversarial examples generated in Task 1, and the baseline adversarial examples.

### Report:
1. Introduce the approaches that are used in the task.
2. Experimental settings --- the values of the tunable parameters for each variant.
3. Evaluation and necessary analysis.
4. Contribution of individual team members.
5. Citations to all related works.

### Possible solutions:
```
1. [+20%] Forest Agostinelli, Michael R. Anderson, and Honglak Lee. Adaptive Multi-Column Deep Neural Networks with Application to Robust Image Denoising. NIPS 2018.
2. [+20%] Geoffrey Hinton, Oriol Vinyals, and Jeff Dean. Distilling the Knowledge in a Neural Network. ICLR 2015.
```

**Note:** You are encouraged to explore new approaches not listed.

### Option 3. Probabilistic ATHENA
* Task: Build a probabilistic ATHENA
* Number of groups: no more than 3 groups
* Bonus: 15%

Students aim to build an ensemble from a library of probabilistic models (such as `Bayesian Neural Networks`) in this task. Each group should aim to build a library of 5 to 20 weak defenses and then build the ensembles from the library. Evaluate your defenses against the benign samples, the adversarial examples generated in Task 1, and the baseline adversarial examples.

### Report:
1. Introduce the approaches that are used in the task.
2. Experimental settings --- the values of the tunable parameters for each variant. 
3. Evaluation of defenses' effectiveness and necessary analysis.
4. Contribution of individual team members.
5. Citations to all related works.

**Note:** You are encouraged to explore new approaches not listed.

### Option 4. Hybrid ATHENA
* Task: Build a hybrid ATHENA
* Number of groups: no more than 3 groups
* Bonus: 10% -- 20%

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

# Task 3. Competition task
* Task: Competition
* Due: 11:59:59 PM, Nov. 30
* Bonus: 20%

Students should aim to seek insights and/or theoretical explanations of why and why not the approach is effective.

Cross evaluation of task 1 and task 2 between all groups will be run by us (or we will provide scripts for students to perform the cross-evaluation). Evaluation results will be provided to the whole class. After the cross-evaluation, each team should aim to perform necessary analysis on the evaluation results and investigate why your approaches are effective (or ineffective) against some approach.

### Report:
1. Introduce the analysis methods that are used in the task.
2. Analysis results and insights. Possible enhancements, future works. etc.
3. Architecture of your machine learning system (for the whole project).
4. Contribution of individual team members.
5. Citations to all related works.

# Optional Research
If a team wants to go beyond the mandatory tasks and do some extra tasks (totally optional, but highly encouraged), we have some exciting possibilities. For example, there is one idea to deploy the defense on a physical device such as AWS DeepLense or NVIDIA Platforms (TX1, TX2, Xavier). We have these platforms in the lab and we can facilitate access to these devices for doing some exciting experiments. As you know, with Athena, there is a tradeoff space (adding/removing WDs and changing ensemble strategy) and you can test it with physical environments. This requires some creativity and motivation to come up with some nice experiments and demo. This optional task is highly encouraged for highly motivated students who want to learn more about adversarial ML and do some research in this direction.
