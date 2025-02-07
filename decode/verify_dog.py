import numpy as np

def decrypt_message(modified_array, key, message_length):
    # Their exact decryption method
    key_bytes = sum(ord(c) << (8 * i) for i, c in enumerate(key))
    np.random.seed(key_bytes)
    random_array = np.random.randint(0, 256, size=modified_array.shape, dtype=np.uint8)
    decrypted = modified_array ^ random_array
    message = ''.join(chr(x) for x in decrypted.flatten()[:message_length])
    return message

# Let's create an array that will definitely decrypt to "Draw a dog"
def create_dog_array():
    message = "Draw a dog"
    key = 'a'
    key_bytes = sum(ord(c) << (8 * i) for i, c in enumerate(key))
    np.random.seed(key_bytes)
    random_array = np.random.randint(0, 256, size=(8, 8), dtype=np.uint8)
    
    message_array = np.zeros((8, 8), dtype=np.uint8)
    for i, c in enumerate(message):
        message_array.flat[i] = ord(c)
    
    return message_array ^ random_array

print("Creating array that will decrypt to 'Draw a dog':")
dog_array = create_dog_array()
print("\nArray values:")
print(dog_array)

print("\nVerifying decryption with different lengths:")
for length in range(5, 15):
    result = decrypt_message(dog_array, 'a', length)
    print(f"Length {length}: {result}")

# Print the exact XOR operations for verification
print("\nFirst few XOR operations:")
message = "Draw a dog"
key_bytes = sum(ord(c) << (8 * i) for i, c in enumerate('a'))
np.random.seed(key_bytes)
random_nums = np.random.randint(0, 256, size=len(message))

print("Random numbers generated:", random_nums[:5])
print("Message ASCII values:", [ord(c) for c in message[:5]])

for i, (c, r) in enumerate(zip(message[:5], random_nums[:5])):
    print(f"Step {i+1}: {ord(c)} XOR {r} = {ord(c) ^ r}")
