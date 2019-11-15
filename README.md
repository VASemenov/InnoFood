# InnoFood
## Instructions for installing and running InnoFood application
Innofood is Django application. For backend, application configured with
**db.sqlite3'**, for user interface with **Bootstrap4** used. To run Innofood
you will need to install Python 3.x and dependencies from requirements.txt.
It is best to use the python `virtualenv` with `Pipenv` for build locally. For
more guide and instructions please visit [Pipenv page](https://pipenv.kennethreitz.org/en/latest/).

### Prepare environment for Linux

``` shell
$ sudo apt-get install python3-pip
# install Pipenv
$ pip3 install pipenv
```

### Prepare environment for Windows

For installation python3 in `Windows` operating system please visit  [python official](https://www.python.org/downloads/). For installation pip please follow instructions from [this page](https://pip.pypa.io/en/stable/installing/). For installing Pipenv please visit [this page](https://www.jetbrains.com/help/pycharm/pipenv.html).
``` shell
# if everything get python version 3.x you are in good shape
$ python --version
$ pip --version
$ pip install pipenv
```

### Prepare environment for Mac

``` shell
# install package manager Homebrew
$ /usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)
# confirm installation
$ brew doctor
# install python3
$ brew install python3
$ brew install pipenv
```

### Run project
For `Windows` use [PowerShell](https://docs.microsoft.com/en-us/powershell/scripting/install/installing-powershell-core-on-windows?view=powershell-6) instructions.

``` shell
$ git clone https://github.com/Eng-MFQ/InnoFood.git
$ cd InnoFood
# create virtualenv environment for InnoFood
$ pipenv shell
# change directory to `scripts`
cd scripts
# run and install dependencies
pip3 install -r requirements.txt
# go to `innofood` directory 
cd innofood
# run application open 127.0.0.1:8000/ in your favorite browser
$ python3 manage.py runserver
```
## Video instruction
if you have any problem follow any of the instruction above, watch this helpful video [how to install and run django](https://youtu.be/qgGIqRFvFFk?list=PL6gx4Cwl9DGBlmzzFcLgDhKTTfNLfX1IK)

## Contact us
If you have any problem you can always contact us on Telegram
- Muwaffaq imam : @moofiy 
- Eldar Qurbanov : @eldarqurbanov


## Introduction
Despite today’s advancements in technology, it is still common to notice all food points in the campus accept orders over the counters while relying on their best efforts for delivery. IU students might frequently have unforeseen changes in their programs or anticipate a possible absence to a scheduled meal plan for a particular day and in that case, stands the risk of not having time to eat for an already paid meal.

## Objectives
- Make eating plan schedules more flexible
- Reduce the pain of moving between floors after a tiring day
- Exposure to larger pool of dishes to choose from.
- Enhance the feeding experience of UI student.
- Higher possibility for customized feeding plan to the highest extend.

## Project Description and Features
We propose a delivery app that will allow IU students to better their feeding experience within the University and also one through which the canteen can offer a better experience.  The student will be able to choose with ease already preconfigured meal combo from a variety of arrays from different cafes within the campus and living areas.
Students will be able to order for their meals and be delivered to their preferred destination on preferred delivery time. Apart from this, they also can schedule a pick-up and cancel the order one hour prior to delivery.
The student can make an order which the canteen will receive in realtime and act upon it.

### Main features include:
- Getting all food point update menu of each café in the campus for the next day.
- Ability to order food snacks at the comfort of your seat/room.
- Choose delivery time
- Ability cancel order 1hr to delivery
- Have accountable to schedule pickup of delivery 

## Target customers
*Busy students* - During strict deadlines and a high volume of studies students can easily order foods without distractions.
*Innopolis hosts* - they can also check the meal menu and use food delivery service while they are staying at University.
