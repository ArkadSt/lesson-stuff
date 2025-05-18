import time
import asyncio
import random


async def fact(n):
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

# fact(3) # 6
# print(fact(6)) # 6 (выводится на экран)


async def fib(n):
    if n <= 1:
        return n
    return await fib(n-1) + await fib(n-2)

async def measure (math_func, number):
    start = time.time()
    result = await math_func(number)
    end = time.time()
    print(f"Task completed in {end - start} seconds. Function: {math_func.__name__}, input: {number}, result: {result}")

async def main():
    tasks = [measure(fib, random.randint(0, 35)) for _ in range(100)]
    await asyncio.gather(*tasks)

asyncio.run(main())