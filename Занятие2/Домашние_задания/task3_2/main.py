def positive_check(fn):
    def wrapper(*args):
        if args != int():
            raise ValueError

        result = fn(*args)
        return result

    return wrapper

@positive_check
def some_func(*args):
    print(*args)
if __name__ == "__main__":
    print(some_func(1,2,3)) # всё хорошо
    print(some_func("r",5))  # должна быть вызвана ошибка ValueError
