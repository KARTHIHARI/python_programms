n=int(input())
g=n
for i in range(1,n+1):
    g=g-1
    print(" "*g,end="")
    print("#"*i)


# or


# [[print(("#"*i).rjust(j," ")) for i in range(1,j+1) ] for j in range(int(input()),0,-int(input())) ] 