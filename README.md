## Motivation
This repo is meant to organize the various projects that I will be working on with my Raspberry Pi.

# Projects
## [The Choice](https://github.com/ajr-zimmer/RPi-projects/tree/master/the-choice)
*The Choice* is a project that was inspired by Neo’s choice in the Matrix films. After realizing that we had a red and blue LED to work with, I knew I could make an interesting homage to the films.

The project consists of a breadboard, Raspberry Pi Model B, a red LED, a blue LED, and a button. The Choice begins by starting the program `wake_up.py`. The user is prompted to push the physical button on the breadboard. Upon doing so, another script begins (`server.py`), which launches a Tornado web server hosting a web page. The address of this web page is given to the user via terminal. When visiting the page, Morpheus greets the user and presents two coloured pills (one red, one blue). When a pill is selected, the corresponding coloured LED turns on.

## [Oberyn](https://github.com/ajr-zimmer/RPi-projects/tree/master/oberyn-bot)
*Oberyn* uses light and pressure sensors to play variations of sounds from the fight scene of “The Mountain and the Viper”, an episode from the popular TV show “Game of Thrones”. The entire instrument is built in the form of a head, with two pressure sensors placed at the eyes, and a number of pull tabs placed on either side of the head. Additionally, there is an LDR inside the head, and a light source that is connected to the Raspberry Pi. The pull tabs move coloured slides that filter the light from our USB light source, and provide our LDR with varying degrees of luminosity. There is a head crushing sound that is played in a loop. It's volume is controlled by how much light is reaching the LDR. Each pressure sensor plays a different scream from the scene, and the amount of pressure placed on the sensor determines the volume. Using the pull tabs and pressure sensors, the user can step into the shoes of The Mountain, and create a gory melody. In order to execute the program, just use command `sudo python screambox.py`, and the head will be ready to use.
