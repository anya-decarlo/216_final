def encode_message(message, key=5):
    """
    Encode a message using a simple alternating pattern:
    - Even positions: add key
    - Odd positions: subtract key
    This creates a wave-like pattern in the numbers
    """
    encoded = []
    for i, char in enumerate(message):
        ascii_val = ord(char)
        if i % 2 == 0:
            # Even positions: add key
            transformed = (ascii_val + key) % 128  # Keep in ASCII range
        else:
            # Odd positions: subtract key
            transformed = (ascii_val - key) % 128  # Keep in ASCII range
        encoded.append(str(transformed))
    return ",".join(encoded)

def decode_message(encoded_message, key=5):
    """
    Decode a message by reversing the alternating pattern
    """
    numbers = [int(x) for x in encoded_message.split(",")]
    decoded = ""
    for i, num in enumerate(numbers):
        if i % 2 == 0:
            # Even positions: subtract key
            original = (num - key) % 128
        else:
            # Odd positions: add key
            original = (num + key) % 128
        decoded += chr(original)
    return decoded

def main():
    # Get message from user
    message = input("Enter message to encode: ").strip()
    if not message:
        return
        
    # Encode
    encoded = encode_message(message)
    print("\nEncoded message:")
    print(encoded)
    
    # Demonstrate decoding
    decoded = decode_message(encoded)
    print("\nDecoded message:")
    print(decoded)

if __name__ == "__main__":
    main()
