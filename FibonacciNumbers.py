i=1
a=-1
b=1
n=int(input("enter a number to print fibonacci number: "))
while i<=n:
    c=a+b
    print(c,end=" ")
    a=b
    b=c
    i=i+1


