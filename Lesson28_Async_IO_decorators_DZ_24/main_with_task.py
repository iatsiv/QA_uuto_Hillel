import asyncio


async def show_massage():
    print(f"Нижче пораховано площу трикутника:")

def add_unit(unit):
    def decorator(func):
        async def wrapper(*args, **kwargs):
            result = await func(*args, **kwargs)
            return f"{result} {unit}"
        return wrapper
    return decorator

@add_unit("м^2")
async def calculate_triangle_area(base, height):
    area = 0.5 * base * height
    return area

async def main():
    async with asyncio.TaskGroup() as tg:
        task1 = tg.create_task(show_massage())
        task2 = tg.create_task(calculate_triangle_area(2, 5))
        await task1
        print(task2.result())

asyncio.run(main())
