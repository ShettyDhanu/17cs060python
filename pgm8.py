# -*- coding: utf-8 -*-
"""
Created on Thu Mar 26 20:52:10 2020

@author: admin
"""

def upperlower(string):
    upper=0
    lower=0
    for i in range(len(string)):
        if(ord(string[i])>=97 and ord(string[i])<=122):
            lower+=1

        elif(ord(string[i])>=65 and ord(string[i])<=90):
            upper+=1
    print("lower case charecter is=%"%lower,"upper case charecter is=%"%upper)
string=input("enter the string")
upperlower(string)