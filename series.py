
#   1.FACTORIAL SERIES
import json
def fact(n):
    result={}
    f=1
    for i in range(n+1):
        if i==0:
            result["0!"]=1
        else:
            f*=i
            result[f"{i}!"]=f #(or)result[str(i)+"!"]
    return result

# 2.FIBONACCI SERIES
def fibbo(n):
    result={}
    f=0
    s=1
    for i in range(n):
        if i==0:
            result["1"]=0
        else:
            s=f+s
            f=s-f
            result[f"{i+1}"]=f
    return result

#   3.POWER SERIES
def powr(n):
    result={}
    for i in range(1,n+1):
        result[f"{i} power {i}"]=i**i
    return result

print("MENU")
print(" 1 for FACTORIAL SERIES")
print(" 2 for FIBONACCI SERIES")
print(" 3 for POWER SERIES")
print("give input:-")
n=int(input())
if n==1:
    print("ENTER THE LIMIT OF FACTORIAL SERIES:-")
    k=fact(int(input()))
    f=open("temp.json","w")
    s=json.dumps(k,indent=4)
    f.write(s)
    print(s)

elif n==2:
    print("ENTER THE LIMIT OF FIBONACCI SERIES:-")
    k=fibbo(int(input()))
    f=open("temp.json","w")
    s=json.dumps(k,indent=4)
    f.write(s)
    print(s)

elif n==3:
    print("ENTER THE LIMIT OF POWER SERIES:-")
    k=powr(int(input()))
    f=open("temp.json","w")
    s=json.dumps(k,indent=4)
    f.write(s)
    print(s)

else:
    print("ERROR 403")


# l=[8,1,12,16,-9,0,2,10,-3,-65]
# g=list()
# for i in range(len(l)):
#     if i==(len(l)-1):
#         break
#     g.append(abs(l[i]-l[i+1]))
# print(g)
# print(max(g))

# l=[8,1,12,16,-9,0,2,10,-3,-65]
# g=list()
# a=min(l)
# b=max(l)
# print(a,b,abs(a-b))
# for i in range(len(l)):
#     for j in range(1,len(l)):
#         g.append(abs(l[i]-l[j]))
# print(g)
# print(max(g))


#ODD SUM EVEN SUM
# l=[8,1,12,16,-9,0,2,10,-3,-65]
# esum=0
# osum=0
# for i in range(len(l)):
#     if i%2==0:
#         esum+=l[i]
#     else:
#         osum+=l[i]
# print("EVEN SUM=",esum)
# print("ODD SUM=",osum)
# #OR
# print(sum(l[0::2]),sum(l[1::2]))
# s = "The Internet is the single largest source of information and therefore it is important to know how to fetch data from various sources And with Wikipedia being one of the largest and most popular sources for information on the Internet Wikipedia is a multilingual online encyclopedia created and maintained as an open collaboration project by a community of volunteer editors using a wiki-based editing system In this article we will see how to use Python s Wikipedia module to fetch a variety of information from the Wikipedia website"
# p=s.upper()
# print(p)
# s=p.split()
# print(type(s))
# result={}
# for i in s:
#     if i not in result:
#         result[i]=1
#     else:
#         result[i]+=1
# print(result)