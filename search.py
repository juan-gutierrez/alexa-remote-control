#!/usr/bin/env python3

import re
import os
import time

getState = False
getJobState = False
currentJobState = "none"
newJobState = "none"
prevState = "none"

while True:

    os.system("./test.py > mytest.txt")
    

    with open("mytest.txt") as openfile:
        for line in openfile:
            for part in line.split():
                if (getState):
                    print(part)
                    currentState = part
                    getState = False
                if (getJobState):
                    print(part)
                    newJobState = part
                    getJobState = False
                if "'machineState'" in part:
                    getState = True
                if "'washerJobState'" in part:
                    getJobState = True
            

    print("Current states is ", currentState)

    if (re.search("run", currentState)):
        prevState = "run"
        print("Lavadora is running")
        if (re.search("weightsensing", newJobState)):
           print("La lavadora esta calentando motores")
           mystring = "./alexa_remote_control.sh -d \"Comedor\" -e speak:" + "\"La lavadora esta calentando motores\""
           mystring2 = "./alexa_remote_control.sh -d \"Dormitorio\" -e speak:" + "\"La lavadora esta calentando motores\""
        if (re.search("wash", newJobState)):
           print("La lavadora comenzo a lavar, chaca chaca")
           mystring = "./alexa_remote_control.sh -d \"Comedor\" -e speak:" + "\"La lavadora comenzo a lavar, chaca chaca\""
           mystring2 = "./alexa_remote_control.sh -d \"Dormitorio\" -e speak:" + "\"La lavadora comenzo a lavar, chaca chaca\""
        if (re.search("rinse", newJobState)):
           print("La lavadora esta enjuagando con Suavitel, pa dejar suavecita la ropita del Gato")
           mystring = "./alexa_remote_control.sh -d \"Comedor\" -e speak:" + "\"La lavadora esta enjuagando con Suavitel, pa dejar suavecita la ropita del Gato\""
           mystring2 = "./alexa_remote_control.sh -d \"Dormitorio\" -e speak:" + "\"La lavadora esta enjuagando con Suavitel, pa dejar suavecita la ropita del Gato\""
        if (re.search("spin", newJobState)):
           print("La lavadora ta exprimiendo, gira que gira")
           mystring = "./alexa_remote_control.sh -d \"Comedor\" -e speak:" + "\"La lavadora ta exprimiendo, gira que gira\""
           mystring2 = "./alexa_remote_control.sh -d \"Dormitorio\" -e speak:" + "\"La lavadora ta exprimiendo, gira que gira\""
        if (re.search("drying", newJobState)):
           print("La lavadora ta secando, que calorsh")
           mystring = "./alexa_remote_control.sh -d \"Comedor\" -e speak:" + "\"La lavadora ta secando, que calorts\""
           mystring2 = "./alexa_remote_control.sh -d \"Dormitorio\" -e speak:" + "\"La lavadora ta secando, que calorts\""
        if (re.search("finish", newJobState)):
            print("Ya esta la ropita")
            mystring = "./alexa_remote_control.sh -d \"Comedor\" -e speak:" + "\"Por fin. Ya esta la ropita\""
            mystring2 = "./alexa_remote_control.sh -d \"Dormitorio\" -e speak:" + "\"Por fin. Ya esta la ropita\""

        if (newJobState != currentJobState):
            currentJobState = newJobState;
            os.system(mystring)
            time.sleep(2)
            os.system(mystring2)

    if (re.search("stop", currentState)):
        if(prevState == "run"):
            mystring = "./alexa_remote_control.sh -d \"Comedor\" -e speak:" + "\"Parece que la lavadora se detuvo. Y ya esta la ropita\""
            mystring2 = "./alexa_remote_control.sh -d \"Dormitorio\" -e speak:" + "\"Parece que la lavadora se detuvo. Y ya esta la ropita\""       
            prevState = "stop" 
            os.system(mystring)
            time.sleep(2)
            os.system(mystring2)

    time.sleep(5)
