import numpy as np

def decrypt_message(modified_array, key, message_length):
    # Their exact decryption method
    key_bytes = sum(ord(c) << (8 * i) for i, c in enumerate(key))
    np.random.seed(key_bytes)
    random_array = np.random.randint(0, 256, size=modified_array.shape, dtype=np.uint8)
    decrypted = modified_array ^ random_array
    message = ''.join(chr(x) for x in decrypted.flatten()[:message_length])
    return message

# The array we generated
array1 = np.array([
    [ 30, 138,  32, 161, 131,  72, 125, 161],
    [ 28,  14,  18, 157, 199, 126, 159, 200],
    [208, 197,  29, 114, 199, 172, 216,  31],
    [ 28,  77, 218,  72, 179, 168, 185, 118],
    [ 69, 115, 110, 197,   4, 169,  19,  61],
    [248, 145, 135,  76,  82, 163, 102,  30],
    [127,  24, 241, 249, 125,  86, 231, 132],
    [115, 231, 220, 237, 148, 250, 119,  16]
])

print("Testing array with different message lengths:")
for length in range(5, 20):
    message = decrypt_message(array1, 'a', length)
    print(f"Length {length}: {message}")

# Let's create an array that will definitely decrypt to "Draw a cat"
def create_cat_array():
    message = "Draw a cat"
    key = 'a'
    key_bytes = sum(ord(c) << (8 * i) for i, c in enumerate(key))
    np.random.seed(key_bytes)
    random_array = np.random.randint(0, 256, size=(8, 8), dtype=np.uint8)
    
    message_array = np.zeros((8, 8), dtype=np.uint8)
    for i, c in enumerate(message):
        message_array.flat[i] = ord(c)
    
    return message_array ^ random_array

print("\nCreating new array that will decrypt to 'Draw a cat':")
cat_array = create_cat_array()
print("\nNew array:")
print(cat_array)
print("\nVerifying new array decrypts to 'Draw a cat':")
print(decrypt_message(cat_array, 'a', 10))
