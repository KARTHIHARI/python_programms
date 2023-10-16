
from collections import Counter
l=list()
n=int(input())
for i in range(n):
    l.append(input())
x=Counter(l)
# s=set(l)
# print(len(s))
for i in x.keys():
    print(x[i],end=" ")
print(x)
print(len(Counter(l)))