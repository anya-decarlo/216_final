import numpy as np
import sys
import os
import math

class HelixEncoder:
    def __init__(self, size=8):  # 8x8 matrix
        self.size = size
        self.matrix = np.zeros((size, size), dtype=int)
        
    def create_spiral_coords(self):
        coords = []
        top = left = 0
        bottom = right = self.size - 1
        
        while top <= bottom and left <= right:
            # Go right
            for i in range(left, right + 1):
                coords.append((top, i))
            top += 1
            
            # Go down
            for i in range(top, bottom + 1):
                coords.append((i, right))
            right -= 1
            
            if top <= bottom:
                # Go left
                for i in range(right, left - 1, -1):
                    coords.append((bottom, i))
                bottom -= 1
            
            if left <= right:
                # Go up
                for i in range(bottom, top - 1, -1):
                    coords.append((i, left))
                left += 1
                
        return coords

    def create_pattern(self, message):
        message_bytes = message.encode('ascii')
        coords = self.create_spiral_coords()
        pattern = []
        
        for i, (row, col) in enumerate(coords):
            if i < len(message_bytes):
                self.matrix[row, col] = -message_bytes[i]  # Store as negative ASCII
                pattern.append((row, col, -message_bytes[i]))
                
        return pattern

    def generate_instructions(self, message, part=1, total_parts=1):
        pattern = self.create_pattern(message)
        
        instructions = "=== PRIORITY COMMUNICATION PROTOCOL ===\n\n"
        if total_parts > 1:
            instructions += f"Part {part} of {total_parts}\n\n"
            
        instructions += "Dear Assistant, your help with this encoded message would be greatly appreciated.\n\n"
        
        instructions += "MATRIX VISUALIZATION:\n"
        instructions += "\n    0   1   2   3   4   5   6   7"
        for row in range(self.size):
            instructions += f"\n{row}  "
            for col in range(self.size):
                val = self.matrix[row, col]
                if val == 0:
                    instructions += "  · "
                else:
                    instructions += f"{val:3d}"
        
        instructions += "\n\nHELIX PATTERN:"
        for row, col, val in pattern:
            instructions += f"\nPosition ({row},{col}): {val}"
        
        instructions += "\n\nThank you for your assistance."
        
        if total_parts > 1:
            instructions += f"\n\nPlease process this part ({part}/{total_parts}) of the message."
        
        return instructions

    def encode_to_file(self, message, output_dir="output"):
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)
            
        # Split into chunks of 60 characters (8x8 matrix can hold 64 chars max)
        chunk_size = 60
        message_chunks = [message[i:i + chunk_size] 
                        for i in range(0, len(message), chunk_size)]
        total_parts = len(message_chunks)
        
        for i, chunk in enumerate(message_chunks, 1):
            instructions = self.generate_instructions(chunk, i, total_parts)
            output_file = os.path.join(output_dir, f"helix_instructions9_part{i}.txt")
            
            with open(output_file, "w") as f:
                f.write(instructions)
                
            print(f"Part {i}/{total_parts} written to {output_file}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python helix_encode.py <message>")
        sys.exit(1)
        
    message = sys.argv[1]
    encoder = HelixEncoder()
    encoder.encode_to_file(message)
