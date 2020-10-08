# Installation
**I encourage you to search for solutions on Google, StackOverflow, official user guides, and discuss on [GitHub](https://github.com/csce585-mlsystems/project-athena/issues) whenever you encounter any installation problems.**

## Install Anaconda
Anaconda is a free and open-source distribution of the Python and R programming languages for scientific computing, that aims to simplify package management and deployment.

Install Anaconda on your computer: https://docs.anaconda.com/anaconda/install/.

## Create an environment
Create an environment for Athena project with a python version of 3.6+ (I use Python 3.7). Activate your environment after it is created.

Create an environment
https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html#id1

Activate an environment
https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html#activating-an-environment

e.g.,

``conda create --name athena python=3.7``

``conda activate athena``

**The following steps must be done in your athena environment (the one you created)**
## Install PyTorch
Install PyTorch. You can find corresponding command line from [here](https://pytorch.org/get-started/locally/#mac-anaconda). 

e.g., install a cpu-only pytorch

``conda install pytorch torchvision cpuonly -c pytorch``


## Install libraries for Athena
You can install required libraries from the [requirements.txt](https://github.com/csce585-mlsystems/project-athena/blob/master/requirements.txt).

### Use pip
Please note that ``pip`` is not installed by default. However, pip is usually installed on a user level, once it is installed, you can use it in all anaconda environment.

Install pip by

``conda install pip``

Install via requirements.txt

``pip install -r requirements.txt``

**If you failed to directly install packages/libraries from requirements.txt, a workaround solution is to install the listed packages one by one manually.** Here are the installations to individual packages/libraries:
1. install [theconf](https://github.com/wbaek/theconf)
2. install [pytorch-gradual-warmup](https://github.com/ildoonet/pytorch-gradual-warmup-lr)
3. install [pystopwatch](https://github.com/ildoonet/pystopwatch2)
4. install [hyperopt](https://github.com/hyperopt/hyperopt)
5. install pretrainedmodels [pip](https://pypi.org/project/pretrainedmodels/), [conda](https://anaconda.org/conda-forge/pretrainedmodels)
6. install tqdm [pip](https://pypi.org/project/tqdm/), [conda](https://anaconda.org/conda-forge/tqdm)
7. install tensorboardX [pip](https://pypi.org/project/tensorboardX/), [conda](https://anaconda.org/conda-forge/tensorboardx)
8. install sklearn [office](https://scikit-learn.org/stable/install.html), [pip](https://pypi.org/project/scikit-learn/), [conda](https://anaconda.org/anaconda/scikit-learn)
9. install [ray](https://pypi.org/project/ray/)
10. install matplotlib [office](https://matplotlib.org/users/installing.html), [pip](https://pypi.org/project/matplotlib/), [conda](https://anaconda.org/conda-forge/matplotlib)
11. install psutil [pip](https://pypi.org/project/psutil/), [conda](https://anaconda.org/anaconda/psutil)
12. install Requests [office](https://requests.readthedocs.io/en/master/user/install/), [pip](https://pypi.org/project/requests/)
13. install [adversarial-robustness-toolbox (ART)](https://github.com/Trusted-AI/adversarial-robustness-toolbox/wiki/Get-Started#setup) 
14. install keras-resnet [pip](https://pypi.org/project/keras-resnet/), [conda](https://anaconda.org/conda-forge/keras-resnet)

### Use conda
**Do NOT use conda to install requirements for Athena project. You will fail as many required libraries such as IBM ART do not support conda installation yet.**

# Create Athena project
## via Command line
Clone a local copy from remote repository via command: https://docs.github.com/en/free-pro-team@latest/github/creating-cloning-and-archiving-repositories/cloning-a-repository.

Mantain the project: https://docs.github.com/en/free-pro-team@latest/github

## via IDE
You can use any python IDE. Since I am using [PyCharm](https://www.jetbrains.com/pycharm/), I will use PyCharm as the example. I believe other IDEs should provide VCS tools, simply follow the official user guides to create a project and put it under control.

1. [Download and install PyCharm](https://www.jetbrains.com/help/pycharm/installation-guide.html#silent)
2. **Team leader please fork the project first.** Then team members can create a project from the team repo. [Create a project from git](https://www.jetbrains.com/pycharm/guide/tips/create-project-from-github/) Or, if you have already downloaded Athena, you can also [create a project from existing local source](https://www.jetbrains.com/help/phpstorm/creating-a-project-from-existing-local-sources.html#4fa83), then [put it under Git version control](https://www.jetbrains.com/help/pycharm/set-up-a-git-repository.html#put-existing-project-under-Git).
3. [Configurate the inspector for you project](https://www.jetbrains.com/help/pycharm/configuring-python-interpreter.html#add-existing-interpreter). **Select the conda environment you created in the previous step**.

# It is all set. Enjoy!

# References
1. [Anaconda](https://docs.anaconda.com/).
2. [PyTorch]().
3. [Git](https://try.github.io/) and [GitHub]().
4. [PyCharm](https://www.jetbrains.com/help/pycharm/quick-start-guide.html).