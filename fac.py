def fact(x):
    if(x<=1):
        return 1;
    
    x*fact(x-1)
    print("me")
    
a=fact(3)
print(a)
         
    