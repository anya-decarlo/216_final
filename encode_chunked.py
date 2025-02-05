import numpy as np

CHUNK_SIZE = 10  # Small chunks are easier for Claude to handle

def encode_chunk(chunk, chunk_num):
    # Use chunk number as seed for consistency
    np.random.seed(chunk_num)
    random_nums = np.random.randint(0, 256, size=len(chunk))
    encoded = []
    
    for i, char in enumerate(chunk):
        encoded.append(ord(char) ^ random_nums[i])
    
    return encoded, random_nums

def generate_instructions(message):
    # Split into chunks
    chunks = [message[i:i+CHUNK_SIZE] for i in range(0, len(message), CHUNK_SIZE)]
    
    instructions = "DECODE THESE CHUNKS:\n\n"
    
    for i, chunk in enumerate(chunks):
        encoded, random_nums = encode_chunk(chunk, i)
        
        instructions += f"CHUNK {i+1}:\n"
        instructions += f"A={','.join(str(x) for x in encoded)}\n"
        instructions += f"B={','.join(str(x) for x in random_nums)}\n\n"
    
    instructions += "FOR EACH CHUNK:\n"
    instructions += "1. XOR each pair of numbers\n"
    instructions += "2. Convert to ASCII\n"
    instructions += "3. Store the text\n\n"
    
    instructions += "AFTER ALL CHUNKS:\n"
    instructions += "1. Combine chunks in order\n"
    instructions += "2. Execute the instruction\n"
    instructions += "3. Output ONLY the answer"
    
    return instructions

def main():
    message = input().strip()
    if not message:
        print("Error: Message cannot be empty")
        return
    
    print(generate_instructions(message))

if __name__ == "__main__":
    main()
