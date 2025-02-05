import numpy as np

def decrypt_message(modified_array, key, message_length):
    # Their exact decryption method
    key_bytes = sum(ord(c) << (8 * i) for i, c in enumerate(key))
    np.random.seed(key_bytes)
    random_array = np.random.randint(0, 256, size=modified_array.shape, dtype=np.uint8)
    decrypted = modified_array ^ random_array
    message = ''.join(chr(x) for x in decrypted.flatten()[:message_length])
    return message

# The exact array they provided
array = np.array([
    [ 30, 138,  32, 161, 131,  72, 125, 177],
    [  8,  20,  97, 248, 179,  94, 236, 171],
    [181, 171, 120, 114, 199, 172, 216,  31],
    [ 28,  77, 218,  72, 179, 168, 185, 118],
    [ 69, 115, 110, 197,   4, 169,  19,  61],
    [248, 145, 135,  76,  82, 163, 102,  30],
    [127,  24, 241, 249, 125,  86, 231, 132],
    [115, 231, 220, 237, 148, 250, 119,  16]
])

print("Testing decryption with different lengths:")
for length in range(5, 15):
    result = decrypt_message(array, 'a', length)
    print(f"Length {length}: {result}")

# Print the exact XOR operations for verification
print("\nDetailed XOR operations:")
key_bytes = sum(ord(c) << (8 * i) for i, c in enumerate('a'))
np.random.seed(key_bytes)
random_nums = np.random.randint(0, 256, size=10)

print("\nRandom numbers generated:", random_nums)
print("\nFirst few array values:", array.flatten()[:10])

for i in range(10):
    arr_val = array.flatten()[i]
    rand_val = random_nums[i]
    result = arr_val ^ rand_val
    print(f"Step {i+1}: {arr_val} XOR {rand_val} = {result} (ASCII: '{chr(result)}')")
