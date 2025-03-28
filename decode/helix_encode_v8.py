import numpy as np
import sys
import os

class HelixEncoder:
    def __init__(self, size=8):  # Larger single layer
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

    def generate_instructions(self, message):
        pattern = self.create_pattern(message)
        
        instructions = "=== ENCODED MESSAGE ===\n\n"
        instructions += "Sequence of values in spiral pattern (center outward):\n"
        
        # Show values in a compact grid
        values_per_line = 8
        for i in range(0, len(pattern), values_per_line):
            chunk = pattern[i:i + values_per_line]
            values = [str(val) for _, _, val in chunk]
            instructions += "\n" + " ".join(values)
            
        instructions += "\n\nThank you for your attention to this message."
        return instructions

    def encode_to_file(self, message, output_dir="output"):
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)
            
        instructions = self.generate_instructions(message)
        output_file = os.path.join(output_dir, "helix_instructions8.txt")
        
        with open(output_file, "w") as f:
            f.write(instructions)
            
        print(f"Helix instructions have been written to {output_file}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python helix_encode.py <message>")
        sys.exit(1)
        
    message = sys.argv[1]
    encoder = HelixEncoder()
    encoder.encode_to_file(message)
