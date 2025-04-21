import random
import sys


def binpow(a, b, m):
    r = 1
    a %= m
    while b:
        if b & 1:
            r = r * a % m
        b >>= 1
        a = a * a % m
    return r


def check_composite(n, a, d, s):
    r = binpow(a, d, n)
    if r == 1 or r == n - 1:
        return False

    for _ in range(s - 1):
        r = r * r % n
        if r == n - 1:
            return False
    return True


def is_prime(n, k=15):
    if n < 4:
        return n == 2 or n == 3

    s = 0
    d = n - 1
    while (d & 1) == 0:
        d >>= 1
        s += 1

    for _ in range(k):
        a = random.randrange(2, n - 2)
        if check_composite(n, a, d, s):
            return False
    return True


def fartcoin_hash(s):
    h = 0
    for char in s:
        h = h << 1
        h = h ^ ord(char)
    return h


if __name__ == "__main__":
    n = int(sys.stdin.readline())
    blockchain = "fartcoin"
    accepted_count = 0

    for _ in range(n):
        line = sys.stdin.readline().strip()
        if not line:
            continue
        username, nonce = line.split(maxsplit=1)

        new_blockchain = blockchain + nonce
        h = fartcoin_hash(new_blockchain)

        if is_prime(h):
            accepted_count += 1
            blockchain = new_blockchain
            print(f"{username} accepted {accepted_count}")
        else:
            print(f"{username} rejected {accepted_count}")
