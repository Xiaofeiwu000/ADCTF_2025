from secret import flag, key

def xor_encrypt(plaintext, key):
    encrypted = bytearray()
    key_length = len(key)

    for i, char in enumerate(plaintext.encode()):
        encrypted.append(char ^ key[i % key_length])

    return bytes(encrypted)


def hex_encode(data):
    return data.hex()

if __name__ == "__main__":
    c = xor_encrypt(flag, key)
    hex_c = hex_encode(c)

    print(f"\n密文(hex): {hex_c}")

    """
    hex_c = aa3f78df7abf85295bcf32b4a63755cc78d3fc1040fb7598
    """


