import readchar
import os

running = True


while running:

    k = readchar.readchar()
    if  k == "w":
        cmd0 = "echo 0=-250 > /dev/servoblaster"
        cmd1 = "echo 1=250 > /dev/servoblaster"
        os.system(cmd0)
        os.system(cmd1)
    elif k == "x":
        cmd0 = "echo 0=250 > /dev/servoblaster"
        cmd1 = "echo 1=-250 > /dev/servoblaster"
        os.system(cmd0)
        os.system(cmd1)
    elif k == "a":
        cmd0 = "echo 0=50 > /dev/servoblaster"
        cmd1 = "echo 1=0 > /dev/servoblaster"
        os.system(cmd0)
        os.system(cmd1)
    elif k == "d":
        cmd0 = "echo 0=0 > /dev/servoblaster"
        cmd1 = "echo 1=-50 > /dev/servoblaster"
        os.system(cmd0)
        os.system(cmd1)
    elif k == " ":
        cmd0 = "echo 0=0 > /dev/servoblaster"
        cmd1 = "echo 1=0 > /dev/servoblaster"
        os.system(cmd0)
        os.system(cmd1)
    elif k == "o":
        running = False

