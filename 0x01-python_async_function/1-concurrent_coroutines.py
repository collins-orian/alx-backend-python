#!/usr/bin/env python3


'''Import wait_random from the previous python file that you’ve written
and write an async routine called wait_n that takes in 2 int arguments
(in this order): n and max_delay. You will spawn wait_random n times with
the specified max_delay. wait_n should return the list of all the delays
(float values). The list of the delays should be in ascending order without
using sort() because of concurrency.'''

from typing import List


wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    '''Execute wait_random n times'''
    delays = []
    for i in range(n):
        delay = await wait_random(max_delay)
        delays.append(delay)
    return sorted(delays)

"""Another way of handling this task is to use the asyncio.gather() within
the asyncio module function as follows:


async def wait_n(n: int, max_delay: int) -> List[float]:
    '''Executes wait_random n times.
    '''
    wait_times = await asyncio.gather(
        *tuple(map(lambda _: wait_random(max_delay), range(n)))
    )
    return sorted(wait_times)
"""
