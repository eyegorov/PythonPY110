def min_len_check(fn):
    def wrapper(str_arg):
        if len(str) < 10:
            raise ValueError
        return fn(str)
    return wrapper


@min_len_check
def some_func(str_arg: str):
    ...


if __name__ == "__main__":
    some_func("Hello, World!!!")  # всё хорошо

    some_func("Short str")  # ValueError("Строка слишком короткая")
