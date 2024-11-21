import asyncio


async def start_strongman(name, power):
    print(f'Силач {name} начал соревнования')
    for i in range(1, 6):
        await asyncio.sleep(1 / power)
        print(f'Силач {name} поднял шар номер {i}')

    print(f'Силач {name} закончил соревнования.')


async def start_tournament():
    task_pasha = asyncio.create_task(start_strongman("Pasha", 3))
    task_denis = asyncio.create_task(start_strongman("Denis", 4))
    task_apollon = asyncio.create_task(start_strongman("Apollon", 5))

    await task_pasha
    await task_denis
    await task_apollon


if __name__ == "__main__":
    asyncio.run(start_tournament())
