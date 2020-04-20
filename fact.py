"""
facorial of a number using recurssion 
"""
def fact(n):
    if(n==0):
        return 1
    else:
        return n*fact(n-1)
x=int(input("enter the number"))
y=fact(x)
print("{}!={}".format(x,y))
