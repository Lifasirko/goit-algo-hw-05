def caching_fibonacci():
    cache = {}

    # print(cache)

    def fibonacci(nu):
        # print(0)
        if nu <= 0:
            # print(1)
            return 0
        elif nu == 1:
            # print(2)
            return 1
        elif nu in cache:
            # print(3)
            return cache[nu]

        cache[nu] = fibonacci(nu - 1) + fibonacci(nu - 2)
        return cache[nu]

    return fibonacci


fib = caching_fibonacci()

if __name__ == "__main__":
    print(fib(int(input("Введіть який номер числа послідовності Фібоначчі вас цікавить"))))
