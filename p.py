# # # # # def minsum(l):
# # # # #     s=0
# # # # #     ls=[]
# # # # #     for i in range(len(l)):
# # # # #         S=sum(l[i])
# # # # #         ls.append(S)
       
# # # # #     return min(ls) 
# # # # # L=[[1,2,3,4],[2,3,4,5],[3,5,1,6]]
# # # # # sum=minsum(L)
# # # # # print("the sum",sum)


# # # # # print(15&22)
# # # # # print(15|22)
# # # # print(15&-22)
# # # # print(-15|22)
# # # # print(~15)
# # # # # n=int(input("upto"))
# # # # # s=0
# # # # # for i in range(1,n+1,1):
# # # # #     sum=1/(i+(i-1))
# # # # #     s+=sum
# # # # # Sum=1+s
# # # # # print(Sum)
# # # a=[1,2,3]
# # # b=[a,3]
# # # c=b[:]
# # # a[0]=7
# # # b[1]=2
# # # print(c)
# # # b=a
# # # b[0]=5
# # # print(a,b)
# i=0
# sum=0
# while i<9:
#     if i%4==0:
#         sum=sum+i
#     i=i+2
# print(sum)
# import io


# x=2
# print(x>>2)



# sum=0
# for i in range(0,9,2):
#     if i%4==0:
#         sum=sum+i
# print(sum)
# # l=[]
# # def c(b):
# #     if(b==0):
# #         return l
# #     d=b%2
# #     l.append(d)
# #     c(b//2)
# # c(6)
# # l.reverse()
# # for i in l:
# #     print(l)
# for i in range(1,10,3):
 
marks={1,2,3,4}
marks1=marks+{2}
print(marks1)