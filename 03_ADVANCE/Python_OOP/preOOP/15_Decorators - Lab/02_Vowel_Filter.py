import functools


def vowel_filter(func):
    vowels = "aeioyu"

    @functools.wraps(func)
    def wrapper():
        return [i for i in func() if i in vowels]
    return wrapper


@vowel_filter
def get_letters():
    return ["a", "b", "c", "d", "e"]


print(get_letters())