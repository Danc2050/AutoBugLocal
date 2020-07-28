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
