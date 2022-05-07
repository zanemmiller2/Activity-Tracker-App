# Programmer: Matthew L Brown
# OSU Email: browmat8@oregonstate.edu
# Course: CS361 - Data Structures
# Assignment: 2.1
# Due Date: 5-9-22
# Most Recent Update: 5-5-22
# Description:  Program to watch an input file located in program root dir named "tips.txt".
#               When parent program writes "tips" into the "tips.txt" file service will
#               delete "tips" from "tips.txt" then locate a random tip *.txt file in the 
#               tips dir and write its contents to a return file called "return_tips.txt".
#               input File "tips.txt"
#               output file "return_tips.txt"

from encodings import utf_8
import os
from os import path
import time
import random

random.seed()
tips_process = True
output_file = False
getText = False
isPath = False

while tips_process == True:
    #
    with open("tips.txt", "r+") as serv_file:
        timeToStart = serv_file.read()
        #print(timeToStart)
        time.sleep(0.25)
        if timeToStart == "run":
            getText = True
            #clearing "tips.txt" input file after getting run command
            serv_file.seek(0)
            serv_file.write("")
            serv_file.truncate()
        if getText == True:
            os.chdir("tips")
            path = os.getcwd()
            subDir = os.listdir(path)
            tempDir = subDir[random.randrange(0, len(subDir)-1, 1)]
            tempPath = path + "/" + tempDir
            isPath = os.path.isdir(tempPath)
            
            #checking to make sure path is a dir and not a file....
            while isPath is False:
                tempDir = subDir[random.randrange(0, len(subDir)-1, 1)]
                tempPath = path + "/" + tempDir
                isPath = os.path.isdir(tempPath)
                
            os.chdir(tempDir)
            #getting file to read
            subTxt = os.listdir(tempPath)
            inputFile = subTxt[random.randrange(0, len(subTxt)-1, 1)]
            tempPath = tempPath + "/" + inputFile
            print(tempPath)
            
            #reseting working directory
            os.chdir("../..")
            path = os.getcwd()

            #clearing output file for new text
            with open("return_tips.txt", "r+") as empty_file:
                empty_file.seek(0)
                empty_file.write("")
                empty_file.truncate()
                empty_file.close()
            #copying tempPath file to "return_tips.txt"
            with open(tempPath, "r", encoding="utf_8") as input:
                with open("return_tips.txt", "w", encoding="utf_8") as output:
                    for line in input:
                        output.write(line)

            #resetting getText
            getText = False