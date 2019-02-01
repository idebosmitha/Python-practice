primes = [2, 3, 5, 7, 11, 13, 17, 19, 23]

def get_sum(n, k, sum_=0):
    if k < 0:
        return False
    if sum_ > n:
        return False
    if n == sum_:
        return True
    for prime in primes:
        val = get_sum(n, k-1, sum_+prime)
        if val:
            return True
    return False


print(get_sum(10, 2))
print(get_sum(1, 6))
print(get_sum(60, 12))


def climb(n, i=0, path=''):
    if i > n:
        return
    if i == n:
        print(path)
    climb(n, i+1, path+'1 ')
    climb(n, i+2, path+'2 ')
