import asyncio


async def show_massage():
    print(f"Нижче пораховано площу фігури:")

def add_unit(unit):
    def decorator(func):
        async def wrapper(*args, **kwargs):
            result = await func(*args, **kwargs)
            return f"{result} {unit}"
        return wrapper
    return decorator

@add_unit("м^2")
async def calculate_triangle_area(base, height):
    await show_massage()
    area = 0.5 * base * height
    return area

print(asyncio.run(calculate_triangle_area(10, 5)))
