#!/usr/bin/python3
# _*_coding:utf-8 _*

#################################
# Title : Password Generator    #
# Author : G. Musin             #
# Localization : Belgium        #
#################################

# Importing library
import random

# program
count = input("How many character do you want ? ")
for item in range(int(count)):
    character = [chr(random.randint(48, 57)), chr(random.randint(65, 90)), chr(random.randint(97, 122))]
    print(character[random.randint(0, 2)], end="")
print("\n")
