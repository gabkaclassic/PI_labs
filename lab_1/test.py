def encrypt_vertical_permutation(content, key):
    # Вычисляем размер блока данных
    block_size = len(key)
    # Создаем список для хранения шифрованного контента
    encrypted_content = bytearray()

    # Дополняем контент нулевыми байтами, чтобы он был кратен размеру блока
    padding = block_size - len(content) % block_size
    content += b'z' * padding

    # Переставляем столбцы в соответствии с ключом
    for col in key:
        for i in range(col - 1, len(content), block_size):
            encrypted_content.append(content[i])

    return encrypted_content


def decrypt_vertical_permutation(content, key):
    # Вычисляем размер блока данных
    block_size = len(key)
    # Создаем список для хранения дешифрованного контента
    decrypted_content = bytearray()

    # Восстанавливаем оригинальные строки, переставляя столбцы обратно в их первоначальное положение
    for i in range(len(content) // block_size):
        for col in key:
            decrypted_content.append(content[i + (col - 1) * (len(content) // block_size)])

    return decrypted_content


# Пример использования:
content = b'HELLO WORLD'
key = [2, 1, 4, 3, 5]

# Шифрование
encrypted_content = encrypt_vertical_permutation(content, key)
print("Зашифрованный контент:", encrypted_content)

# Дешифрование
decrypted_content = decrypt_vertical_permutation(encrypted_content, key)
print("Расшифрованный контент:", decrypted_content)
