import sys
import numpy as np

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
    
    for _ in range (s - 1):
        r = r * r % n
        if r == n - 1:
            return False
    return True

def is_prime(n, k = 5):
    if n < 4:
        return n == 2 or n == 3
    
    s = 0
    d = n - 1
    while (d & 1) == 0:
        d >>= 1
        s += 1

    for _ in range(k):
        a = np.random.randint(2, n - 2)
        if check_composite(n, a, d, s):
            return False
    return True

def fartcoin_hash(s):
    h = 0
    for char in s:
        h = h << 1
        h = h ^ ord(char)
    return h

def fnv1a_hash(data):
    """
    Implements the FNV-1a hash algorithm for strings.
    
    Args:
        data: The input string to hash
        
    Returns:
        The 32-bit FNV-1a hash value as an integer
    """
    # FNV constants for 32-bit hash
    FNV_PRIME = 16777619
    OFFSET_BASIS = 2166136261
    
    # Initialize hash with offset basis
    hash_value = OFFSET_BASIS
    
    # Process each byte in the input string
    for byte in data.encode('utf-8'):
        # XOR the current byte with the hash
        hash_value ^= byte
        # Multiply by the FNV prime
        hash_value *= FNV_PRIME
        # Keep only 32 bits
        hash_value &= 0xFFFFFFFF
        
    return hash_value


if __name__ == "__main__":
    n = int(sys.stdin.readline())
    blockchain = "fartcoin"
    accepted_count = 0

    for _ in range(n):
        line = sys.stdin.readline().strip()
        if not line:
            continue
        username, nonce = line.split(maxsplit=1)

        if len(nonce) < 5:
            print(f"{username} rejected {accepted_count}")
            continue
            
        new_blockchain = blockchain + nonce
        h = fartcoin_hash(new_blockchain)
        #h = fnv1a_hash(new_blockchain)



        if is_prime(h):
            accepted_count += 1
            blockchain = new_blockchain
            print(f"{username} accepted {accepted_count}")
        else:
            print(f"{username} rejected {accepted_count}")
