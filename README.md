# Simple Pi Robot

This code is for a simple pi robot built using continuous rotation servos conneceted directly to the pi without the use of motoro controllers.

## Setup

First you will need to install servoblaster:

```
git clone https://github.com/richardghirst/PiBits.git
cd PiBits/ServoBlaster/user/
make
sudo make install
```

The clone this repository:

```
git clone https://github.com/ipswichmakerspace/simplePiBot.git
cd simplePiBot
```

Run the setup.sh script to setup the servoblaster pins:

```
./setup.sh
```

Install readchar:

```
pip install readchar
```

## Running

The run the program:

```
python robot.py
```

The following keys will be used:

W = go forwards
X = go backwards
A = spin left
D = spin right
<Space> = Stop
O = exit program



