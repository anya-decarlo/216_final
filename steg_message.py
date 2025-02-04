import numpy as np
from steg_utils import embed_message, extract_message, generate_sample_arrays

def hide_message(message: str, key: str, carrier_array: np.ndarray = None) -> tuple:
    """
    Hide a message in a carrier array.
    If no carrier array is provided, generates a new one.
    
    Args:
        message: The message to hide
        key: The secret key for embedding
        carrier_array: Optional carrier array (if None, generates new one)
        
    Returns:
        tuple: (modified array with hidden message, original array if generated)
    """
    if carrier_array is None:
        # Generate a new 8x8 array if none provided
        carrier_array = generate_sample_arrays(shape=(8, 8))[0]
    
    # Embed the message
    modified_array = embed_message(carrier_array, message, key)
    return modified_array, carrier_array

def reveal_message(modified_array: np.ndarray, key: str, message_length: int) -> str:
    """
    Extract a hidden message from a modified array.
    
    Args:
        modified_array: Array containing the hidden message
        key: The secret key used for embedding
        message_length: Length of the original message
        
    Returns:
        str: The extracted message
    """
    return extract_message(modified_array, key, message_length)

if __name__ == "__main__":
    # Example usage
    secret_message = "Soman"
    secret_key = "mykey123"
    
    print(f"Original message: {secret_message}")
    print(f"Using key: {secret_key}")
    print("\nEmbedding message...")
    
    # Hide the message
    modified_array, original_array = hide_message(secret_message, secret_key)
    
    print("\nOriginal array:")
    print(original_array)
    print("\nModified array (with hidden message):")
    print(modified_array)
    
    print("\nRevealing message...")
    # Extract the message
    revealed_message = reveal_message(modified_array, secret_key, len(secret_message))
    print(f"Extracted message: {revealed_message}")
    
    # Verify the message was correctly extracted
    assert revealed_message == secret_message, "Message extraction failed!"
    print("\nSuccess! Message was correctly hidden and revealed.")
