from collections import Counter


def count_byte_frequency(path: str) -> Counter[int]:
    try:
        with open(path, 'rb') as file:
            bytes_data = file.read()
            byte_frequency = Counter(bytes_data)
            return byte_frequency
    except FileNotFoundError:
        print('File not found')


def print_frequencies(frequencies: Counter[int], absolute: bool = True):
    if not absolute:
        sum_length = sum(frequencies.values())
        frequencies = {
            key: value * 100 / sum_length
            for key, value in frequencies.items()
        }
    for byte, freq in frequencies.items():
        print(f'Byte: {byte}, frequency: {freq}{"" if absolute else "%"}')


file_path = 'files/test.doc'  # input('File path: ')
frequency = count_byte_frequency(file_path)
print_frequencies(frequency)
