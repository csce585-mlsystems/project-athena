# Fall 2020
This branch is for the grading in fall 2020.

## Structure
Materials in this branch is organized in the following structure:
```
Task1
  |--- Group1
  |      |--- README.md (information of the task)
  |      |--- Submissions (a folder contains submissions for task1)
  |      |--- Comments.md (Comments from instructors)
Task2
  |--- Group1
  |      |--- README.md (information of the task)
  |      |--- Submissions (a folder contains submissions for task1)
  |      |--- Comments.md (Comments from instructors)
Task3
  |--- Group1
  |      |--- README.md (information of the task)
  |      |--- Submissions (a folder contains submissions for task1)
  |      |--- Comments.md (Comments from instructors)
```

**Grades for each task are given in dropbox.**

## Criteria
|   |   Task1   |   Task2 Opt1  | Task2 Opt2    |   Task2 Opt4  |
|:--:|:--:|:--:|:--:|:--:|
|Assignment|  5%  |   5%  |   5%  |   5%  |
|Background|  15%   |   15% |   15% |   15% |
|Experimental Settings| 30% |   30% |   20% |   25% |
|Results and Discussions|   30% |   30% |   25% |   30% |
|Citation and Contribution| 10% |   10% |   5%  |   5%  |
|Implementation (scripts)|  10% |   10% |   30% |   20% |

## Report
A sample report for your reference: [Clutch](https://github.com/Dojones98/project-athena/blob/master/task1/report_task1.ipynb)

1. **Assignment**. Briefly introduce the assignment. What to do in assignment.
2. **Background**. Introduce the attacks, methods, techniques you used in the assignment. Sample background: [JiR](https://github.com/Jacob-L-Vincent/project-athena/blob/master/reports/Report%281%29.ipynb).
3. **Experimental Study**. Sample experiment study: [doubleE](https://github.com/andrewwunderlich/project-athena/blob/master/Task%201/Task1Report.pdf) and [Ares](https://github.com/cjshearer/project-athena/blob/master/Task2/Report.ipynb) (the breakdown of the task).
    1. Do NOT post scripts (except very small pieces) directly, leave the scripts and configurations in the original files instead. List all relevant files with necessary brief descriptions.  
    2. Experiment Design. How you will launch the experiment, with high-level steps. Provide information that are needed in order to replicate your experiment. For example, What attacks (methods and number of variants) used to generate the AEs? What models you evaluated on what AEs? What ensemble(s) (number of weak defense and ensemble strategy) is used? And so on. **Note**: you do NOT need to post the configuration of individual weak defenses (and attack) here, provide the path to the corresponding configuration files instead.
    3. For all tasks, you need to evaluate at least the following models: (1) the undefended model (``UM``), the ``PGD-ADT``, and one ensemble.  
4. **Results and Discussion**. Sample discussion: [doubleE](https://github.com/andrewwunderlich/project-athena/blob/master/Task%201/Task1Report.pdf)
    1. Do NOT post the log.
    2. Visualize your evaluation results with brief description (for people to understand your results: figures and/or tables, etc.).
    3. Discuss the results. 
5. **Citation**. Citations to related works. For example, if you used ``FGSM`` to generate AEs in your assignment, cite [this](https://arxiv.org/abs/1412.6572) work. Sample citation: [JiR](https://github.com/Jacob-L-Vincent/project-athena/blob/master/reports/Report%281%29.ipynb). 
6. **Contributions**. Contributions of individual members. **Please do NOT use initials or nick names of team members.**