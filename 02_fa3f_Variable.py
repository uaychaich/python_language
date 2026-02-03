# a=None
# print(type(a),"a =", a)
# a="Uaychai said 'Let's python begin'"
# print(type(a),"a =", a)
# a=5
# print(type(a),"a =", a)
# a=5.23
# print(type(a),"a =", a)
# a=5+2j
# print(type(a),"a =", a)
# a=True
# print(type(a),"a =", a)

# -----------------------------------------

# a:int = 5
# print(type(a),"a =", a)
# a:int = "Luke"
# print(type(a),"a =", a)
# a="Yoda"
# print(type(a),"a =", a)

# -----------------------------------------

# a, b, c = 5, "Yoda", True
# print(type(a), type(b), type(c),"a =", a,"b =", b,"c =", c)

# -----------------------------------------

# a =[17,5,"Uaychai"]
# print(type(a), "a=", a, "a[0]=", a[0], "len(a)=", len(a))
# a =[17,5,31]
# print(type(a), "a=", a, "a[0]=", a[0], "len(a)=", len(a))
# a.append(25)
# print("a=", a, "len(a)=", len(a))
# print(a.pop(1))
# print("a=", a, "len(a)=", len(a))
# a.remove(31)
# print("a=", a, "len(a)=", len(a))
# a.insert(1,77)
# print("a=", a, "len(a)=", len(a))
# a[1]=88
# print("a=", a, "len(a)=", len(a))

# b=[17,5,[20,3]]
# print(type(b), "b=", b, "b[2]=", b[2], )

# -----------------------------------------

# a ={17,5,"Uaychai"}
# print(type(a), "a=", a, "len(a)=", len(a))
# a ={17,5,31}
# print(type(a), "a=", a, "len(a)=", len(a))
# a.add(77)
# print(type(a), "a=", a, "len(a)=", len(a))
# print(a.pop())
# print(type(a), "a=", a, "len(a)=", len(a))
# a.remove(31)
# print(type(a), "a=", a, "len(a)=", len(a))

# print(a[0])

# b={17,5,{20,3}}
# print(type(b), "b=", b)
# b={17,5,[20,3]}
# print(type(b), "b=", b)
# b={{17,5},{20,3}}
# print(type(b), "b=", b)

# -----------------------------------------

# a=(17,5,"Uaychai")
# print(type(a), "a=", a, "len(a)=", len(a))
# a=(17,5,31)
# print(type(a), "a=", a,"a[0]=", a[0], "len(a)=", len(a))
# a.index()

# a[0]=77
# print(type(a), "a=", a,"a[0]=", a[0], "len(a)=", len(a))

# b={(15,20,"Uaychai"),(17,55,"Yoda")}
# print(type(b), "b=", b, "len(b)=", len(b))

# c={(15,"Uaychai"),(17,55,"Yoda"),14}
# print(type(c), "c=", c, "len(c)=", len(c))

# d=[(15,20,"Uaychai"),(17,55,"Yoda")]
# print(type(d), "d=", d, "len(d)=", len(d))

# e=[(15,"Uaychai"),(17,55,"Yoda"),14]
# print(type(e), "e=", e, "len(e)=", len(e))

# -----------------------------------------

# a={"firstname":"Uaychai","age":25}
# print(type(a), "a=", a, "len(a)=", len(a), "a[firstname]=", a["firstname"], "a.keys=", a.keys(), "a.values=", a.values())
# print("a.keys=", a.keys(), "a.values=", a.values(), "a.items=", a.items())
# #print(a[0])

# a["salary"]=50
# print(type(a), "a=", a, "len(a)=", len(a), "a[firstname]=", a["firstname"], "a.keys=", a.keys(), "a.values=", a.values())
# a["firstname"]="UaychaiNaja"
# print(type(a), "a=", a, "len(a)=", len(a), "a[firstname]=", a["firstname"], "a.keys=", a.keys(), "a.values=", a.values())
# a.update({"age":30,"salary": 500})
# print(type(a), "a=", a, "len(a)=", len(a), "a[firstname]=", a["firstname"], "a.keys=", a.keys(), "a.values=", a.values())
# print(a.pop("age"))
# print(type(a), "a=", a, "len(a)=", len(a), "a[firstname]=", a["firstname"], "a.keys=", a.keys(), "a.values=", a.values())

# a["test1"]=(5,6,7)
# a["test2"]={5,6,7}
# a["test3"]=[5,6,7]
# print(type(a), "a=", a, "len(a)=", len(a), "a[firstname]=", a["firstname"], "a.keys=", a.keys(), "a.values=", a.values())

# -----------------------------------------

# a=int("25")
# print(type(a),"a=", a)
# b=set([25,27,26])
# print(type(b), "b=", b)
# c=tuple([25,27,26])
# print(type(c), "c=", c)
# d=tuple(b)
# print(type(d), "d=", d)
# e=set(d)
# print(type(e), "e=", e)

# -----------------------------------------

# import datetime
# x=datetime.datetime.now()
# print(x, x.day, x.month, x.year, x.hour, x.minute, x.second)
# y=datetime.date(1999,12,6)
# print(y, y.day, y.month, y.year)
# z=datetime.time(23,11,22)
# print(z, z.hour, z.minute, z.second)

# -----------------------------------------

# x=input("Please fill something:5")
# print(x, type(x))

# -----------------------------------------