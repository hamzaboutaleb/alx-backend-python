#!/usr/bin/env python3
"""
Create an asyncio.Task to run the 'wait_random'
coroutine with the specified 'max_delay'
"""

import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int):
    """
    Create an asyncio.Task to run the 'wait_random'
    coroutine with the specified 'max_delay'.

    Args:
        max_delay: The maximum delay for the 'wait_random' coroutine.

    Returns:
        A task that represents the execution of 'wait_random'
        with the given 'max_delay'.
    """
    return asyncio.create_task(wait_random(max_delay))
