def positive_check(fn):
    def wrapper(arg):
        if arg < 0:
            raise ValueError

        result = fn(arg)
        return result

    return wrapper


@positive_check
def some_func(num: int):
    print(num)


if __name__ == "__main__":
    some_func(5)  # всё хорошо

    some_func(-5)  # должна быть вызвана ошибка ValueError
