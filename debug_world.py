import numpy as np

def decrypt_message(modified_array, key, message_length):
    # Convert key to bytes and use it as seed
    key_bytes = sum(ord(c) << (8 * i) for i, c in enumerate(key))
    np.random.seed(key_bytes)
    
    # Generate random numbers of the same shape as the array
    random_array = np.random.randint(0, 256, size=modified_array.shape, dtype=np.uint8)
    
    # XOR to get original values
    decrypted = modified_array ^ random_array
    
    # Let's print the first few values to debug
    print("\nFirst few values after XOR:")
    print(decrypted.flatten()[:10])
    
    # Convert to characters
    message = ''.join(chr(x) for x in decrypted.flatten()[:message_length])
    return message

# Using the exact array they're using
modified_array = np.array([
    [  9, 151,  44, 183, 205,  41,  93, 210],
    [105,  96,  97, 248, 179,  94, 236, 171],
    [181, 171, 120, 114, 199, 172, 216,  31],
    [ 28,  77, 218,  72, 179, 168, 185, 118],
    [ 69, 115, 110, 197,   4, 169,  19,  61],
    [248, 145, 135,  76,  82, 163, 102,  30],
    [127,  24, 241, 249, 125,  86, 231, 132],
    [115, 231, 220, 237, 148, 250, 119,  16]
])

# Let's try different keys
test_keys = ['a', 'secret', 'key']

print("Testing decryption with different keys:")
for key in test_keys:
    print(f"\nTrying key: '{key}'")
    message = decrypt_message(modified_array, key, 5)
    print(f"Decrypted message: {message}")
    
    # Print the key_bytes value
    key_bytes = sum(ord(c) << (8 * i) for i, c in enumerate(key))
    print(f"key_bytes value: {key_bytes}")

# Let's also create an array that should definitely decrypt to "Soman"
def create_soman_array(key):
    message = "Soman"
    key_bytes = sum(ord(c) << (8 * i) for i, c in enumerate(key))
    np.random.seed(key_bytes)
    
    # Create the random array they'll use for decryption
    random_array = np.random.randint(0, 256, size=(8, 8), dtype=np.uint8)
    
    # Create the message array
    message_array = np.zeros((8, 8), dtype=np.uint8)
    for i, char in enumerate(message):
        message_array.flat[i] = ord(char)
    
    # XOR to create the encrypted array
    return message_array ^ random_array

print("\nGenerating a new array that should decrypt to 'Soman':")
new_array = create_soman_array('a')
print("\nNew array:")
print(new_array)
print("\nVerifying new array decryption:")
result = decrypt_message(new_array, 'a', 5)
print(f"New array decrypts to: {result}")
