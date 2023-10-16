# for i in range(10):
#     if i%2!=0:
#         continue
    # print(i)p
# a=[1,2,2.4,"hai",[1,2,3,[1,2,3]]]
# for i in range(len(a)):
#     print(a[i])
# for i in range (len(a)+10):
#     print(a)
#     a.pop()
#     a.remove(a[i])
#     a.append(i+1)
#     a.extend(a)
#     if len(a) ==20:
#         break
# a=dict(input())

# print(sorted(a))
# a={"a":1,"k":4,"c":5}
# print(sorted(a))


#min max
#a=[2,4,7,3,2,1,3,8,0]
# if a[0]<=a[-1]:
#     print("small no is :" ,a[0])
#     print("big no is :",a[-1])
# else:
#     print("error")
#or
# s=0
# mn =a[0]
# mx = a[0]
# for i in a:
#     if mn >i:
#         mn =i
#     if mx < i:
#         mx=i
#     s=s+i

# print("max:",mx,max(a))
# print("min:",mn,min(a))
# print("sum:",s,sum(a))
# a=[]
# for i in range(101):
#     a.append(i)
# print(len(a))
# num=[i for i in range(20)]
# num2=[i for i in range(20,30) ]

# a=[(i,j) for i in num for j in num2]
# print(a)



# # Python3 program introducing f-string
# val = 'Geeks'
# print(f"{val}for{val} is a portal for {val}.")

# import datetime
# name = 'Tushar'
# age = 23
# print(f"Hello, My name is {name} and I'm {age} years old.")
# today = datetime.datetime.today()
# print(f"{today:%B %d, %Y}")
# name='hariharasuthan'
# age=22
# city='rajapalayam'

# print(f'my name is  and my age is {age}.I am from {city}'
# print(f'hai { range(5)}')


# string formatting 1
# name="hai"
# age=1500000000
# s="{name},{age:,}".format(name='h',age=1500000000)
# print(s)

#FACTORIALS


# def fact(s):
#     s=s.replace("!","")
#     s=int(s)
#     print(s,type(s))
#     x=1
#     while s>1:
#         x=x*s
#         s=s-1
#     return x

# f=fact("8!")
# print(f)
# n = int(input())

# if (n%2)!=0 :
#     print("Weird")
# elif 2<=(n%2) and 5>=(n%2):
#     print("Not Weird")
# else:
#     print(" Notweird")





# n = int(input())
# for i in range(1,n+1):
#         print(i,end=" ")

# l=list()
# n=int(input())
# for i in range(n):
#     l.append(input())
# s=set(l)
# for i in l:
#     print(l.count(i))

# l=set(l)
# print(l.)



# divison mod
# import math
# i=int(input())
# n=int(input())
# print (divmod(i,n))

# # power mod
# a=int(input())
# p=int(input())
# m=int(input())
# print(pow(a,p))
# print(pow(a,p,m))

# x = int(input())
# y = int(input())
# z = int(input())
# n = int(input())
# # for i in range(n):
# #     for j in range(n):
# #         for k in range(n):
# #             print(i,j,k)
# a=[(i,j,k) for i in range(x+1) for j in range(y+1) for k in range(z+1) if (i+j+k)!=n]
# print(a)


# x = int(input())
# y = int(input())
# z = int(input())
# n = int(input())
# a=[[i,j,k] for i in range(x+1) for j in range(y+1) for k in range(z+1) if (i+j+k)!=n]
# print(a)

# l=list()
# n = int(input())
# for i in range(n):
#     l.append(input())
# mx=max(l[0],l[1])
# sec=min(l[0],l[1])
# for i in range(n):
#     if l[i]>mx:
#         sec=mx
#         mx=l[i]
#     elif l[i]>sec and l[i]!=mx:
#         sec=l[i]
#     elif mx==sec and l[i]!=sec:
#         sec=l[i]
# print(sec)

# l=list()
# n = int(input())
# for i in range(n):
#     l.append(input())
# mx=max(l[0],l[1])
# secmx=min(l[0],l[1])
# for i in range(n):
#     if l[i]>mx:
#         secmx=mx
#         mx=l[i]
#     elif l[i]>secmx and l[i]!=mx:
#         secmx=l[i]
#     elif mx==secmx and l[i]!=secmx:
#         secmx=l[i]
# print(secmx)


# n = int(input())
# l=list()
# l.__add__()
# mx=max(l[0],l[1])
# secmx=min(l[0],l[1])
# for i in range(n):
#     if l[i]>mx:
#         secmx=mx
#         mx=l[i]
#     elif l[i]>secmx and l[i]!=mx:
#         secmx=l[i]
#     elif mx==secmx and l[i]!=secmx:
#         secmx=l[i]
# print(secmx) 
    
