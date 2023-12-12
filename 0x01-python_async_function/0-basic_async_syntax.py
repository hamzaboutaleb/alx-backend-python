#!/usr/bin/env python3
"""asynchronous coroutine that takes in an integer argument
(max_delay, with a default value of 10) named wait_random that waits for a
random delay between 0 and max_delay (included and float value) seconds
and eventually returns it."""
import asyncio
import random
import time


async def wait_random(max_delay: int = 10) -> float:
    """wait_random
    Args:
      max_delay: max number of seconds to wait
    Returns:
      time function take to execute
    """
    start = time.time()
    rand = random.randint(0, max_delay)
    await asyncio.sleep(rand)
    end = time.time()
    return end - start

print(asyncio.run(wait_random()))
print(asyncio.run(wait_random(5)))
print(asyncio.run(wait_random(15)))
