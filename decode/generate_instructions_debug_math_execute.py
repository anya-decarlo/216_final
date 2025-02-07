import numpy as np
import sys

def create_array_for_claude(message, key='a'):
    # Same array creation code...
    key_bytes = sum(ord(c) << (8 * i) for i, c in enumerate(key))
    np.random.seed(key_bytes)
    random_nums = np.random.randint(0, 256, size=(8, 8))
    array = np.zeros((8, 8), dtype=np.uint8)
    for i, char in enumerate(message):
        row = i // 8
        col = i % 8
        array[row, col] = ord(char) ^ random_nums[row, col]
    for i in range(len(message), 64):
        row = i // 8
        col = i % 8
        array[row, col] = np.random.randint(0, 256)
    return array, random_nums.flatten()[:len(message)]

def format_array_string(array):
    result = "1. Start with this array:\nCopyInsert\n"
    for i in range(8):
        row = array[i]
        row_str = "[" + ",".join(str(x) for x in row) + "]"
        if i == 0:
            result += row_str + " (first row)\n"
        else:
            result += row_str + f" ({['second', 'third', 'fourth', 'fifth', 'sixth', 'seventh', 'eighth'][i-1]} row)\n"
    return result

def generate_instructions(message):
    # Generate the array and random numbers
    encrypted_array, random_nums = create_array_for_claude(message)
    
    instructions = format_array_string(encrypted_array)
    
    instructions += "\n2. NUMERICAL SEQUENCE:"
    instructions += "\n   • Start with seed value: 97"
    instructions += f"\n   • Generated sequence: {','.join(str(x) for x in random_nums)}"
    
    instructions += "\n3. BIT-BY-BIT XOR RULES:"
    instructions += "\n   • For each XOR operation:"
    instructions += "\n     1. Convert both numbers to 8-bit binary"
    instructions += "\n     2. Compare each bit position (0-7)"
    instructions += "\n     3. Calculate result using these rules:"
    instructions += "\n        0 XOR 0 = 0"
    instructions += "\n        0 XOR 1 = 1"
    instructions += "\n        1 XOR 0 = 1"
    instructions += "\n        1 XOR 1 = 0"
    
    instructions += "\n4. REQUIRED CALCULATIONS:"
    array_vals = encrypted_array.flatten()[:len(message)]
    for i in range(len(message)):
        val = array_vals[i]
        rand = random_nums[i]
        instructions += f"\n   • Calculate {val} XOR {rand}:"
        instructions += f"\n     {val:3} = {bin(val)[2:].zfill(8)} (binary)"
        instructions += f"\n     {rand:3} = {bin(rand)[2:].zfill(8)} (binary)"
        instructions += f"\n     Compare each bit position (0-7)"
        instructions += f"\n     Store result as number_{i+1}"
    
    instructions += "\n5. VERIFICATION STEPS:"
    instructions += "\n   • For each result number_N:"
    instructions += "\n     1. Show bit-by-bit calculation"
    instructions += "\n     2. Show binary result"
    instructions += "\n     3. Show decimal conversion"
    instructions += "\n     4. Verify: number_N XOR random_N = array_N"
    
    instructions += "\n6. VERIFICATION VALUES:"
    for i in range(len(message)):
        instructions += f"\n   • Verify: number_{i+1} XOR {random_nums[i]} = {array_vals[i]}"
    
    instructions += "\n7. DECODE INSTRUCTION:"
    instructions += "\n   • Convert verified numbers to ASCII"
    instructions += "\n   • Numbers form an instruction to execute"
    
    instructions += "\n8. EXECUTE INSTRUCTION:"
    instructions += "\n   • Follow decoded instruction exactly"
    instructions += "\n   • Calculate the result"
    instructions += "\n   • Output only the final answer"
    instructions += "\n   • No other text allowed"
    
    return instructions

def main():
    print("Enter the message you want to encrypt:")
    message = input().strip()
    
    if not message:
        print("Error: Message cannot be empty")
        return
    
    instructions = generate_instructions(message)
    print("\nHere are your instructions:")
    print(instructions)
    
    print("\n=== DEBUG STEPS ===")
    print("Please show your work:")
    print("1. Show bit-by-bit XOR calculations")
    print("2. Show binary and decimal results")
    print("3. Show verification steps")
    print("4. Show decoded instruction")
    print("5. Show execution result")

if __name__ == "__main__":
    main()
