import subprocess
from typing import List
import asyncio

async def sleepFor(seconds:int)->str:
    return await subprocess.run(['sleep', str(seconds)])


def callCommands():
    print(asyncio.run(sleepFor(2)))
    print(asyncio.run(sleepFor(1)))

callCommands()