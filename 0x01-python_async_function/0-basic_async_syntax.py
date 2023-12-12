#!/usr/bin/env python3
import asyncio
import random
import time


async def wait_random(max_delay: int = 10) -> float:
    start = time.time
    rand = random.randint(0, max_delay)
    await asyncio.sleep(rand)
    end = time.time
    return end - start
