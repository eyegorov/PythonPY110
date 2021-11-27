if __name__ == "__main__":
    def my_list(n, a0, a1):
        for i in range(n):
            yield a0 + i * a1
    pass

     print(my_list(1,2,3))