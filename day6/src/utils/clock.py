import asyncio
import time

async def create_clock():
    while True:
        print(time.strftime("%H:%M:%S", time.localtime()))
        """
        pauses the execution of the function for 1 second, allowing other tasks to run concurrently if needed.
        this is useful in an asynchronous context to prevent blocking the event loop, allowing other tasks to execute while waiting for the next clock update.
        """
        await asyncio.sleep(1)

if __name__ == "__main__":
    asyncio.run(create_clock())