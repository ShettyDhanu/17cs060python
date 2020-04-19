"""
to check number amstrong
"""

def isArmstrong(st):
    p=len(st)
    n=int(st) #to find exponential
    tot=0
    num=n
    while n>0: #if the no is greater than 0 we need to find length that is p
        d=n%10
        tot=tot+(d**p)
        n=int(n/10)
    if num==tot:
        return True
    else:
        return False

x=input("enter) no")

if isArmstrong(x):
    print(x,"is an armstrong number")
else:
     print(x,"is not a armstrong number")
    
        
        
