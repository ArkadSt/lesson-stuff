import asyncio

async def prepare_pizza():
    print("Preparing pizza")
    await asyncio.sleep(3)
    print("Pizza prepared")

async def deliver_pizza():
    print("Staring delivery")
    await asyncio.sleep(5)
    print("Pizza delivered")


async def order_pizza():
    await prepare_pizza()
    await deliver_pizza()

asyncio.run(order_pizza())
