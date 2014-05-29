This is a python script used to control omxplayer with a apple remote.
For this script to run we use python-lirc.
You can install it with sudo apt-get install python-lirc.
After this copy the .lircrc file to your home folder and move the lircd.conf file to /etc/lirc/lircd.conf and restart the lirc service with sudo service lirc restart.

Connect your TSOP1838 IRReceiver's pin 1 to pin 12 of your GPIO header pin on your raspberrypi and pin 2 and pin 3 of your receiver to pin 6 and pin 2.

Then start any movie on your pi by typing python omxplayer.py "Movie name with full path".