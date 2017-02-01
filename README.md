## Motivation
This repo is meant to organize the various projects that I will be working on with my Raspberry Pi.
# Projects
## [The Choice](https://github.com/ajr-zimmer/RPi-projects/tree/master/the-choice)
*The Choice* is a project that was inspired by Neo’s choice in the Matrix films. After realizing that we had a red and blue LED to work with, I knew I could make an interesting homage to the films.

The project consists of a breadboard, Raspberry Pi Model B, a red LED, a blue LED, and a button. The Choice begins by starting the program `wake_up.py`. The user is prompted to push the physical button on the breadboard. Upon doing so, another script begins (`server.py`), which launches a Tornado web server hosting a web page. The address of this web page is given to the user via terminal. When visiting the page, Morpheus greets the user and presents two coloured pills (one red, one blue). When a pill is selected, the corresponding coloured LED turns on.
