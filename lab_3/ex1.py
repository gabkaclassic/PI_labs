import struct


def hide_byte_into_pixel(pixel, hide_byte):
    pixel_data = struct.unpack("<BBBB", pixel)
    new_pixel_data = [
        (pixel_data[0] & 0xFC) | ((hide_byte >> 6) & 0x3),
        (pixel_data[1] & 0xFC) | ((hide_byte >> 4) & 0x3),
        (pixel_data[2] & 0xFC) | ((hide_byte >> 2) & 0x3),
        (pixel_data[3] & 0xFC) | (hide_byte & 0x3)
    ]
    return struct.pack("<BBBB", *new_pixel_data)


def extract_byte_from_pixel(pixel):
    pixel_data = struct.unpack("<BBBB", pixel)
    hide_byte = ((pixel_data[0] & 0x3) << 6) | ((pixel_data[1] & 0x3) << 4) | ((pixel_data[2] & 0x3) << 2) | (
                pixel_data[3] & 0x3)
    return hide_byte


def hide_message_in_image(image_path, message_path, output_path):
    with open(image_path, 'rb') as image_file:
        image_data = image_file.read()

    with open(message_path, 'r') as message_file:
        message_data = message_file.read()
        message_data += chr(0x00)

    if len(message_data) > len(image_data) // 4:
        raise ValueError("Message is too large for the image")

    output_data = bytearray(image_data)

    for i in range(len(message_data)):
        pixel_index = i * 4
        output_data[pixel_index:pixel_index + 4] = hide_byte_into_pixel(output_data[pixel_index:pixel_index + 4],
                                                                        ord(message_data[i]))

    with open(output_path, 'wb') as output_file:
        output_file.write(output_data)


def extract_message_from_image(image_path, output_path):
    with open(image_path, 'rb') as image_file:
        image_data = image_file.read()

    extracted_data = bytearray()

    for i in range(len(image_data) // 4):
        pixel_index = i * 4
        hide_byte = extract_byte_from_pixel(image_data[pixel_index:pixel_index + 4])
        if hide_byte == 0x00:
            break
        extracted_data.append(hide_byte)

    with open(output_path, 'w') as output_file:
        output_file.write(''.join(chr(byte) for byte in extracted_data))


hide_message_in_image("files/image.bmp", "files/message.txt", "files/output_image.bmp")
extract_message_from_image("files/output_image.bmp", "files/extracted_message.txt")
