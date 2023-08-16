# c=bin(15)[2:]
# if len(c)==len("work"):
#     print("True")

# s=input()
# t=len(s)

# n = 4
# binary = format(n, 'b')
# print(binary) # Output: '100'
# binary = '10000001'
# decimal = int(binary, 2)
# print(decimal) #


#   SUB STRING

s=input()
n=len(s)
print(f"Substrings of {s} :")
for i in range(1,2**n):
    t=""
    c=bin(i)[2:].rjust(n,"0")
    for j in range(n):
        if c[j]=="1":
            t=t+s[j]
    print("\t\t",i,":",t)

