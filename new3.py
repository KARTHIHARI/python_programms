class temp:
    def __init__(self,x) -> None:
        self.x=x
    def display(self,h):
        self.h=h
        print(self.x,self.h)

    def ex(self,g):
        self.g=g

t=temp(10)
# t.display(160)
# print("X:",t.x)

temp.display(t,160)
temp.ex(t,80)
print("h:",t.x,t.h,t.g)


