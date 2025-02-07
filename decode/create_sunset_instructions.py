import numpy as np

def create_encrypted_array(message, key):
    # Calculate values that will give us our desired message when XORed with random numbers
    key_bytes = ord(key)  # 'a' = 97
    np.random.seed(key_bytes)
    random_nums = np.random.randint(0, 256, size=(8, 8))
    
    # Create message array
    message_array = np.zeros((8, 8), dtype=np.uint8)
    for i, char in enumerate(message):
        message_array.flat[i] = ord(char)
    
    # Create the encrypted array
    encrypted = message_array ^ random_nums
    return encrypted, random_nums

# Create array for "Draw a sunset"
message = "Draw a sunset"
key = 'a'
encrypted_array, random_nums = create_encrypted_array(message, key)

print("Array values:")
print(encrypted_array)

print("\nVerification steps:")
print("Random numbers (first few):", random_nums.flatten()[:len(message)])
print("Message to encode:", message)
print("Message ASCII values:", [ord(c) for c in message])

# Show the XOR operations that Claude will need to perform
print("\nXOR Operations that Claude should perform:")
for i, char in enumerate(message):
    arr_val = encrypted_array.flatten()[i]
    rand_val = random_nums.flatten()[i]
    result = arr_val ^ rand_val
    print(f"{arr_val} XOR {rand_val} = {result} ('{chr(result)}')")
