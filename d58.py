import time
import asyncio


async def fun1():
    print('pop-corn kha liye')


async def fun2():
    await asyncio.sleep(5)
    print('episode dekh liya')


async def main():
    print(1)
    task1 = asyncio.create_task(fun1())
    print(2)
    await asyncio.sleep(1)
    task2 = asyncio.create_task(fun2())
    print(3)
    await task1
    print(4)
    await task2
    print(5)


t1 = time.time()
asyncio.run(main())
t2 = time.time()
print(t2-t1)
