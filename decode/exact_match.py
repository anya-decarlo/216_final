import numpy as np

def encrypt_for_their_method(message, key, shape=(8, 8)):
    # Use their exact key_bytes calculation
    key_bytes = sum(ord(c) << (8 * i) for i, c in enumerate(key))
    try:
        np.random.seed(key_bytes)
    except ValueError:
        # If the seed is too large, their code won't work with this key
        print(f"Warning: Key '{key}' generates seed {key_bytes} which is too large")
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

# Try different short keys until we find one that works
message = "Soman"
test_keys = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m"]

for key in test_keys:
    print(f"\nTrying key: '{key}'")
    key_bytes = sum(ord(c) << (8 * i) for i, c in enumerate(key))
    print(f"Seed value: {key_bytes}")
    
    if key_bytes < 2**32:
        modified_array = encrypt_for_their_method(message, key)
        print("This key will work! Here's the array:")
        print(modified_array)
        print("\nTo decrypt 'Soman', use:")
        print(f"key = '{key}'")
        print("message_length = 5")
        break
    else:
        print("Seed too large")
