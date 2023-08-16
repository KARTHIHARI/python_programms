# def table(x):
#     def value(y):
#         print(f"{x}x{y}={x*y}")
#     return value
# print("table.no:")
# n=int(input())
# print("which no.:")
# i=int(input())
# f=table(n)
# f(i)


def dec(fun):
    def haii(*args,**kargs):
        print("****")
        fun(*args,**kargs)
        print("****")
    return haii

def dec2(fun):
    def haii(*args,**kargs):
        print("%%%%%")
        fun(*args,**kargs)
        print("%%%%%")
    return haii
@dec2
@dec   #hi=dec(hi)
def hi():
    print("hello")

# hi=dec(hi)

# hi=dec(hi)
# hi=dec2(hi)
hi()

