import asyncio
async def greet():
    print("hello")
    await asyncio.sleep(5)
    print("welcome")
asyncio.run(greet())    