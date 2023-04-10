'''1. Напишіть декоратор, який визначає час виконання функції.
Заміряйте час іиконання функцій з попереднього ДЗ'''

from time import monotonic_ns

from lib import stupid_calc
from lib import what_season

def time_func_decorator(func_to_decor):
    '''
    Measures the execution time of a function
    :param func_to_decor:
    :return: wrapped func_to_decor
    '''
    def wrapper(*args, **kwargs):
        start_time = monotonic_ns()
        func_to_decor(*args, **kwargs)
        end_time = monotonic_ns()
        total_time = end_time - start_time
        print(f'Function "{func_to_decor.__name__}" \
finished in {total_time} nanoseconds with result "{func_to_decor(*args)}"')

    return wrapper


what_season = time_func_decorator(what_season)
what_season('10.02')

stupid_calc = time_func_decorator(stupid_calc)
stupid_calc(2, 3, '/')