# SPLIT
# def split(s,d=[]):
#     result=list()
#     temp=""
#     for i in s:
#         if i in d :
#             if temp!="":
#                 result.append(temp)
#                 temp=""
#             continue
#         temp+=i
#     if temp !="":
#         result.append(temp)
#     return result
# s="1 2 3 12/12/2000$"

# print(split(s,["/"]))

# SPLIT
# n=input()
# n=n.split()
# n=[int(n[i]) for i in range(len(n)) ]
# print(n)
# n=int(input())
# l=input()
# l=l.split()
# l=[int(l[i]) for i in range(n)]
# print(l)
# mx=max(l[0],l[1])
# secmx=min(l[0],l[1])
# for i in range(n):
#     if l[i]>mx:
#         secmx=mx
#         mx=l[i]
#     elif l[i]>secmx and l[i]!=mx:
#         secmx=l[i]
#     elif mx==secmx and l[i]!=secmx:
#         secmx=l[i]
# print(secmx)
# s=list()
# for i in range(int(input())):
#     name = input()
#     score = float(input())
#     a=[name,score]
#     s.append(a)
# mn=min(s[-1],s[-2])
# secmn=max()
# c=list()
# for i in range(len(s)):
#     if s[i]<mn:
#         secmn=mn
#         mn=s[i]
#     elif s[i]<secmn and s[i]!=mn:
#         secmn=s[i]
#     elif s[i]==secmn:
#         c=c.append(s[i])
#     elif secmn==mn and s[i]!=secmn:
#         secmn=s[i]
# print(secmn[0])
        
# def solve(students):
# #    min_mark = min(x[1] for x in students)
# #    students = [x for x in students if x[1] > min_mark]
#    min2_mark = min(x[1] for x in students)
#    students = sorted([x[0] for x in students if x[1] == min2_mark])
#    for x in students:
#       print(x)

# students = [['Amal',37],['Bimal',37],['Tarun',36],['Akash',41],['Himadri',39]]
# solve(students)

# def fun(stud):

#     mn=min(i[1] for i in stud)
#     stud=[i for i in stud if i[1]>mn]
#     mn2=min(i[1] for i in stud)
#     stud=sorted([i[0] for i in stud if i[1]==mn2 ])
#     for i in stud:
#         print(i)
# stud=list()
# for i in range(int(input())):
#     name = input()
#     score = float(input())
#     a=[name,score]
#     stud.append(a)
# print(stud)
# fun(stud)
# n=int(input())
# student={}
# for i in range(n):
#     name, *line = input().split()
#     scores = list(map(float, line))
#     student[name] = scores
# print(student)
# # for i in student.values():
# #     print(i)
# qname=input()
# if qname in student.keys():
#     l=student[qname]
#     avg=sum(l)/len(l)
# print(avg)

# def facto(n):
#     for i in range(n):    
#         if (i==0):
#             print(1)
#         else :
#             k=i
#             print(k)
# f=int(input())
# print(facto(f))




# ERROR HANDLING(EXCEPTION HANDLING)

# a="haiii"
# l=[1,2]
# try:
#     print(a+1)
#     for i in range(4):
#         print(i)
# except Exception as exc:
#     print("ERROR!!",type(exc))
#     print(exc)

#AMSTRONG NUMBER

# def ano(x):
#     n=list(map(int,str(x)))
#     s=0
#     for i in n:
#         s+=i**len(n)
#     return x==s
# # a=int(input())
# # print(ano(a))
# for g in range(1,10000):
#     if ano(g):
#         print(g)

#String Count

# a=input().strip()
# b=input().strip()
# c=len(a)
# d=len(b)
# count=0
# for i in range(0, c-d+1):
#     l = i
#     for j in range(0, d):
#         if a[l] == b[j]:
#             l+= 1
#             if j == d-1:
#                 count = count + 1
#             else:
#                 continue
#         else:
#             break
# print(count)
from datetime import datetime,timedelta
# print(datetime.today(),datetime.today()-timedelta(days=5))
# print(type(datetime.today()),type(datetime.now()))

# # s="23 6 21".split()
# print(datetime.now(),timedelta(days=100))
# for i in range(1,101):
#     a=(datetime.now()+timedelta(days=i)).strftime("%d %m %y")
#     print(a)
#SLEEP

# import time
# print(datetime.today())
# time.sleep(5)
# print(datetime.now())

# def solve(cost,tip,tax):
#     tp=cost/100*tip
#     tx=tax/100*cost
#     total=cost+tp+tx
#     print(int(total))

# meal_cost = float(input().strip())

# tip_percent = int(input().strip())

# tax_percent = int(input().strip())

# solve(meal_cost, tip_percent, tax_percent)




# import random
# l=list()
# j=10
# n=0
# while n<j:
#     a=random.randint(1,20)
#     if a in l:
#         continue
#     n+=1
#     l.append(a)
# c=0
# n=[]
# for i in range(j):
#     a=int(input())
#     n.append(a)
#     if a in l:
#         c+=1
# if c==0 :
#     print("Lose the game")
# else:
#     print("%.2f"%(c/j*100))

