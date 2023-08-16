#INFINITY
n=int(input())
for i in range(n):
    for j in range(n):
        if (j==0) :
            print("*",end=" ")
        elif j==n-1:
            print("*",end=" ")
        elif i+j==n-1:
            print("*",end=" ")
        elif i==j:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()