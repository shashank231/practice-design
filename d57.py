import asyncio

# fun1 is a coroutine now, as we put async
async def fun1():
    print('started')
    return 5

# To execute a coroutine, we need an event loop, asyncio.run automatically
# creates this event loop for us
a = asyncio.run(fun1())

print(a)