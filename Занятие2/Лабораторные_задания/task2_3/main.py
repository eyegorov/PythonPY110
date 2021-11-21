from itertools import count

def pow_gen(base: int, step: float = 1.0)
    for i in count(0, step):
        yield base ** i
if __name__ == "__main__":
    pow_numbers = pow_gen(10, 0.2)

    for _ in range(5):
        print(next(pow_numbers))
