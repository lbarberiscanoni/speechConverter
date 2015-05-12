#!/usr/bin/python

import subprocess 
import shlex
import time

# convert .docx into .markdown 
fileName = raw_input("Type the name of the file EXACTLY and include the file extension\n :")
year = raw_input("what year is it? Please use 4 numbers\n :")
month = raw_input("what month is it? Please use 2 numbers\n :")
day = raw_input("what day of the month is it? please use 2 numbers\n :")
date = year + "-" + month + "-" + day + "-"
speechTitle = raw_input("give title to this speech, without using capital letters and using - between each word\n :")
speechName = date + speechTitle + ".markdown"

subprocess.call("w2m " + fileName + " >>" + speechName, shell=True)

# build the front matter and add it to the .markdown file
n_of_tags = input("How many topic areas does your speech fit in?\n The options are:\n Constitutional Law (conlaw)\n, Counterplans (counterplan)\n, Domestic (domestic)\n, Economics (econ)\n, Foreign Policy (foreign)\n, Philosophical (philosophical)\n \nEnter the number (as a number and not a word) here :")
time.sleep(1)

tags = []
for i in range(int(n_of_tags)):
    choice = "\n- " + raw_input("\nChoose between conlaw, counterplan, domestic, econ, foreign, and philosophical\n \nEnter the topic area here :")
    tags.append(choice)
    time.sleep(1)

name = raw_input("\nwhat is your name? (capitalize the first letter): ")
last_name = raw_input("\nwhat is your last name? (1 word limit and capitalize the first letter): ")
authorID = name + "-" + last_name

with open(speechName, "r") as file:
    originalText = file.read()

with open(speechName, "w") as file:
    file.write("---\n" + "layout: post\n" + "tags: "+ " ".join(tags) + "\nauthor: " + authorID + "\n---\n" + originalText)
