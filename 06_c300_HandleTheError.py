# x=input('Dividend:')
# y=input('Divisor:')
# z=float(x)/float(y)
# print(z)

# -------------------------------------

# try:
#     x=input('Dividend:')
#     y=input('Divisor:')
#     z=float(x)/float(y)
#     print(z)
# except ValueError as e:
#     print('Diviend or Divisor is not a number.')
#     print(e.args)
# except ZeroDivisionError as e:
#     print('Divisor can not be a zero')
#     print(e.args)
# except Exception as e:
#     print('Something went wrong')
#     print(e.args)
# else:
#     print('No Error Here')
# finally:
#     print('End try')

# -------------------------------------

# import datetime

# def Year2Age(x):
#     if (int(x)>=1000 and int(x)<=9999):
#         return datetime.datetime.now().year - int(x)
#     else:
#         return

# birthyear = input("Please input your birth's year:")
# age = Year2Age(birthyear)
# print(f'Your age is {age}')
# -------------------------------------
    
# import datetime

# def Year2Age(x):
#     if (int(x)>=1000 and int(x)<=9999):
#         return datetime.datetime.now().year - int(x)
#     else:
#         raise ValueError("your birth year should be between 1000 and 9999")

# birthyear = input("Please input your birth's year:")
# age = Year2Age(birthyear)
# print(f'Your age is {age}')