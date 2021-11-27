def iter_check(some_object):
    def wrapper(*args, **kwargs):
        if (hasattr(some_object, '__iter__') and hasattr(some_object. __next__) and some_object.__iter__() is some_object):
            raise TypeError ("Объект <название или номер позиционного аргумента> <значение аргумента> не является итерируемым")
        result = some_object(*args,**kwargs)
        return result

if __name__ == "__main__":
    @iter_check
    def some_func(*args, **kwargs):
        print(*args, **kwargs)
    if __name__ == "__main__":
        print(some_func())
    pass

