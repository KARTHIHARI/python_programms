# import os

# # os.environ["test"]="ok"

# # print(os.environ)

# [print(i) for i in os.environ["Path"].split(";")]


n = int(input()) #This must me an odd number
c = 'H'


# #Top Pillars
# for i in range(n+1):
#     print((c*n).center(n*2)+(c*n).center(n*6))

# #Middle Belt
# for i in range((n+1)//2):
#     print((c*n*5).center(n*6)) 

# #Bottom Pillars
# for i in range(n+1):
#     print((c*n).center(n*2)+(c*n).center(n*6)) 
# 
for i in range(n):
    print(((c*(n-i-1)).rjust(n)+c+(c*(n-i-1)).ljust(n)).rjust(n*6)) 