# import asyncio

# async def main():
#     await asyncio.sleep(5)
#     print("main success")

# asyncio.run(main())

#---------------------------------------------

# import asyncio
# import datetime

# async def work(second:int,text:str):
#     await asyncio.sleep(second)
#     print(text)

# async def main():
#     print("main success")
#     print(f"Begin at {datetime.datetime.now()}")
#     await work(10,"Work 1 Success")
#     await work(5,"Work 2 Success")
#     print(f"End at {datetime.datetime.now()}")

# asyncio.run(main())

#---------------------------------------------

# import asyncio
# import datetime

# async def work(second:int,text:str):
#     await asyncio.sleep(second)
#     print(text)

# async def main():
#     print(f"Begin at {datetime.datetime.now()}")
#     await work(10,"Work 1 Success")
#     await work(5,"Work 2 Success")
#     print(f"End at {datetime.datetime.now()}")

# asyncio.run(main())

#---------------------------------------------

# import asyncio
# import datetime

# async def work(second:int,text:str):
#     await asyncio.sleep(second)
#     print(text)

# async def main():
#     print(f"Begin at {datetime.datetime.now()}")
#     task1 = asyncio.create_task( work(10,"Work 1 Success"))
#     task2 = asyncio.create_task( work(5,"Work 2 Success"))
#     print('do something')
#     await task1
#     await task2
#     print(f"End at {datetime.datetime.now()}")

# asyncio.run(main())

#---------------------------------------------

# import asyncio
# import datetime

# async def work(second:int,text:str):
#     await asyncio.sleep(second)
#     return f"{text} is finished at {datetime.datetime.now()}"

# async def main():
#     print(f"Begin at {datetime.datetime.now()}")
#     task1 = asyncio.create_task( work(10,"Work 1"))
#     task2 = asyncio.create_task( work(5,"Work 2"))
#     print('do something')
#     result1 =await task1
#     result2 =await task2
#     print(result1)
#     print(result2)
#     print(f"End at {datetime.datetime.now()}")

# asyncio.run(main())

#---------------------------------------------

# import asyncio
# import datetime

# async def work(second:int,text:str)->str:
#     await asyncio.sleep(second)
#     return f"{text} is finished at {datetime.datetime.now()}"

# async def main():
#     print(f"Begin at {datetime.datetime.now()}")
#     task1 = asyncio.create_task( work(10,"Work 1"))
#     task2 = asyncio.create_task( work(5,"Work 2"))
#     print('do something')
#     result = await asyncio.gather(task1,task2)
#     print(result[0])
#     print(result[1])
#     print(f"End at {datetime.datetime.now()}")

# asyncio.run(main())

#---------------------------------------------