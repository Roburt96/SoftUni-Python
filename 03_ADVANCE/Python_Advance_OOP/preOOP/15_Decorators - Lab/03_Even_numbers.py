import functools

def even_numbers(numbers):

    @functools.wraps(numbers)
    def wrapper(nums):
        x = [x for x in nums if x % 2 == 0]
        return x
    return wrapper


@even_numbers
def get_numbers(numbers):
    return numbers

print(get_numbers([1, 2, 3, 4, 5]))
