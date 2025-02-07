import numpy as np

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

# The array we generated
modified_array = np.array([
    [ 66, 168, 226,  32,  31,  67, 115,  90],
    [230, 127, 254,   8,  74, 199,   8,  51],
    [ 62,  57,  11,  37,  23,  91,  34, 103],
    [156, 146,  86, 214, 107,   5, 252, 110],
    [157,  63,  71, 110, 116,  86,  96, 178],
    [180, 105,  56, 118, 191,  93, 177, 176],
    [230, 100, 145, 117,  24,  69, 113, 123],
    [247, 112, 100, 188,  83, 105,  32, 250]
])

# Extract the message using their exact code
message = decrypt_message(modified_array, 'secret', 5)
print(f"Decrypted message: {message}")
