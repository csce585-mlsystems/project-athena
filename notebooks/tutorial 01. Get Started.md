# Installation
**I encourage you to search for solutions on Google, StackOverflow, official user guides, and discuss on [GitHub](https://github.com/csce585-mlsystems/project-athena/issues) whenever you encounter any installation problems.**

## Install Anaconda
Anaconda is a free and open-source distribution of the Python and R programming languages for scientific computing, that aims to simplify package management and deployment.

Install Anaconda on your computer: https://docs.anaconda.com/anaconda/install/.

## Create and setup the environment from yml file
[Create an environment from yml file](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html#creating-an-environment-from-an-environment-yml-file) 

The yml file for Athena project (you may want to update the **prefix** before you start): ``athena-environment.yml``.

Or, you can follow the following this guide to set up the environment manually.
----------
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
