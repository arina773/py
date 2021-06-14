def big_fibonacci(n):
    f_1 = 1
    f_2 = 1
    f_next = 1
    while len(str(f_next)) != n:
        f_next = f_1 + f_2
        f_1 = f_2
        f_2 = f_next
    return f_next
