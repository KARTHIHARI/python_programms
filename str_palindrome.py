# s=input("Enter String:")
# n=len(s)
# print(f"Substrings of {s} :")
# l=[]
# for i in range(1,2**n):
#     t=""
#     c=bin(i)[2:].rjust(n,"0")
#     for j in range(n):
#         if c[j]=="1":
#             t=t+s[j]
#             rs=t[::-1]
#             if t==rs:
#                 l.append(rs)
#     print("\t\t",i,":",t)
    
# # s=input("give string:")

# # rs=s[::-1]

# # print("normal:",s,"rev_string:",rs)
# print(l)
# mx=len(l[-1])
# mn=len(l[0])
# for i in l:
#     if mx<len(i):
#         mx=len(i)
#     elif mn>len(i)
# print("min:",1,"\n","max:",mx,"\n","difference:",mx-1)




# s=input("enter a string:")
# t=""
# l=[]
# for i in range(len(s)):
#     t=s[i]
#     print(t)
#     for j in range(1,len(s)):
#         if i<j:
#             t+=s[j]
#             rs=t[::-1]
#             print(t)
#             if rs==t:
#                 l.append(t)
# print(l)
# l=sorted(l)
# print(l)
# mx=len(l[-1])
# mn=len(l[0])
# for i in l:
#     if mx<len(i):
#         mx=len(i)
#     elif mn>len(i):
#         mn=len(i)
# print("min:",mn,"\n","max:",mx,"\n","difference:",abs(mx-mn))




s=input("enter a string:")
t=""
l=[]
k=[]
for i in range(len(s)):
    t=s[i]
    print(t)
    k.append(len(t))
    for j in range(1,len(s)):
        if i<j:
            t+=s[j]
            rs=t[::-1]
            print(t)
            if rs==t:
                l.append(t)
                k.append(len(t))
print(k)
k=sorted(k)
print(k)
mx=k[-1]
mn=k[-1]
for i in l:
    if mx<len(i):
        mn=mx
        mx=len(i)
    elif mn>len(i):
        mn=len(i)
print("min:",mn,"\n","max:",mx,"\n","difference:",abs(mx-mn))
