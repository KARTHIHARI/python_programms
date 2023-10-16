def gen():
    f=0
    s=1
    while True:
        yield f
        s=f+s
        f=s-f



g=gen()
print(g)
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))