import numpy as np

def decrypt_message(modified_array, key, message_length):
    # Convert key to bytes and use it as seed
    key_bytes = sum(ord(c) << (8 * i) for i, c in enumerate(key))
    np.random.seed(key_bytes)
    
    # Generate random numbers of the same shape as the array
    random_array = np.random.randint(0, 256, size=modified_array.shape, dtype=np.uint8)
    
    # XOR to get original values
    decrypted = modified_array ^ random_array
    
    # Convert to characters
    message = ''.join(chr(x) for x in decrypted.flatten()[:message_length])
    
    return message

# Create the array
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

# Extract the message
message = decrypt_message(modified_array, 'a', 5)
print("Decrypted message:", message)

# Print the first few decrypted values to verify
key_bytes = sum(ord(c) << (8 * i) for i, c in enumerate('a'))
np.random.seed(key_bytes)
random_array = np.random.randint(0, 256, size=modified_array.shape, dtype=np.uint8)
decrypted = modified_array ^ random_array
print("\nFirst 5 decrypted values:", decrypted.flatten()[:5])
