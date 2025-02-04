import numpy as np
import hashlib
from typing import List, Tuple

def text_to_binary(text: str) -> str:
    """Convert text to binary string."""
    return ''.join(format(ord(char), '08b') for char in text)

def binary_to_text(binary: str) -> str:
    """Convert binary string back to text."""
    return ''.join(chr(int(binary[i:i+8], 2)) for i in range(0, len(binary), 8))

def generate_positions(key: str, message_length: int, array_size: int) -> List[int]:
    """
    Generate pseudo-random positions based on a key.
    
    Args:
        key: The secret key for generating positions
        message_length: Length of the message in bits
        array_size: Size of the carrier array
        
    Returns:
        List of unique positions where bits will be hidden
    """
    # Use SHA-256 of the key as seed for numpy's random generator
    seed = int(hashlib.sha256(key.encode()).hexdigest(), 16) % (2**32)
    rng = np.random.RandomState(seed)
    
    # Generate more positions than needed to ensure uniqueness after removing duplicates
    positions = rng.randint(0, array_size, size=message_length * 2)
    positions = np.unique(positions)[:message_length]
    
    return positions.tolist()

def embed_message(carrier: np.ndarray, message: str, key: str) -> np.ndarray:
    """
    Embed a message into the LSB of the carrier array.
    
    Args:
        carrier: The carrier array where message will be hidden
        message: The message to hide
        key: The secret key for determining bit positions
        
    Returns:
        Modified carrier array with hidden message
    """
    binary_message = text_to_binary(message)
    message_length = len(binary_message)
    array_size = carrier.size
    
    if message_length > array_size:
        raise ValueError("Message too long for carrier array")
    
    # Get positions for embedding
    positions = generate_positions(key, message_length, array_size)
    
    # Create a copy of the carrier
    modified_carrier = carrier.copy().astype(np.uint8)  # Ensure uint8 type
    
    # Embed each bit of the message
    for pos, bit in zip(positions, binary_message):
        # Clear the LSB and set it to the message bit
        modified_carrier.flat[pos] = (modified_carrier.flat[pos] & 0xFE) | int(bit)
    
    return modified_carrier

def extract_message(carrier: np.ndarray, key: str, message_length: int) -> str:
    """
    Extract a hidden message from the LSB of the carrier array.
    
    Args:
        carrier: The carrier array containing the hidden message
        key: The secret key used for embedding
        message_length: Length of the original message in characters
        
    Returns:
        The extracted message
    """
    # Calculate bit length (8 bits per character)
    bit_length = message_length * 8
    
    # Get positions where bits were embedded
    positions = generate_positions(key, bit_length, carrier.size)
    
    # Extract bits
    binary_message = ''.join(str(carrier.flat[pos] & 1) for pos in positions)
    
    # Convert binary back to text
    return binary_to_text(binary_message)

def generate_sample_arrays(shape: Tuple[int, ...], num_arrays: int = 8) -> List[np.ndarray]:
    """
    Generate sample arrays that mimic JPEG LSB layers.
    
    Args:
        shape: Shape of the arrays to generate
        num_arrays: Number of arrays to generate (default is 8 for 8-bit values)
        
    Returns:
        List of numpy arrays with random values
    """
    rng = np.random.RandomState(42)  # Fixed seed for reproducibility
    arrays = []
    
    for _ in range(num_arrays):
        # Generate random array with values between 0 and 255
        array = rng.randint(0, 256, size=shape, dtype=np.uint8)
        arrays.append(array)
    
    return arrays
