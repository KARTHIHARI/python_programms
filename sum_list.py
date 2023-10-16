from datetime import datetime
l1= [1,7,8,10]
l2= [5,-2,-1,3]
sum= 6

# for i in l1:
#     if sum-i in set(l2):
#         print(i,sum-i)
a=datetime.now()
print(a)
[print(i,j) for i in l1 for j in l2 if i+j==sum]
b=datetime.now()
print(b,"diff",abs(b-a))
for i in l1: 
    for j in l2:
        if i+j==sum:
            print(i,j)
c=datetime.now()
print(c,"diff",abs(c-b))




