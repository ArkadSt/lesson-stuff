import asyncio
import time
async def task(id, n_seconds):
    start = time.time()
    await asyncio.sleep(n_seconds)
    end = time.time()
    print(f"Task {id} completed in {end - start} seconds")
    

async def main():
    await asyncio.gather(
        task(1, 5),
        task(2, 6)
    )

asyncio.run(main())

# 0! = 1
# 5! = 5*4*3*2*1
# 10! = 10 * 9 * 8!

