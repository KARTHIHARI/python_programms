import math

def prime(x):
    if x<3:
        return True
    for i in range(2,int(math.sqrt(x))+1):
        if x%i==0:
            return False
    return True
for i in range(1,25):
    if prime(i):
        print(i)
    # prime(i)
# print(prime(23))
