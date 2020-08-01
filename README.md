# AutoBugTracker (Local Side)
> Updated: 7/28/2020

> NOTE: AutoBugTracker currently exists as two separate and distinct repositories. One, for the [local side](https://github.com/Danc2050/AutoBugLocal) and the other for the [server side](https://github.com/Danc2050/TheBugTracker). You're currently on the local side :open_mouth: :cloud: :umbrella:.

## Contents
* [Description](#description)
	* [What is AutoBugTracker?](#what-is-autobugtracker)
	* [Why use AutoBugTracker?](#why-use-autobugtracker)
	* [Who should use AutoBugTracker?](#who-should-use-autobugtracker)
* [Instructions](#instructions)
    * [Setup](#setup)
    * [Usage](#usage)
* [Features](#features)
	* [Current](#current)
	* [Stretch Goals](#stretch-goals)
* [Contributors](#contributors)
	* [Product Owners / Sponsors](#product-owners--sponsors)
	* [Development Team](#development-team)

## Description
### What is AutoBugTracker?
AutoBugTracker is a python program that executes a client program, detects bugs, and filters bugs of your choosing. It then sends any bugs it encounters to a server where it, records, and reports the bugs to Github. AutoBugTracker utilizes a PostgreSQL database to help keep things organized and keeps team members updated on the status of bugs via email.

### Why use AutoBugTracker?
AutoBugTracker facilitates an efficient workflow for programmers, making it a great addition to any development suite.

### Who should use AutoBugTracker?
AutoBugTracker is valuable to developers working in large teams, that need the ability to accumulate a large quantity of debug information from their customers. AutoBugTracker is highly configurable and can be tailored for your teams specific needs.

## Instructions
### Setup
Currently the AutoBugTracker client side repository can be cloned [here](https://github.com/Danc2050/AutoBugLocal).  
  
_Eventually we would like to set this up as a pip package._

#### Windows Setup
To run AutoBugTracker on windows machines you will need to install WSL 1 and the Ubuntu terminal for windows 10.  

1. Install the Windows Subsystem for Linux.
	1. Open PowerShell as Administrator:
		1. To open the PowerShell type `PowerShell` into the search box on windows 10.
	2. To install WSL 1 for windows copy and paste this command into PowerShell, then restart your computer:
		1. `dism.exe/online/enable-feature/featurename:Microsoft-Windows-Subsystem-Linux/all/norestart`.
2. Installing Ubuntu.
	1. Once WSL 1 has been installed and enabled, open the windows Microsoft store by searching for it in the Windows 10 search bar.
	2. Now search for Ubuntu and then click on install to start installing.
	3. Now that Ubuntu has been installed launch the process. The first time Ubuntu is opened it will finish installing some files and then ask you to create a username and password.
	4. Once the above setup is done you have installed WSL 1 and the Ubuntu Linux distribution that can be used to run AutoBugTracker.
3. Updating Ubuntu and Installing pip.
	1. Now that Ubuntu is installed you may need to update it.
		1. At the Ubuntu command line type: `sudo apt update`.
		2. Now there may be some libraries that need to be installed so AutoBugTracker can run. Install pip if you have not already by typing in: `sudo apt install python3-pip`.
		3. Now when you try to run AutoBugTracker and there are some dependencies missing you can install them using pip3.
4. Setting up AutoBugTracker in Ubuntu.
	1. Now that we have the proper environment setup to use AutoBugTracker on Windows 10 we need to pull the project from the github repo and set up the correct python path.
		1. Create a directory for AutoBugTracker.
			1. `mkdir someDirectory`.
		2. Now go to the AutoBugLocal [repo](https://github.com/Danc2050/AutoBugLocal) and copy the link under the green code button.
		3. Once you have copied the link under the green code button, `cd` into the directory that you want to clone the repo into and enter the following command:
			1. `git clone https://github.com/Danc2050/AutoBugLocal.git`.
5. Running AutoBugTracker.
	1. Now the `PYTHONPATH=` variable needs to be added to your `.bashrc` file.
		1. Go to your base directory and you can type:
			1. `ls -a` and then `vim .bashrc`.
		2. At the very bottom of the `.bashrc` file on a new line add:
			1. `export PYTHONPATH=$PWD/AutoBugLocal;`.
				1. Save the changes and exit the `.bashrc` file.
			2. Now at the command line type: `source .bashrc`.
		3. At the Ubuntu command line type:
			1. `PYTHONPATH=$PWD/AutoBugLocal`.
6. Running your tests.
	1. To run tests using AutoBugTracker you will want to be in the AutoBugLocal directory and then create a new directory for your test scripts.
		1. `mkdir localTests`.
			1. `cd` into this directory and you can put your tests scripts in here.
				1. Mine is called `test.py`.
		2. To run AutoBugTracker along with a test script `cd` into AutoBugLocal and then type, depending on your test directory and script name:
			1. `python3 src/Main.py -S localTests/test.py`.
            2. **Note:** You may need to run the command `chmod +x test.py` in order for AutoBugTracker to be able to execute the test script.

#### Example Black List
A black list can be configured locally to prevent any unwanted/unnecessary bugs from making it to the server.  
  
_In the future we will probably have the local black list sync up with one located at the remote server. This would make sure that all clients ignore the same kinds of bugs._

**black.list**:

```
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'spam' is not defined

Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: Can't convert 'int' object to str implicitly
```

### Usage
AutoBugTracker can be run by using the command `python3 AutoBugLocal -S client-program`

## Features
### Current
* Execute client program and capture output of bugs.
* Black-list filtering.

### Stretch Goals
* Alter config options at program execution via command line arguments.
* Capture bugs from programs written in more languages.
* Pip package.
* Formalize project. (Give it more professional layout features, i.e. `__main__.py`, `-help` command, etc.)
* Record user input to see what they did specifically when a bug occurred.

## Contributors
### Product Owners / Sponsors
> [:grin: Daniel Connelly](https://www.linkedin.com/in/dconnelly2/)  
> [:sweat_smile: Teal Dulcet](https://www.tealdulcet.com/)

### Development Team
#### Team Lead
> :joy: Antonio DiMaggio

#### Software Engineers
> :smirk: Ryan Campbell  
> :laughing: Ramon Guarnes  
> :grinning: Dana Khoshnaw  
> :blush: Princess Kim  
> :wink: Armando Lajara  
> :sunglasses: Mahmoud Al Robiai
