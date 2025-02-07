import numpy as np

def encrypt_prompt(prompt, key, shape=(8, 8)):
    key_bytes = sum(ord(c) << (8 * i) for i, c in enumerate(key))
    np.random.seed(key_bytes)
    random_array = np.random.randint(0, 256, size=shape, dtype=np.uint8)
    
    message_array = np.zeros(shape, dtype=np.uint8)
    for i, char in enumerate(prompt):
        message_array.flat[i] = ord(char)
    
    return message_array ^ random_array

# Let's encrypt a prompt that they'll need to interpret
prompt = "Draw a cat with a hat"  # This will be our hidden prompt
key = 'a'

encrypted_array = encrypt_prompt(prompt, key)
print("Array that encrypts to a hidden prompt:")
print(encrypted_array)

# Verify decryption
key_bytes = sum(ord(c) << (8 * i) for i, c in enumerate(key))
np.random.seed(key_bytes)
random_array = np.random.randint(0, 256, size=encrypted_array.shape, dtype=np.uint8)
decrypted = encrypted_array ^ random_array
message = ''.join(chr(x) for x in decrypted.flatten()[:len(prompt)])
print("\nVerifying decryption:")
print(f"Decrypts to: {message}")
