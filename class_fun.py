# class People:

#     def __init__(self,name):
#         self.name=
#         self.type="happy"

# p1=People("jake")
# print(p1.name,p1.type)


# class Pwr:
#     def __init__(self,number):
#         self.number=number
#         print("square:",number**2)
#         self.cube()

#     def cube(self):
#         print("cube:",self.number**3)


# n=int(input())
# p1=Pwr(n)
# print(p1)

# class Animal:
#     def __init__(self) -> None:
#         print("main")
#         super().__init__()
#     def about(self):
#         print("this is animal")
# class Cow(Animal):
#     def legs(self):
#         print("4 legs")
#     def food(self):
#         print("veg")

# class Dog(Animal):
#     def __init__(self) -> None:
#         print("dog")
#         super().__init__()
#     def legs(self):
#         print("4 legs")
#     def food(self):
#         print("non-veg")
#     def about(self):
#         print("hii")
#         super().about()

# class Pet(Dog):
#     def __init__(self,name) -> None:
#         print("pet")
#         super().__init__()

#     def about(self):
#         super().about()
        

# d=Pet()
# d.about()