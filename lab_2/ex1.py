import random
from typing import List, Tuple


def generate_prime() -> int:
    prime = random.randint(2 ** 10, 2 ** 12)
    while not is_prime(prime):
        prime = random.randint(2 ** 10, 2 ** 12)
    return prime


def is_prime(n: int) -> int:
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True


def gcd(a: int, b: int) -> int:
    while b != 0:
        a, b = b, a % b
    return a


def mod_inverse(a: int, m: int) -> int:
    m0, x0, x1 = m, 0, 1
    while a > 1:
        q = a // m
        m, a = a % m, m
        x0, x1 = x1 - q * x0, x0
    return x1 + m0 if x1 < 0 else x1


def encrypt(content: bytes, e: int, n: int) -> List[int]:
    return [pow(byte, e, n) for byte in content]


def decrypt(content: List[int], d: int, n: int) -> bytes:
    return bytes([pow(byte, d, n) for byte in content])


def generate_rsa_keys() -> Tuple[Tuple[int, int], Tuple[int, int]]:
    p = generate_prime()
    q = generate_prime()
    n = p * q
    phi = (p - 1) * (q - 1)
    e = random.randint(1, phi)
    while gcd(e, phi) != 1:
        e = random.randint(1, phi)
    d = mod_inverse(e, phi)
    return (e, n), (d, n)


def main():
    public_key, private_key = generate_rsa_keys()
    print("Public Key:", public_key)
    print("Private key:", private_key)
    with open('files/input', 'rb') as f:
        data = f.read()

    encrypted_data = encrypt(data, public_key[0], public_key[1])

    with open('files/encrypted', 'wb') as f:
        for byte in encrypted_data:
            f.write(byte.to_bytes(4, byteorder='big'))

    decrypted_data = decrypt(encrypted_data, private_key[0], private_key[1])

    with open('files/decrypted', 'wb') as f:
        f.write(decrypted_data)

    with open('files/input', 'rb') as f:
        original_data = f.read()

    with open('files/decrypted', 'rb') as f:
        decrypted_data = f.read()

    if original_data == decrypted_data:
        print("Encrypted and Decrypted are equals")
    else:
        print("Encrypted and Decrypted are not equals")


if __name__ == "__main__":
    main()
