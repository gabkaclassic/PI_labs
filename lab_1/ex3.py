from typing import List

EMPTY_CHAR = b'z'


def read_key(key_path: str) -> List[int]:
    try:
        with open(key_path, 'rb') as file:
            key = file.read().strip().decode('utf-8')
        return [int(x) for x in key.split()]
    except FileNotFoundError:
        print('Key file not found')


def pad_data(data: bytes, block_size: int) -> bytes:
    padding_length = block_size - len(data) % block_size
    if padding_length == block_size:
        return data
    else:
        return data + bytes([padding_length] * padding_length)


def encrypt(data: bytes, key: List[int]) -> bytes:
    block_size = len(key)
    encrypted_content = bytearray()

    padding = block_size - len(data) % block_size
    data += EMPTY_CHAR * padding

    # Переставляем столбцы в соответствии с ключом
    for col in key:
        for i in range(col - 1, len(data), block_size):
            encrypted_content.append(data[i])

    return encrypted_content


def decrypt(data: bytes, key: List[int]) -> bytes:
    block_size = len(key)
    decrypted_content = bytearray()

    for i in range(len(data) // block_size):
        for col in key:
            decrypted_content.append(data[i + (col - 1) * (len(data) // block_size)])

    return decrypted_content.rstrip(EMPTY_CHAR)


def process_file(input_path: str, output_path: str, key_path: str, mode: str):
    key = read_key(key_path)
    try:
        with open(input_path, 'rb') as f:
            data = f.read()
    except FileNotFoundError:
        print('Input file not found')
    if mode == 'encrypt' or mode == 'e':
        data = pad_data(data, len(key))
        processed_data = encrypt(data, key)
    elif mode == 'decrypt' or mode == 'd':
        processed_data = decrypt(data, key)
    else:
        print('Invalid mode')
        exit(1)
    try:
        with open(output_path, 'wb') as f:
            f.write(processed_data)
    except Exception as e:
        print(f'File writing error: {e}')


input_file = 'files/test.doc'  # input('From: ')
output_file = 'files/encrypted'  # input('To: ')
key_filename = 'files/key.txt'  # input('Key file path: ')
mode = 'e'  # input('Mode: ').lower()
process_file(input_file, output_file, key_filename, mode)

input_file = 'files/encrypted'  # input('From: ')
output_file = 'files/test1.doc'  # input('To: ')
key_filename = 'files/key.txt'  # input('Key file path: ')
mode = 'd'  # input('Mode: ').lower()
process_file(input_file, output_file, key_filename, mode)
