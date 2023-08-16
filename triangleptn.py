#kite
print("Enter Odd Number Only:")
n=int(input())
for i in range(n):
    for j in range(n):
        if(i+j==n//2) or (i==n//2) or (j-i==n//2) :
             print("*",end=" ")
        elif (j==n//2) or (i-j==n//2) or (i-j==0) or (i+j==n-1) or (i+j==n+(n//2)-1):
             print("*",end=" ")
        else:
           print(" ", end=" ")
        
    print()