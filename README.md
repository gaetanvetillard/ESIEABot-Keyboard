# ESIEABOT-Keyboard
This is an unofficial code to use [ESIEABot](https://esieabot.esiea.fr/) from SSH console with your laptop keyboard (wireless).
Please, contact me if you have isssues by [mail](mailto:vetillard@et.esiea.fr). 

## Installation

**Installation**

    sudo apt-get install python-dev python-setuptools swig 
    git clone https://github.com/gaetanvetillard/ESIEABot-Keyboard.git
Wait for installation finishing, then :

    cd ESIEABot-Keyboard
    git clone --recursive https://github.com/WiringPi/WiringPi-Python.git
    cd WiringPi-Python
    sudo python setup.py install

**Usage**

When the installation is finished, if there isn't issue, you could do :

    cd ..
    sudo python main.py
Wait for the "Ok" print in the console, and you can use following keys to control the robot :

|Key| Action |
|--|--|
| z | Forward |
| q | Backward |
| s | Left spin |
| d | Right spin |
| t | Stop the robot|
| x | Exit and return to the console |

