# import datetime

# x=datetime.datetime(1980,5,25)
# print(x.day, x.isocalendar())

#----------------------------------------------

# class Person:
#     def __init__(self,name,salary=0):
#         self.name = name
#         self.salary=salary

# x=Person("Uaychai",500)
# y=Person("Yoda")
# print(x.name, x.salary)
# print(y.name, y.salary)
# y.salary=700
# print(y.name, y.salary)

#----------------------------------------------

# class Person:
#     numberofeye=2
#     def __init__(self,name,salary=0):
#         self.name = name
#         self.salary=salary

# x=Person("Uaychai",500)
# y=Person("Yoda")
# print(x.name, x.salary,x.numberofeye)
# print(y.name, y.salary,y.numberofeye)
# Person.numberofeye=3
# print(x.name, x.salary,x.numberofeye)
# print(y.name, y.salary,y.numberofeye)

#----------------------------------------------

# class Person:
#     numberofeye=2
#     def __init__(self,name,salary=0):
#         self.name = name
#         self.salary=salary

# x=Person("Uaychai",500)
# y=Person("Yoda")
# print(x.name, x.salary,x.numberofeye)
# print(y.name, y.salary,y.numberofeye)
# x.weight=60
# print(x.name, x.salary,x.numberofeye, x.weight)
# print(y.name, y.salary,y.numberofeye)

#----------------------------------------------

# class Person:
#     numberofeye=2
#     def __init__(self,name,salary=0):
#         self.name = name
#         self.salary=salary
    
#     def tax(self,taxrate):
#         return self.salary*taxrate

# x=Person("Uaychai",500)
# y=Person("Yoda")
# print(x.name, x.salary,x.numberofeye,x.tax(0.07))
# print(y.name, y.salary,y.numberofeye,y.tax(0.07))

#----------------------------------------------

# class Person:
#     numberofeye=2
#     def __init__(self,name,salary=0):
#         self.name = name
#         self.salary=salary
    
#     def tax(self,taxrate):
#         return self.salary*taxrate
    
#     def __str__(self):
#         return f"{self.name} {self.salary} naja"
    
#     def __eq__(self, value):
#         return self.salary== value

# x=Person("Uaychai",500)
# y=Person("Yoda")
# print(x.name, x.salary,x.numberofeye,x.tax(0.07))
# print(y.name, y.salary,y.numberofeye,y.tax(0.07))
# print(x,y)
# print(x==500)

#----------------------------------------------

# class Person:
#     numberofeye=2
#     def __init__(self,name,salary=0):
#         self.name = name
#         self.salary=salary
    
#     def tax(self,taxrate):
#         return self.salary*taxrate
    
#     def __str__(self):
#         return f"{self.name} {self.salary} naja"
    
#     def __eq__(self, value):
#         return self.salary== value

# class Employee(Person):
#     def __init__(self, name, salary=0, yearexp=0):
#         super().__init__(name, salary)
#         self.yearexp=yearexp

# x=Employee("Uay",500,3)
# print(x.name, x.salary, x.yearexp, x.tax(0.07))

#----------------------------------------------

# class UayClass:
#     def __init__(self,x,y,z):
#         self.publicprop=x
#         self._protecedprop=y 
#         self.__privateprop=z 
#     def publicmethod(self):return 1
#     def _protecedmethod(self):return 2
#     def __privatemethod(self):return 3

# class UaySubClass(UayClass):
#     def __init__(self, x, y, z):
#         super().__init__(x, y, z)

# a=UayClass(10,20,30)
# print(a.publicprop)
# print(a.publicmethod())
# print(a._protecedprop)
# print(a._protecedmethod())
# print(a.__privateprop)
# print(a.__privatemethod())

# b=UaySubClass(10,20,30)
# print(b.publicprop)
# print(b.publicmethod())
# print(b._protecedprop)
# print(b._protecedmethod())
# print(b.__privateprop)
# print(b.__privatemethod())

#----------------------------------------------

# class Outer:
#     def __init__(self):
#         self.name = 5
    
#     class Innter:
#         def __init__(self):
#             self.display =7

# x = Outer.Innter()
# print(x.display)

#----------------------------------------------