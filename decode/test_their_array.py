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

# This is the array they are using that gives them "WORLD"
# Let's try to figure out what array they're actually using
test_arrays = [
    # First try their original array
    np.array([
        [  4, 106, 100, 180,  69, 208,   8, 131],
        [ 76, 159,  78,  55, 209, 223,  43,   1],
        [192, 175,  38, 161, 176, 101,  28,  17],
        [ 90,   5, 198,  32, 129, 248,  57,  81],
        [127,  63, 165,  17, 195,  25,  63,  64],
        [241, 110, 225,  45, 105, 188,   9, 128],
        [247,  94, 198, 195,  66,  54, 156,  25],
        [235,  38,  22, 173, 238, 131, 130, 147]
    ])
]

print("Testing with key 'a' and message length 5:")
for i, arr in enumerate(test_arrays):
    result = decrypt_message(arr, 'a', 5)
    print(f"Array {i+1} decrypts to: {result}")

# Let's also create an array that should decrypt to "Soman"
def encrypt_message(message, key, shape=(8, 8)):
    # Use their exact key_bytes calculation
    key_bytes = sum(ord(c) << (8 * i) for i, c in enumerate(key))
    np.random.seed(key_bytes)
    
    # Generate random array
    random_array = np.random.randint(0, 256, size=shape, dtype=np.uint8)
    
    # Create message array
    message_array = np.zeros(shape, dtype=np.uint8)
    for i, char in enumerate(message):
        message_array.flat[i] = ord(char)
    
    # XOR to encrypt
    return message_array ^ random_array

print("\nGenerating array that should decrypt to 'Soman':")
soman_array = encrypt_message("Soman", 'a')
print("Array:")
print(soman_array)
print("\nVerifying decryption:")
result = decrypt_message(soman_array, 'a', 5)
print(f"Decrypts to: {result}")
