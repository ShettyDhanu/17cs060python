"""
python program to accept the user name and their age printout the a message by addressed to them
that tells them the year that they will turn 100 years old

"""
name=input("enter the name:")
age=int(input("enter the age"))
from datetime import date
yr=date.today().year
print("{} will turn 100 year old in the year{}".format(name,yr+100-age))
