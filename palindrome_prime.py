def is_prime(n, i=2):
    if n <= 1:
        return False
    elif (n % i == 0):
        return False
    elif (i * i > n):
        return True
    return is_prime(n, i + 1)

l_ = []
for i in range(10000, 99999):
    if is_prime(i) and str(i) == str(i)[::-1]:
        l_.append(i)
print(l_)
