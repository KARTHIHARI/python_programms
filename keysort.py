#key sort

a={"a":16,"k":6,"c":5}
def fun(y):
        return a[y]
b = sorted(a)
print(a,b)

#value sort
b=sorted(a,key=fun)
print(a,b)