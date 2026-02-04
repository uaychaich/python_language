# def func1():
#     print("func1 naja")

# func1()
# func1()

#-------------------------------------------

# def func2():
#     return 5

# x=func2()
# print(x)

#-------------------------------------------

# def func3():
#     yield 1
#     yield 3
#     yield 5

# for x in func3():
#     print(x)

#-------------------------------------------

# def func4(x,y=3):
#     return x+y

# a = func4(5,7)
# print(a)
# a = func4(5)
# print(a)

#-------------------------------------------

# def func5(x:int,y:int=3)->int:
#     return x+y

# a = func5(5,7)
# print(a)

#-------------------------------------------

# def func6(x,*data):
#     print(f"x is {x}")
#     print(type(data))
#     for y in data:
#         print(y)

# func6('Uay',5,8,20,"Yoda")

#-------------------------------------------

# x=lambda x,y,z: f"{x} {y} {z}"
# print(x(5,7,"Yoda"))

#-------------------------------------------