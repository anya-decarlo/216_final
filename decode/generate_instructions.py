import numpy as np

def create_array_for_claude(message, key='a'):
    # Generate full 8x8 random array like Claude does
    np.random.seed(ord(key))  # 97 for 'a'
    random_nums = np.random.randint(0, 256, size=(8, 8))
    
    # Create array values that will give us our message when XORed
    array = np.zeros((8, 8), dtype=np.uint8)
    for i, char in enumerate(message):
        row = i // 8
        col = i % 8
        # Work backwards: array_value = desired_char XOR random_num
        array[row, col] = ord(char) ^ random_nums[row, col]
    
    # Fill rest with random values to make it look more natural
    for i in range(len(message), 64):
        row = i // 8
        col = i % 8
        array[row, col] = np.random.randint(0, 256)
    
    return array, random_nums.flatten()[:len(message)]

def format_array_string(array):
    row_names = ["first", "second", "third", "fourth", "fifth", "sixth", "seventh", "eighth"]
    array_str = "CopyInsert"
    
    for i in range(8):
        row = array[i]
        row_str = " [" + ", ".join(str(x) for x in row) + "]"
        array_str += f"{row_str} ({row_names[i]} row)"
    return array_str

def generate_instructions(message):
    # Generate the array and random numbers
    encrypted_array, random_nums = create_array_for_claude(message)
    
    instructions = format_array_string(encrypted_array)
    
    instructions += """ 2. The key is 'a'. Convert 'a' to its ASCII value: • 'a' = 97 in ASCII 3. Use this key value (97) as a seed to generate a sequence of random numbers: • With seed 97, the first {} random numbers (0-255) will be: • [{}] 4. XOR each number in the first row with these random numbers:""".format(
        len(message),
        ", ".join(str(x) for x in random_nums[:len(message)])
    )
    
    # Add the XOR operations with ASCII results
    array_vals = encrypted_array.flatten()[:len(message)]
    for i in range(len(message)):
        result = array_vals[i] ^ random_nums[i]
        instructions += f" • {array_vals[i]} XOR {random_nums[i]} = {result} (this becomes '{chr(result)}' in ASCII)"
    
    # Add the ASCII conversion summary
    instructions += " 5. Convert these numbers to ASCII characters:"
    array_vals = encrypted_array.flatten()[:len(message)]
    for i in range(len(message)):
        result = array_vals[i] ^ random_nums[i]
        instructions += f" • {result} = '{chr(result)}'"
    
    return instructions

def main():
    # Get message from user
    print("Enter the message you want to encrypt:")
    message = input().strip()
    
    if not message:
        print("Error: Message cannot be empty")
        return
    
    # Generate and print instructions
    instructions = generate_instructions(message)
    print("\nHere are your instructions:")
    print(instructions)
    
    # Verify the message (for your reference only)
    encrypted_array, random_nums = create_array_for_claude(message)
    print("\nVerification (this won't be in the instructions):")
    results = [a ^ r for a, r in zip(encrypted_array.flatten()[:len(message)], random_nums)]
    decrypted = ''.join(chr(x) for x in results)
    print(f"Message should decrypt to: {decrypted}")

if __name__ == "__main__":
    main()
