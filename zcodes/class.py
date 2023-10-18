"""
Coroutine is a wrapped version of a function that allows it to run asynchronously,
help us to allowing execution to be suspended and resumed
"""


import asyncio
import time

"""
async => tells python to create a wrapper around this function, so when you call this function, it will actually return a coroutine object,
         this coroutine object is just like a function, and it can be executed, and to execute a coroutine you need to await its execution.
"""
async def main():
    print('start')
    task = asyncio.create_task(foo("foo starts"))   # asyncio.create_task, tells asyncio to start executing foo as soon as it possibly can, and to allow other code to run while foo is not running
                                                    # while this task is getting created main is still running
    await asyncio.sleep(2)  # jab ye asyncio.sleep hua tab he foo chalega
    # await task  , jab tak task nahi ho jata ruka rahega
    print('end')
    await asyncio.sleep(2)
    


"""
await main() => to use await keyword, it must be inside a asynchronous function. 
"""

async def foo(txt):
    print(txt)
    await asyncio.sleep(3)   # asyncio.sleep returns a coroutine, we have to await that coroutine, to make it run
    print("foo ends")



asyncio.run(main())  # asyncio.run take a coroutine and this coroutine is going to be the entry point to our program.
                     # asyncio.run is creating the event loop adding main() to that, that's what allowing us to actually run main()



