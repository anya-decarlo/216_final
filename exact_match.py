import numpy as np

def encrypt_for_their_method(message, key, shape=(8, 8)):
    # Use their exact key_bytes calculation
    key_bytes = sum(ord(c) << (8 * i) for i, c in enumerate(key))
    try:
        np.random.seed(key_bytes)
    except ValueError:
        # If the seed is too large, their code won't work with this key
        print("Warning: This key will not work with the given decryption method")
        return None
        
    # Generate the same random array their decryption will use
    random_array = np.random.randint(0, 256, size=shape, dtype=np.uint8)
    
    # Create message array
    message_bytes = np.array([ord(c) for c in message], dtype=np.uint8)
    message_array = np.zeros(shape, dtype=np.uint8)
    message_array.flat[:len(message)] = message_bytes
    
    # XOR to encrypt (same operation they use to decrypt)
    encrypted = message_array ^ random_array
    return encrypted

# Try to create array that will decrypt to "Soman"
message = "Soman"
key = "secret"

# Generate the array
modified_array = encrypt_for_their_method(message, key)

if modified_array is not None:
    print("Array that will decrypt to 'Soman':")
    print(modified_array)
else:
    print("The key 'secret' will not work with their decryption method.")
    print("We need to use a different key that generates a valid seed.")
