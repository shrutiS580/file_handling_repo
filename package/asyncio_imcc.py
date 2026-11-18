import asyncio

async def main():
    task = asyncio.create_task(fn2())

    print("one")
    print("four")

    await asyncio.sleep(3)
    print("five")

    await asyncio.sleep(1)


async def fn2():
    await asyncio.sleep(1)
    print("two")

    await asyncio.sleep(5)

asyncio.run(main())