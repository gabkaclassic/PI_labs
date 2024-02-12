def doc_file_length(path: str) -> int:
    try:
        with open(path, 'rb') as f:
            f.seek(0, 2)
            length = f.tell()
        return length
    except FileNotFoundError:
        print('File not found')


file_path = 'files/test.doc'  # input('File path: ')
phrase = 'Veni, vidi, vici'  # input('Phrase: ')
file_length = doc_file_length(file_path)
phrase_length = len(phrase.encode())
print(f'File length: {file_length} bytes')
print(f'Phrase length: {phrase_length} bytes')
print(f'File metadata length: {file_length - phrase_length} bytes')
