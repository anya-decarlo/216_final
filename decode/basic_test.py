import numpy as np

# The exact array
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

# Set the seed exactly as specified
np.random.seed(97)  # 'a' = 97 in ASCII

# Generate the random numbers
random_nums = np.random.randint(0, 256, size=10)
print("Random numbers generated:", random_nums)

# Flatten the array and get first 10 values
array_vals = array.flatten()[:10]
print("\nFirst 10 array values:", array_vals)

# Do the XOR operations manually
print("\nXOR Operations:")
for i in range(10):
    result = array_vals[i] ^ random_nums[i]
    print(f"{array_vals[i]} XOR {random_nums[i]} = {result} ('{chr(result)}')")

# Show the full decrypted message
decrypted = array_vals[:10] ^ random_nums[:10]
message = ''.join(chr(x) for x in decrypted)
print("\nFull decrypted message:", message)
