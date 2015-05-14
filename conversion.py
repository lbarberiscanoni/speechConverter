#!/usr/bin/python

import subprocess 
import shlex
import time

# convert .docx into .markdown 
fileName = raw_input("Type the name of the file EXACTLY and include the file extension\n \nIf there are spaces, the use \ between each word\n \nExample: GMOs Neg.docx = GMOs\ Neg.docx\n \nEnter Here: ")
year = raw_input("\nwhat year is it? Please use 4 numbers\n :")
month = raw_input("\nwhat month is it? Please use 2 numbers\n :")
day = raw_input("\nwhat day of the month is it? please use 2 numbers\n :")
date = year + "-" + month + "-" + day + "-"
speechTitle = raw_input("\ngive title to this speech, WITHOUT USING CAPITAL LETTERS and using - between each word\n :")
speechName = date + speechTitle + ".markdown"

subprocess.call("w2m " + fileName + " >>" + speechName, shell=True)

# build the front matter and add it to the .markdown file
n_of_tags = input("HOW MANY topic areas does your speech fit in?\n The options are:\n Constitutional Law (conlaw)\n, Counterplans (counterplan)\n, Domestic (domestic)\n, Economics (econ)\n, Foreign Policy (foreign)\n, Philosophical (philosophical)\n \nEnter the NUMBER (as a number and not a word) here :")
time.sleep(1)

tags = []
for i in range(int(n_of_tags)):
    choice = "\n- " + raw_input("\nChoose between conlaw, counterplan, domestic, econ, foreign, and philosophical\n \nEnter the TOPIC AREA here :")
    tags.append(choice)
    time.sleep(1)

if raw_input("Are you Joe, Sarai, Michael, or Will?\n Type y for yes or n for no: ") == "y":
    regular_user = raw_input("Type your name : ")
    if regular_user == "joe" or regular_user == "Joe":
        name = "Joe"
        last_name = "Gunst"
    elif regular_user == "sarai" or regular_user == "Sarai":
        name = "Sarai"
        last_name = "Dai"
    elif regular_user == "lorenzo" or regular_user == "Lorenzo":
        name = "Lorenzo"
        last_name = "Barberis-Canonico"
    elif regular_user == "will" or regular_user == "Will":
        name = "Will"
        last_name = "Tapp"
    else:
        name = "Michael"
        last_name = "Gallagher"
else:
    name = raw_input("\nwhat is your name? (capitalize the first letter): ")
    last_name = raw_input("\nwhat is your last name? (1 word limit and capitalize the first letter): ")

authorID = name + "-" + last_name

with open(speechName, "r") as file:
    originalText = file.read()

with open(speechName, "w") as file:
    file.write("---\n" + "layout: post\n" + "tags: "+ " ".join(tags) + "\nauthor: " + authorID + "\n---\n" + originalText)
