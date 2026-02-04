# import pathlib
# print(__file__)
# print(pathlib.Path(__file__).parent)

# -----------------------------------------------

# import pathlib

# x=open(f'{pathlib.Path(__file__).parent}\\data.txt','rt', encoding='utf-8')
# y=x.read()
# print(y)
# x.seek(0)
# y=x.readlines()
# print(y)
# x.close()

# -----------------------------------------------

# import pathlib

# x=open(f'{pathlib.Path(__file__).parent}\\data.txt','at', encoding='utf-8')
# x.write("\nHi Wade")
# x.close

# x=open(f'{pathlib.Path(__file__).parent}\\data.txt','rt', encoding='utf-8')
# y=x.read()
# print(y)
# x.close()

# -----------------------------------------------

# import pathlib

# x=open(f'{pathlib.Path(__file__).parent}\\data2.txt','xt', encoding='utf-8')
# x.write("\nHi Wade")
# x.close

# x=open(f'{pathlib.Path(__file__).parent}\\data2.txt','rt', encoding='utf-8')
# y=x.read()
# print(y)
# x.close()

# -----------------------------------------------

# import pathlib

# with open(f'{pathlib.Path(__file__).parent}\\data.txt','rt', encoding='utf-8') as x:
#     y=x.read()
#     print(y)
#     x.seek(0)
#     y=x.readlines()
#     print(y)

# -----------------------------------------------

# import pathlib
# import csv

# with open(f'{pathlib.Path(__file__).parent}\\data.csv','rt', encoding='utf-8',newline='\n') as x:
#     y=csv.reader(x,delimiter=',')
#     for z in y:
#         print(z)

# -----------------------------------------------

# import pathlib
# import csv

# with open(f'{pathlib.Path(__file__).parent}\\data.csv','at', encoding='utf-8',newline='\n') as x:
#     y=csv.writer(x,delimiter=',',doublequote=False)
#     y.writerow(['Clair','Redlight',40])