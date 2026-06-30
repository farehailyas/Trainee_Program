import asyncio 
async def tea():
    print("started making tea")
    await asyncio.sleep(3)
    print("tea done")

async def toast():
    print("start making toast")
    await asyncio.sleep(1)
    print("end making toast") 

async def main():
    await asyncio.gather(tea() , toast())

asyncio.run(main())
#gether run these functions parallel

