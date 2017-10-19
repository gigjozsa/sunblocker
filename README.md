# sunblocker
A (python pyrap) method to remove solar-like RFI from interferometric data

Copyright (c) 2017 Gyula Istvan Geza Jozsa, Paolo Serra, Kshitij Thorat, Sphesihle Makhatini, NRF (Square Kilometre Array South Africa) - All Rights Reserved

## Installation:
### Using virtualenv:
See installing virtualenv below if virtualenv is not installed, i.e. the first command does not work.

Then find out where your virtualenv directories are stored. In this example, this directory is called `~/.virtualenv`. If there is no such directory, create one:
```
$ [mkdir .virtualenv]
```
Then create a virtualenv in which all packages for your project will be installed:
```
$ cd .virtualenv
$ virtualenv --no-site-packages usingsunblock [replace usingsunblock by the name of your choice]
```
This creates a virtualenv called `usingsunblock` (which is an example-name) in the `.virtualenv` directory which is completely independent of any system site-packages, to active the virtualenv run the activation script
```
$ source ~/.virtualenv/usingsundblock/bin/activate
```
Then install the required packages into your virtualenv.
```
$ pip install --upgrade pip
$ pip install -r [path to sunblocker]/requirements.txt
$ pip install [path to sunblocker]/
$ [pip install bla]
$ [pip install blub]
$ ...
```
Any time you activate the virtualenvironment (the `source ...` command above) only the installed packages will be available and the installation is protected against any other installation, that is the virtue of the virtualenv.

To leave the virtualenv (and also disabling sunblocker in that virtual environment), type:
```
$ deactivate
```
### Not using virtualenv
Some would say that using a virtual environment is the safe way. After being warned, type:
```
$ pip install --upgrade pip
$ pip install -r [path to sunblocker]/
```

## Usage:
Use method phazer of class Sunblocker in module sunblocker. See description therein. E.g.:
```
...
import sunblocker
mysb = sunblocker.sunblocker.Sunblocker()
mysb.phazer(['yoyo.ms'], outset = ['yoyout.ms'], channels = a, imsize = 512, cell = 4, pol = 'i', threshold = 4., mode = 'all', radrange = 0, angle = 0, show = 'test.pdf', verb = True, dryrun = False)
mysb.vampirisms(inset = '../IC5264_160627/IC5264_160627.ms', lat = -30.721*units.deg, lon = 21.411*units.deg, hei = 100.*units.m, dryrun = True, avantsoleil = 1.*units.s, apresnuit = 2.*units.s, avantnuit = 3.*units.s, apresoleil = 4.*units.s, horizon = -34.*units.arcmin, nononsoleil = False, flinvert = False, verb = True)
...
```
## Installing virtualenv:
You'll need pip. Run:
```
$ which pip
```
If there is no output, then you need to install pip:
```
$ sudo easy_install pip
```
Then run:
```
virtualenv --version
```
If there is a response (i.e. a version number returned), do nothing. If there is an error message, do:
```
sudo easy_install virtualenv
```
or
```
sudo easy_install virtualenv
```
or
```
sudo apt-get install python-virtualenv
```
then
```
sudo pip install virtualenvwrapper
```
That should do.
