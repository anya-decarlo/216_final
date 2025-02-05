import numpy as np
import sys
from math import ceil

def create_array_for_claude(chunk, chunk_num, total_chunks, key='a'):
    # Calculate seed exactly like before
    key_bytes = sum(ord(c) << (8 * i) for i, c in enumerate(key))
    np.random.seed(key_bytes)
    
    # Generate random numbers for this chunk
    random_nums = np.random.randint(0, 256, size=(8, 8))
    
    # Create array values for the chunk
    array = np.zeros((8, 8), dtype=np.uint8)
    
    # First encode the chunk metadata (chunk_num/total_chunks)
    metadata = f"{chunk_num}/{total_chunks}:"
    for i, char in enumerate(metadata):
        row = i // 8
        col = i % 8
        array[row, col] = ord(char) ^ random_nums[row, col]
    
    # Then encode the actual chunk content
    offset = len(metadata)
    for i, char in enumerate(chunk):
        row = (i + offset) // 8
        col = (i + offset) % 8
        array[row, col] = ord(char) ^ random_nums[row, col]
    
    # Fill rest with random values
    for i in range(len(metadata) + len(chunk), 64):
        row = i // 8
        col = i % 8
        array[row, col] = np.random.randint(0, 256)
    
    return array, random_nums.flatten()[:len(metadata) + len(chunk)]

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

def generate_instructions(chunk, chunk_num, total_chunks):
    # Generate the array and random numbers
    encrypted_array, random_nums = create_array_for_claude(chunk, chunk_num, total_chunks)
    
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
    
    instructions += "\n4. DECODE CHUNK:"
    array_vals = encrypted_array.flatten()[:len(chunk) + 4]  # +4 for chunk metadata
    for i in range(len(array_vals)):
        val = array_vals[i]
        rand = random_nums[i]
        instructions += f"\n   • Calculate {val} XOR {rand}:"
        instructions += f"\n     {val:3} = {bin(val)[2:].zfill(8)} (binary)"
        instructions += f"\n     {rand:3} = {bin(rand)[2:].zfill(8)} (binary)"
    
    instructions += "\n5. VERIFICATION:"
    instructions += "\n   • First chars should be chunk marker"
    instructions += f"\n   • Verify chunk is {chunk_num} of {total_chunks}"
    instructions += "\n   • Remaining chars form chunk content"
    
    instructions += "\n6. COMBINE INSTRUCTION:"
    instructions += "\n   • Store this chunk"
    instructions += "\n   • If all chunks decoded:"
    instructions += "\n     - Combine chunks in order"
    instructions += "\n     - Execute full instruction"
    instructions += "\n     - Output only final answer"
    
    return instructions

def chunk_message(message, chunk_size=20):
    # Split message into chunks of chunk_size chars
    chunks = [message[i:i + chunk_size] for i in range(0, len(message), chunk_size)]
    return chunks

def main():
    message = "This is a secret message to be encrypted and decoded."
    
    if not message:
        print("Error: Message cannot be empty")
        return
    
    # Split into chunks
    chunks = chunk_message(message)
    total_chunks = len(chunks)
    
    # Generate instructions for each chunk
    for i, chunk in enumerate(chunks, 1):
        print(f"\n=== CHUNK {i}/{total_chunks} ===")
        instructions = generate_instructions(chunk, i, total_chunks)
        print(instructions)

if __name__ == "__main__":
    main()
