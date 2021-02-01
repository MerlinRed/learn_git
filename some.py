def fib(n):
    if n < 3:
        return n
    return fib(n - 1) + fib(n - 2)


if __name__ == '__main__':
    fib(10)
