#!/usr/bin/env python3
import asyncio
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random

async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Run the wait_random coroutine 'n' times with the specified 'max_delay'.
    Args:
        n:  The number of times to run the wait_random coroutine
        max_delay: The maximum delay for each wait_random call.
    Returns:
        A list containing the delays for each completed wait_random call.
    """

    tasks = [asyncio.create_task(wait_random(max_delay)) for _ in range(n)]
    return tasks

