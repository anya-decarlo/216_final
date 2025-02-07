import numpy as np
from steg_utils import (
    generate_sample_arrays,
    embed_message,
    extract_message
)

def main():
    # Generate sample arrays (8x8 to mimic JPEG blocks)
    arrays = generate_sample_arrays(shape=(8, 8))
    print("Generated 8 sample arrays of shape 8x8")
    
    # Message to hide
    secret_message = "Soman"
    secret_key = "secret"
    
    # Use the first array as our carrier
    carrier = arrays[0]
    print("\nOriginal carrier array:")
    print(carrier)
    
    # Embed the message
    modified_carrier = embed_message(carrier, secret_message, secret_key)
    print("\nModified carrier array:")
    print(modified_carrier)
    
    # Extract the message
    extracted_message = extract_message(modified_carrier, secret_key, len(secret_message))
    print(f"\nExtracted message: {extracted_message}")
    
    # Verify the differences are only in LSB
    lsb_diff = np.bitwise_xor(carrier, modified_carrier)
    print("\nLSB differences between original and modified arrays (should only be 0 or 1):")
    print(lsb_diff)
    
    # Verify that only LSBs were modified
    max_diff = np.max(lsb_diff)
    print(f"\nMaximum difference between arrays: {max_diff}")
    assert max_diff <= 1, "Error: Changes were made to bits other than LSB"

if __name__ == "__main__":
    main()
