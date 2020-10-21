## Intro
  This is a working set of instructions to set up the athena conda environment for both Linux and Windows machines.  
  This set up will run both the craft_adversarial_examples.py and transformation.py within the tutorials directory. 

### Create a new environment, be sure to set python to 3.7
	conda create --name env_name python=3.7

### Activate that environment
	conda activate env_name

### Install pytorch - follow link in tutorial.md if not sure which command line to use. I used:
	conda install pytorch torchvision -c pytorch

### Install tensorflow
	conda install tensorflow==1.13.1

### Install the opencv libs:
	conda install opencv==3.4.2

### Install the new requirements.txt file from Athena main directory
	pip install -r requirments.txt

### Downgrade the following packages:
	pip install Pillow==7.0.0
	pip install scikit-learn==0.22.1
	pip install Keras==2.3.0
	pip install scipy==1.4.1

-- Following instructions for pycharm. 
1. Import the athena source code via git
2. Right click on the src folder and Mark Directory as > Source
3. Press Ctrl + Alt + S, under Project: proj_name, select Python Interpreter.  
	  - Press the gear next to Python Interpreter on right and Add.  
	  - Find where you installed Anaconda and find the python.exe in the correct env directory.

Note for Windows users:  
I do not know if this will happen on all machines but my pycharm thought transformation.py was
a test file because of the test() in it and as such continually tried to open it with a non existing module "pytest." Should that 
be the case, press the drop down in the top right and select Edit Configurations.  
From there the left hand side will have a Python drop down and a Test drop down. Delete the transformation under the Test drop down list and Apply.
I did not have to do this when I tested the Linux install.
