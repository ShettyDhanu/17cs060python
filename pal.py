"""
to check no palindrome or not"""

def ispalindrome(n):
    num=n
    rev=0
    d=0
    while n>0:
        d=n%10
        n=int(n/10)
        rev=rev*10+d
    if(num==rev):
        return True
    else:
        return False

x=int(input("enter the number"))
if  ispalindrome(x):
    print(x,"is a palindrome")
else:
    print(x,"is not a palindrome")
