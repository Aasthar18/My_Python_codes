def pattern(n):
    for i in range(1,n+1,1):
        for j in range(1,i+1):
            print(j,end=" ")
        print("\n")
n=4
pattern(n)

# msg="goodmorning  "
# print(msg.capitalize())

dic={"p1":10,"p2":2,"p3":50,"p4":45}
print(max(dic))
