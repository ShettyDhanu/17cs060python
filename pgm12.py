#condition statement=if else if
#to find largest number

n1=int(input("enter number1"))
n2=int(input("enter number2"))
n3=int(input("enter number3"))
if(n1>n2)and(n1>n3):
    print("n1 is largest of n3 and n2")
elif(n2>n1)and(n2>n3):
    print("n2 is largest of n3 and n1")
else:
    print("n3 is largest of n1 and n2")
