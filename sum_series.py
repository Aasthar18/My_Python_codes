import math
def Sum(x,n):
    for i in range(1,n,1):
        sum=(-1**i)*(x**(2*i))/(math.factorial(2*i))
        sum+=sum
        s=1+sum
    return s
x=int(input("enter the value of x"))
n=int(input("enter upto ehich you want to print the sum of series:"))

print("the sum of the series is:",Sum(x,n))