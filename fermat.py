import math
import random


def prime_test(N, k):
    return fermat(N, k), miller_rabin(N, k)


def mod_exp(x, y, N):
    if y == 0:
        return 1
    z = mod_exp(x, y // 2, N)
    if y % 2 == 0:
        return (z**2) % N
    else:
        return (x * z**2) % N
    # mod_exp requires 2 mods per iterations of y bit numbers, and one multiplication.
    # The runtime of mod_exp is O(y^3)


def fprobability(k):
    return 1 - (1/(2**k))
# Time complexity of fprobability is constant


def mprobability(k):
    return 1 - (1/(4**k))
# Time Complexity of mprobability is constant


def fermat(N, k):
    for i in range(k):
        a = random.randint(1, N - 1)
        if mod_exp(a, N - 1, N) != 1:
            return 'composite'
    return 'prime'
# Time Complexity of fermat is 0(N^3) because mod_exp is N^3, and fermat loops through k times
# k * N^3 = 0(N^3)


def miller_rabin(N, k):
    for i in range(0, k):
        a = random.randint(1, N - 1)
        n = N - 1
        templist = []
        while (n % 2) == 0:
            if (mod_exp(a, n, N)) != 1:
                templist.append(mod_exp(a, n, N))
            n = n // 2
        if templist:
            if templist[0] != N - 1:
                return 'composite'
    return 'prime'
# Time Complexity of miller_rabin is 0(N^4) because we call mod_exp N times
# N * N^3 = 0(N^4)
