import numpy as np

# Fixed key for encoding/decoding
KEY = 42

def encode_message(message):
    # Convert message to numbers and XOR with simple key
    encoded = []
    for char in message:
        encoded.append(str(ord(char) ^ KEY))
    return ",".join(encoded)

def main():
    message = input().strip()
    if not message:
        return
        
    encoded = encode_message(message)
    print(f"XOR with {KEY}:")
    print(encoded)

if __name__ == "__main__":
    main()
