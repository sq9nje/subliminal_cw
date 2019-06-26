# Learn CW while you work!
Subliminal CW is a simple application that helps you subconsciously learn Morse code telegraphy while you go about your day at the computer. The program plays back random characters through the speakers. The character is displayed in a small window, which you can pin to your desktop so you can glance at it any time. It's that simple!

## Installation
First things first - you'll need Python3 to run this app, so go get a distribution suitable for your OS. Next, you'll need to either download or clone this repository. 

The application has just a few dependencies, namely it requires the following modules:
* numpy
* six
* pygame

You can install these simply by issueing 
```
pip3 iinstall -r requirements.txt
```
in the directory you saved this project to.

## Usage
Subliminal CW has a few command line parameters that controll it's behaviour.
```
usage: cw.py [-h] [-s WPM] [-t TONE] [-d DELAY] [-r REPEAT] [--debug]

Learn CW while you work!

optional arguments:
  -h, --help            show this help message and exit
  -s WPM, --wpm WPM     Speed in WPM. Default 20
  -t TONE, --tone TONE  Tone frequency in Hz. Default 600
  -d DELAY, --delay DELAY
                        Delay between characters in ms. Default 1000
  -r REPEAT, --repeat REPEAT
                        Number of repetitions of each character.
  --debug               Dispaly debug information.

```

## Known Issues
There are audible clicks at the ends of DITs and DAHs. It's a bit annoying, but I'm working on improving that and hope it will be fixed soon.

## ToDo
* Volume control
* Configurable character sets
* Why limit ourselves to single characters? Why not play back longer phrases like callsigns?
* Got other ideas? Let me know!

### Acknowledgements
[morsecodelib](https://github.com/partofthething/morsecodelib) Copyright (c) 2015 Nick Touran 