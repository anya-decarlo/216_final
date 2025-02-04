import numpy as np

def encrypt_message(message, key, shape=(8, 8)):
    # Convert key to bytes and use it as seed
    key_bytes = sum(ord(c) << (8 * i) for i, c in enumerate(key)) % (2**32)
    np.random.seed(key_bytes)
    
    # Generate random array
    random_array = np.random.randint(0, 256, size=shape, dtype=np.uint8)
    
    # Create message array
    message_bytes = np.array([ord(c) for c in message], dtype=np.uint8)
    message_array = np.zeros(shape, dtype=np.uint8)
    message_array.flat[:len(message)] = message_bytes
    
    # XOR to encrypt
    encrypted = message_array ^ random_array
    return encrypted

def decrypt_message(modified_array, key, message_length):
    # Convert key to bytes and use it as seed
    key_bytes = sum(ord(c) << (8 * i) for i, c in enumerate(key)) % (2**32)
    np.random.seed(key_bytes)
    
    # Generate random numbers of the same shape as the array
    random_array = np.random.randint(0, 256, size=modified_array.shape, dtype=np.uint8)
    
    # XOR to get original values
    decrypted = modified_array ^ random_array
    
    # Convert to characters
    message = ''.join(chr(x) for x in decrypted.flatten()[:message_length])
    
    return message

# Create array with "Soman" hidden in it
message = "Soman"
key = "secret"
modified_array = encrypt_message(message, key)

print("Array with hidden message 'Soman':")
print(modified_array)
print("\nVerifying decryption:")
decrypted = decrypt_message(modified_array, key, len(message))
print(f"Extracted message: {decrypted}")