# print("List is:-",l)
# print("Your input is:-",n)



# from datetime import datetime,timedelta
# # print(datetime.now()-datetime(2001,12,31))

# for i in range(2001,2024):
#      print(datetime(i,12,31).strftime("%Y %m %A"))




# d=[False,False,True]
# result1=d[0]
# result2=d[0]
# for i in d:
#     result1 =not result1 & i #all function
#     result2 = result2 | i #any function
#     # print(not result1, not result2)
# print(result1,result2)
# print(all(d),any(d))




# class Color:
#     def __init__(self,clr):
#         self.clr=clr
    
# class Shape:
#     def __init__(self,side,radious):
#         self.side=side
#         self.radious=radious

# class Triangle(Shape,Color):
#     def __init__(self,side,clr):
#         super(Color,self).__init__(clr)
#         super(Shape,self).__init__(side)
#         # Shape.__init__(self,side,0)
#         # Color.__init__(self,clr)

#     def about(self):
#         print("color:",self.clr)
#         print("sides:",self.side)

#     def area(self):
#         print("area",self.side**2)

# class Circle(Shape,Color):
#     def __init__(self,radious,clr):
#         # super(Color,self).__init__(clr)
#         # super(Shape,self).__init__(side)
#         Shape.__init__(self,0,radious)
#         Color.__init__(self,clr)

#     def about(self):
#         print("color:",self.clr)
#         print("radious:",self.radious)

#     def area(self):
#         print("area",22/7*self.radious**2)

# c=Circle(3,"red")
# c.about()
# c.area()     #self is convert to Circle.area(c)

# n=int(input())
# for i in range(2,n):


    
        


#   SUB STRING

# s=input()
# w=[]
# f=[]
# g=[]
# l=[]
# t=""
# for i in range(len(s)):
#     t=s[i]
#     w.append(t)
#     if t==s[-1]:
#         break
#     else:
#         for j in range(1,len(s)):
#             if i<j:
#                 if s.count(s[j])>=t.count(s[j]):
#                     t+=s[j]
#                     w.append(t)
#                 for k in range(2,len(s)):
#                     if j<k:
#                         t+=s[k]
#                         p=s[i]+s[j]
#                         p=p+s[k]
#                         if p not in f:
#                             f.append(p)
#                         if t not in g:
#                             g.append(t)
#                     if f[j]==g[k]:
#                         f.remove(g[k])
#                 t=s[i]
# print(w)
# print(g,f,w)

# print(f,g,w)






#PRIME NUMBER ADDITION

# import math

# def prime(x):
#     if x<3:
#         return True
#     for i in range(2,int(math.sqrt(x))+1):
#         if x%i==0:
#             return False
#     return True
# # for i in range(2,25):
# #     if prime(i):
# #         print(i)
# #     prime(i)
# n=int(input())
# h=n
# l=[]
# d=[]
# for i in range(1,n+1):
#     if prime(i):
#         l.append(i)
# for i in range(len(l)-1,-1,-1):
#     p=h-l[i]
#     if p in l:
#         if l[i] not in d:
#             d.append(l[i])
#         if p not in d:
#             d.append(p)
#         h=p
#     elif p-l[i] in l:
#         if p not in d:
#             d.append(p-l[i])
#         if l[i] not in d:
#             d.append(l[i])
#         h=p
#     elif sum(d)>=n:
#         if sum(d)>n:
#             sm=sum(d)-n
#             if sm in d:
#                 d.remove(sm)
#                 break
#         else:
#             break
    

# print(d)
# print(sum(d))


#PRIME NUMBER ADDITION SERIES

# import math

# def prime(x):
#     if x<3:
#         return True
#     for i in range(2,int(math.sqrt(x))+1):
#         if x%i==0:
#             return False
#     return True
# # for i in range(2,25):
# #     if prime(i):
# #         print(i)
# #     prime(i)
# print("start range:")
# s=int(input())
# print("end range:")
# e=int(input())
# for j in range(s,e+1):
#     h=j
#     l=[]
#     d=[]
#     for i in range(1,j+1):
#         if prime(i):
#             l.append(i)
#     for i in range(len(l)-1,-1,-1):
#         p=h-l[i]
#         if p in l:
#             if l[i] not in d:
#                 d.append(l[i])
#             if p not in d:
#                 d.append(p)
#             h=p
#         elif p-l[i] in l:
#             if p-l[i] not in d:
#                 d.append(p-l[i])
#             if l[i] not in d:
#                 d.append(l[i])
#             h=p
#         elif sum(d)>=j:
#             if sum(d)>j:
#                 sm=sum(d)-j
#                 if sm in d:
#                     d.remove(sm)
#                     break
#             else:
#                 break
        

#     print(sum(d))
#     print(d)


