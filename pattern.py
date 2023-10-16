#CROSS

# n=int(input())
# for i in range(n):
#     for j in range(n):
#         if i+j==n-1:
#             print("*",end=" ")
#         elif i==j:
#             print("*",end=" ")

#         else:
#             print(" ",end=" ")
            
#     print()

# #RIT TRIANGLE
# n=int(input())
# for i in range(n):
#     for j in range(n):
#         if (i==n-1) :
#             print("*",end=" ")
#         elif j==n-1 :
#             print("*",end=" ")
#         elif i+j==n-1:
#             print("*",end=" ")
      
#         else:
#             print(" ",end=" ")
#     print()


#LFT Triangle with slash
# n=int(input())
# for i in range(n):
#     for j in range(n):
#         if (j==0) :
#             print("*",end=" ")
#         elif i==n-1 :
#             print("*",end=" ")
#         elif i+j==n-1:
#             print("*",end=" ")
#         elif i==j:
#             print("*",end=" ")
      
#         else:
#             print(" ",end=" ")
#     print()

#square with cross
# n=int(input())
# for i in range(n):
#     for j in range(n):
#         if (i==0) | (j==0) :
#             print("*",end=" ")
#         elif i==n-1 or j==n-1:
#             print("*",end=" ")
#         elif i+j==n-1:
#             print("*",end=" ")
#         elif i==j:
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")
#     print()


#Timeline
# n=int(input())
# for i in range(n):
#     for j in range(n):
#         if (i==0) :
#             print("*",end=" ")
#         elif i==n-1:
#             print("*",end=" ")
#         elif i+j==n-1:
#             print("*",end=" ")
#         elif i==j:
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")
#     print()

#SQUARE
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


