n=int(input())
for i in range(n):
    for j in range(n):
        if (i==0) | (j==0) :
            print("*",end=" ")
        elif i==n-1 or j==n-1:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()