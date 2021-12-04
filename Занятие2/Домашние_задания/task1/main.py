#progression = [start  * step ** (n - 1) for i in range (n)])




def mylist(n, a0, a1):
    for i in range(n):
        yield a0 + i*a1
my_generator = mylist(12,1,2)
print(next(my_generator))
print(next(my_generator))
print(next(my_generator))
print(next(my_generator))






