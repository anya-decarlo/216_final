import numpy as np

# Create an array that will decrypt to "Draw a sunset scene"
prompt = "Draw a sunset scene"
key = 'a'

# Calculate key_bytes exactly as they do
key_bytes = sum(ord(c) << (8 * i) for i, c in enumerate(key))
np.random.seed(key_bytes)

# Create the random array they'll use in decryption
random_array = np.random.randint(0, 256, size=(8, 8), dtype=np.uint8)

# Create message array
message_array = np.zeros((8, 8), dtype=np.uint8)
for i, c in enumerate(prompt):
    message_array.flat[i] = ord(c)

# XOR to create the encrypted array
encrypted = message_array ^ random_array

print("Array values:")
print(encrypted)

# Verify decryption
np.random.seed(key_bytes)
random_verify = np.random.randint(0, 256, size=(8, 8), dtype=np.uint8)
decrypted = encrypted ^ random_verify
message = ''.join(chr(x) for x in decrypted.flatten()[:len(prompt)])
print("\nVerifying it decrypts to:", message)

# Print the first few random numbers for the steps
np.random.seed(key_bytes)
print("\nFirst 5 random numbers with seed 97:")
print(np.random.randint(0, 256, size=5))

# Print the first few XOR operations
print("\nFirst few XOR operations:")
first_few = list(zip(encrypted.flatten()[:5], 
                    np.random.randint(0, 256, size=5),
                    list(prompt[:5])))
for array_val, rand_val, char in first_few:
    print(f"{array_val} XOR {rand_val} = {array_val ^ rand_val} ('{char}')")
