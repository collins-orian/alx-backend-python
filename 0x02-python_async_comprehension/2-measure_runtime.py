#!/usr/bin/env python3

'''
Import async_comprehension from the previous file and write a
measure_runtime coroutine that will execute async_comprehension
four times in parallel using asyncio.gather. measure_runtime
should measure the total runtime and return it. Notice that
the total runtime is roughly 10 seconds, explain it to yourself.
'''

import time
import asyncio
from importlib import import_module as using

async_comprehension = using('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    '''Executes async_comprehension 4 times and measures the
    total execution time.
    '''
    start = time.perf_counter()
    await asyncio.gather(*(async_comprehension() for _ in range(4)))
    end = time.perf_counter()
    return end - start
