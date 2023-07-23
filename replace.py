# def replaceVowels(s):
#     vowels = "aeiouAEIOU"
#     l = list(s)
#     for i in range(len(l)):
#         if l[i] not in vowels:
#             l[i] = '#'
#     s_p = "".join(l)
#     # del l
#     return (s_p)
# s=input("enter:")
# print(replaceVowels(s))
def fun(s):
    for i in s:
        if i not in"aeiou":
            s=s.replace(i,"*")
            
    return s
s="aastha"
print(fun(s))