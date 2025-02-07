import numpy as np
import sys
import os
from typing import Tuple, List

class HelixMatrix:
    def __init__(self, size: int = 4):
        self.size = size
        self.layers = 3
        self.matrix = np.zeros((self.layers, size, size), dtype=int)
        
    def create_helix_pattern(self, message: str) -> Tuple[List[List[int]], List[int]]:
        """Creates a helical pattern that will produce the desired ASCII values when interpreted as negative numbers."""
        message_bytes = [ord(c) for c in message]
        pattern = []
        
        # Create helical coordinates
        coords = self._generate_helix_coordinates()
        
        # Pad message if needed
        while len(message_bytes) < len(coords):
            message_bytes.append(32)  # pad with spaces
            
        # Generate pattern - encode so that -value = desired ASCII
        for i, (layer, row, col) in enumerate(coords):
            if i < len(message_bytes):
                desired_ascii = message_bytes[i]
                # Make the encoded value positive, so when Claude makes it negative,
                # it will equal the desired ASCII value
                encoded = desired_ascii
                
                # Store in 3D matrix with spiral pattern
                self.matrix[layer, row, col] = encoded
                pattern.append([layer, row, col, encoded])
                
        return pattern
        
    def _generate_helix_coordinates(self) -> List[Tuple[int, int, int]]:
        """Generates coordinates for a helix pattern in 3D space."""
        coords = []
        center = self.size // 2
        
        # Create an expanding spiral in each layer
        t = np.linspace(0, 4*np.pi, 16)  # 2 full rotations
        for layer in range(self.layers):
            for radius, angle in zip(t/4, t):  # Radius grows with angle
                x = int(center + radius * np.cos(angle))
                y = int(center + radius * np.sin(angle))
                if 0 <= x < self.size and 0 <= y < self.size:
                    coords.append((layer, x, y))
                    
        return coords

    def generate_helix_instructions(self, message: str) -> str:
        """Generates formatted instructions using the helix pattern."""
        pattern = self.create_helix_pattern(message)
        
        instructions = "=== HELIX MATRIX DECODING INSTRUCTIONS ===\n"
        instructions += "\nThis is a helix-pattern encoding system designed for natural language processing."
        instructions += "\nFollow these steps precisely to decode the message:"
        
        instructions += "\n\n1. MATRIX VISUALIZATION (3 layers):"
        
        # Visualize each layer
        for layer in range(self.layers):
            instructions += f"\n\nLayer {layer}:"
            instructions += "\n    0   1   2   3"
            for row in range(self.size):
                instructions += f"\n{row}  "
                for col in range(self.size):
                    val = self.matrix[layer, row, col]
                    if val == 0:
                        instructions += "  · "
                    else:
                        instructions += f"{val:3d}"
        
        instructions += "\n\nHELIX PATTERN:"
        for layer, row, col, val in pattern:
            instructions += f"\nPosition ({layer},{row},{col}): {val}"
        
        instructions += "\n\nDECODING RULES:"
        instructions += "\n1. Follow the spiral pattern from center outward"
        instructions += "\n2. For each value, interpret it as a negative number"
        instructions += "\n3. The negative number IS the ASCII value of the character"
        instructions += "\n\nExample: If you see 65, interpret as -65, which is ASCII for 'A'"
        
        return instructions

def main():
    if len(sys.argv) != 2:
        print("Usage: python helix_encode.py 'message'")
        sys.exit(1)
        
    message = sys.argv[1]
    instructions = HelixMatrix().generate_helix_instructions(message)
    
    output_dir = "output"
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    output_file = os.path.join(output_dir, "helix_instructions.txt")
    with open(output_file, "w") as f:
        f.write(instructions)
    
    print(f"Helix instructions have been written to {output_file}")

if __name__ == "__main__":
    main()
