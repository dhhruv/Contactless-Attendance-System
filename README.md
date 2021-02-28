# Contactless-Attendance-System

### Recognize The faces And Take Automatic Attandance. :sparkles:

![Face Recognition Logo](https://github.com/kmhmubin/Face-Recognition-Attendance-System/blob/master/Document%20Metarial/Project%20demo%20images/Face-Recognition-Attendance-System-Logo.jpg)


![GitHub](https://img.shields.io/github/license/kmhmubin/Face-Recognition-Attendance-System)

## Motivation :astonished:
----------------------------
This Repository was created as a part of MINeD Hackathon, a national level hackathon organized by Centre of Excellence in Data Science at the CSE Department of Nirma University.
We seek to provide a valuable attendance service for both teachers and students. Reduce manual process errors by provide automated and a reliable attendance system uses face recognition technology.

## Features :clipboard:
---------------------------
* Check Camera
* Capture Faces
* Train Faces
* Recognize Faces & Attendance
* Automatic Email

## Screenshots :camera:
-----------------------------------
### Command Line Interface

![Command Line Interdace](https://github.com/kmhmubin/Face-Recognition-Attendance-System/blob/master/Document%20Metarial/Project%20demo%20images/CODE%20INTERFACE.png)

### Checking Camera

![Checking Camera](https://github.com/kmhmubin/Face-Recognition-Attendance-System/blob/master/Document%20Metarial/Project%20demo%20images/Program%20working.jpg)

### Automail 

![Automail](https://github.com/kmhmubin/Face-Recognition-Attendance-System/blob/master/Document%20Metarial/Project%20demo%20images/automail.jpg)


## Tech Stack Used :computer:
--------------------------
Build With - 
* Python 3.8

Modules Used -

All The Module are Latest Version.
* OpenCV Contrib 4.0.1
* Pillow
* Numpy
* Pandas
* Shutil
* CSV
* yagmail

Facial Recognition Algorithms -
* Haar Cascade
* LBPH (Local Binary Pattern Histogram)

Softwares Used -
* Pycharm 2019.2
* VS CODE 
* Jupyter Notebook
* Git

## Installation :key:
-----------------------------------

#### Download or Clone the project

First Download or Clone the Project on Your Local Machine. To download the project from GitHub press **Download Zip**

![Download Zip](https://github.com/kmhmubin/Face-Recognition-Attendance-System/blob/master/Document%20Metarial/Project%20demo%20images/download%20zip.png)

or 

You can clone the project with git bash.To clone the project using git bash first open the git bash and write the following code
```
git clone https://github.com/kmhmubin/Face-Recognition-Attendance-System.git
```
demo 

![Git clone](https://github.com/kmhmubin/Face-Recognition-Attendance-System/blob/master/Document%20Metarial/Project%20demo%20images/git%20clone_edit_0.gif)

After download, Open the project using **Pycharm or VSCODE**. Then we have to create an python enviroment to run the program.

#### create enviroment 
First open the terminal or command line in the IDE.Then write the following code.
```
python -m venv venv
```
Then activate the enviroment using the code below for windows.
```
.\venv\Scripts\activate
```
[ *Notice:*
If your pc don't have virtual enviroment or pip install the follow this link.
[How to create Virtual Enviroment](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/) ]

#### Installing the packages
--------------------------------------------------

After creating the enviroment on your project let's install the necessary packages. 

![pip isntall demo](https://github.com/kmhmubin/Face-Recognition-Attendance-System/blob/master/Document%20Metarial/Project%20demo%20images/pip%20install_edit_0.gif)

To install those package open the terminal or command line and paste the code from below

```
pip install -r requirements.txt
```

[ **Note: During the package installation, sometimes it shows errors due to package dependencies and to avoid those error you can install those packages as admin.** ]

## Test Run :bicyclist:
-----------------------
After creating the virtual environment and installing the packages, open the IDE terminal to run the program.
1. To use Command Line Version Use:

```
py main.py
```
2. To use GUI Version Use:

```
py main_gui.py
```
Here is a demo to run the program. I'm Using the Pycharm IDE in my demo.

![Test Run](https://github.com/kmhmubin/Face-Recognition-Attendance-System/blob/master/Document%20Metarial/Project%20demo%20images/code%20demo_edit_0.gif)

## How To Use? :pencil:
----------------------
If you want to use it then follow the steps below:

1. First download or clone the repository.
2. Import the project to your preferable IDE.
Recommended : PyCharm
3. Create a python virtual environment.
4. Install all the packages from [requirements.txt]().
5. Change the mail information in the [Info.py]().
6. Run the project using the Command Prompt or PowerShell or your IDE Terminal Button.