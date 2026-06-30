"""Part A"""

import asyncio
import time

async def fetch_user():
    print("Fetching user")
    await asyncio.sleep(2)
    print("User fetched")
    return "User data"

async def fetch_orders():
    print("Fetching orders")
    await asyncio.sleep(1)
    print("Orders fetched")
    return "Orders data"

async def fetch_inventory():
    print("Fetching inventory")
    await asyncio.sleep(1.5)
    print("Inventory fetched")
    return "Inventory data"

async def main():
    start = time.time()
    result = await asyncio.gather(fetch_user(), fetch_orders(), fetch_inventory())
    end = time.time()
    print(f"Results: {result}")
    print(f"Total time: {end - start:.2f}s")

asyncio.run(main())