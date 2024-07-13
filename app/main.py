from core.utils import timer


@timer
def even_numbers_for_yield(n: int):
    for i in range(int(n / 2)):
        yield i * 2


@timer
def even_numbers_while_yield(n: int):
    i = 0
    while i < n:
        yield i
        i += 2


if __name__ == "__main__":
    limit = 10000000000000
    gen = even_numbers_for_yield(limit)
    gen = even_numbers_while_yield(limit)
    gen = even_numbers_comp(limit)
