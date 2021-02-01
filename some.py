from functools import lru_cache


@lru_cache(maxsize=200)
def func(n):
    if n < 3:
        return n
    return func(n - 1) + func(n - 2)


if __name__ == '__main__':
    func(200)
