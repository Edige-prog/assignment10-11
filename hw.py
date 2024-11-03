from functools import reduce
import time

# Exercise-1: First-class Function Operation
def operation(func, x: int, y: int) -> int:
    return func(x, y)

# Exercise-2: Implement Map Function
def my_map(func, my_list: list) -> list:
    return [func(item) for item in my_list]

# Exercise-3: Lambda Function with Filter
def filter_even_numbers(numbers: list) -> list:
    return list(filter(lambda x: x % 2 != 0, numbers))

# Exercise-4: Recursive Factorial
def recursive_factorial(n: int) -> int:
    if n <= 1:
        return 1
    else:
        return n * recursive_factorial(n - 1)

# Exercise-5: Decorator for Timing
def timeit_decorator(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"{func.__name__} took {end_time - start_time:.6f} seconds")
        return result
    return wrapper

# Exercise-6: Function Composition
def compose(*funcs):
    def composed_function(x):
        for func in funcs:
            x = func(x)
        return x
    return composed_function

# Exercise-7: Partial Application
def partial(func, *args):
    def partially_applied(*more_args):
        return func(*args, *more_args)
    return partially_applied

# Exercise-8: Reduce to Compute Factorial
def factorial_reduce(n: int) -> int:
    return reduce(lambda x, y: x * y, range(1, n + 1), 1)

# Exercise-9: Function Memoization
def memoize(func):
    cache = {}
    def memoized_function(*args):
        if args not in cache:
            cache[args] = func(*args)
        return cache[args]
    return memoized_function

# Exercise-10: Custom Reduce Function
def my_reduce(func, iterable, initializer=None):
    it = iter(iterable)
    if initializer is None:
        value = next(it)
    else:
        value = initializer
    for element in it:
        value = func(value, element)
    return value

# Exercise-11: Lambda Function Sort
def sort_by_last_letter(words: list) -> list:
    return sorted(words, key=lambda word: word[-1])

# Exercise-12: Recursive List Reversal
def recursive_reverse(my_list: list) -> list:
    if len(my_list) <= 1:
        return my_list
    else:
        return [my_list[-1]] + recursive_reverse(my_list[:-1])

# Exercise-13: Decorator for Function Counting
def count_calls(func):
    def wrapper(*args, **kwargs):
        wrapper.calls += 1
        print(f"'{func.__name__}' was called {wrapper.calls} times.")
        return func(*args, **kwargs)
    wrapper.calls = 0
    return wrapper

# Exercise-14: Use reduce to Find the Maximum Number
def find_max(numbers: list) -> int:
    return reduce(lambda x, y: x if x > y else y, numbers)

# Exercise-15: Use filter and lambda to Remove Elements
def remove_elements(my_list: list, element) -> list:
    return list(filter(lambda x: x != element, my_list))

# Exercise-16: Higher-Order Function for Repeats
def repeat(n: int):
    return lambda s: s * n

# Exercise-17: Recursive List Sum
def recursive_sum(my_list: list) -> int:
    if not my_list:
        return 0
    else:
        return my_list[0] + recursive_sum(my_list[1:])

# Exercise-18: Map with Multiple Lists
def add_two_lists(list1: list, list2: list) -> list:
    return list(map(lambda x, y: x + y, list1, list2))
