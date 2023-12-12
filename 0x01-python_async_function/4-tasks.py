#!/usr/bin/env python3
import asyncio
from typing import List
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int):
    """
    Run the wait_random coroutine 'n' times with the specified 'max_delay'.
    Args:
        n:  The number of times to run the wait_random coroutine
        max_delay: The maximum delay for each wait_random call.
    Returns:
        A list containing the delays for each completed wait_random call.
    """

    tasks = [await task_wait_random(max_delay) for _ in range(n)]
    result = await asyncio.gather(*tasks)
    return result
