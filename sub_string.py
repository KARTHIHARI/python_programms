    
# SUB SEQUAL

s=input()
t=""
l=[]
for i in range(len(s)):
    t=s[i]
    print(t)
    for j in range(1,len(s)):
        if i<j:
            t+=s[j]
            rs=t[::-1]
            print(t)
            if rs==t:
                l.append(t)

                #(OR)
for i in range(len(s)+1):
    for j in range(i+1,len(s)+1):
        print(s[i:j])

print(l)
# s=input()
# for i in range(0,len(s)+1):
#     print(s[i:len(s)+1])


