def is_prime(n, i=2):
    if n <= 1:
        return False
    elif (n % i == 0):
        return False
    elif (i * i > n):
        return True
    return is_prime(n, i + 1)
