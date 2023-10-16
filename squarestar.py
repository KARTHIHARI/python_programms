n=int(input())
c=""
for i in range(1,n+1):
    c+=str(i) #c=c+str(i)
print(c+c)
for i in range(1,n):
    print(c[:-i:].ljust(n)+c[i::].rjust(n))
for i in range(1,n+1):
    print(c[:i:].ljust(n)+c[-i::].rjust(n))
 