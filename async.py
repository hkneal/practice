import asyncio

async def waiter(event):
    print('Waiting for the event to be set...')
    await event.wait()
    print('Event is set, proceeding!')

async def setter(event):
    await asyncio.sleep(2)
    print('Setting the event...')
    event.set()

async def main():
    event = asyncio.Event()

    # Create tasks for waiter and setter coroutines
    waiter_task = asyncio.create_task(waiter(event))
    setter_task = asyncio.create_task(setter(event))

    # Gather and run the tasks concurrently
    await asyncio.gather(waiter_task, setter_task)

if __name__ == "__main__":
    asyncio.run(main())