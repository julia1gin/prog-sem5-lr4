from gen_fib import my_genn

def test_fib_with_3():
    assert my_genn().send(3) == [0, 1, 1], "Тривиальный случай n = 3, список [0, 1, 1]"


def test_fib_with_5():
    assert my_genn().send(5) == [0, 1, 1, 2, 3], "Пять первых членов ряда"


def test_fib_empty_list():
    assert my_genn().send(0) == [], "Нет элементов"


def test_fib_with_more_than_11():
    assert my_genn().send(11) == [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55], "Больше чем 11 чисел"


def test_fib_with_negative():
    assert my_genn().send(-1) == "Number of elements cannot be negative"


def test_fib_with_string():
    assert my_genn().send('abc') == "Number of elements cannot be string"


def test_fib_with_float():
    assert my_genn().send(1.5) == "Number of elements cannot be float"