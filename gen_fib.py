import functools


def fib_elem_gen():
    """Генератор, возвращающий элементы ряда Фибоначчи"""

    a = 0
    b = 1

    while True:
        yield a
        res = a + b
        a = b
        b = res

g = fib_elem_gen()

while True:
    el = next(g)
    if el > 10:
        break


def my_genn():
    """Сопрограмма"""
    number_of_fib_elem = yield

    while True:
        if type(number_of_fib_elem) == str:
            yield "Number of elements cannot be string"
            break
        elif type(number_of_fib_elem) == float:
            yield "Number of elements cannot be float"
            break
        elif number_of_fib_elem < 0:
            yield "Number of elements cannot be negative"
            break

        print(number_of_fib_elem)

        generator = fib_elem_gen()

        v = []

        for i in range(number_of_fib_elem):
            v.append(next(generator))

        l = [*v]  # example data
        number_of_fib_elem = yield l


def fib_coroutine(g):
    @functools.wraps(g)
    def inner(*args, **kwargs):
        gen = g(*args, **kwargs)
        gen.send(None)
        return gen
    return inner


my_genn = fib_coroutine(my_genn)
gen = my_genn()
print(gen.send(10))
print(gen.send(5))
print(gen.send(-5))