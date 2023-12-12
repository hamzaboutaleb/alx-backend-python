#!/usr/bin/env python3
"""Measure the total time taken to execute 'wait_n' coroutine 'n'
times with the specified 'max_delay'."""

import asyncio
from typing import List
import time
wait_n = __import__('1-concurrent_coroutines').wait_n


async def measure_time(n: int, max_delay: int = 10) -> float:
    """Measure the total time taken to execute 'wait_n' coroutine 'n'
    times with the specified 'max_delay'.
    Args:
        n: The number of times to run the 'wait_n' coroutine.
        max_delay: The maximum delay for each 'wait_random' call.
    Returns:
        The total time taken to execute all 'wait_n' calls in seconds.
    """
    start = time.time()
    await wait_n(n, max_delay)
    end = time.time()

    return (end - start) / n
