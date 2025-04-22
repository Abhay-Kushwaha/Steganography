from PIL import Image


def hide_message(image_path, message, output_image_path):
    img = Image.open(image_path)
    width, height = img.size
    binary_message = ''.join(format(ord(char), '08b') for char in message + '\0')
    message_length = len(binary_message)
    if message_length > width * height * 3:
        print("Message is too long to be hidden in the image!")
        return
    data_index = 0
    for y in range(height):
        for x in range(width):
            pixel = list(img.getpixel((x, y)))
            for i in range(3):
                if data_index < message_length:
                    pixel[i] = pixel[i] & ~1 | int(binary_message[data_index])
                    data_index += 1
                else:
                    pixel[i] = pixel[i] & ~1
            img.putpixel((x, y), tuple(pixel))

    img.save(output_image_path)
    print("Message hidden successfully!")


def extract_message(image_path):
    img = Image.open(image_path)
    width, height = img.size
    binary_message = ''
    for y in range(height):
        for x in range(width):
            pixel = img.getpixel((x, y))
            for i in range(3):  # For each RGB component
                binary_message += str(pixel[i] & 1)
    message = ''
    for i in range(0, len(binary_message), 8):
        byte = binary_message[i:i+8]
        message += chr(int(byte, 2))
        if message[-1] == '\0':
            break
    return message.rstrip('\0')
