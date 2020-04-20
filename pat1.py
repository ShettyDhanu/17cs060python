"""
write a program to write pattern
*
**
***
using nested loop
"""

n=int(input("enter the no of lines"))
for i in range(n):
    for j in range(i+1):
        print("*",end='')
    print('')
