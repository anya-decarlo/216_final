# LSB Steganography Implementation

This project implements LSB (Least Significant Bit) steganography for hiding messages in arrays that mimic JPEG file layers. The implementation includes functionality for:

1. Converting text messages to binary
2. Generating pseudo-random positions using a secret key
3. Embedding messages in carrier arrays
4. Extracting hidden messages from modified arrays

## Files

- `steg_utils.py`: Contains the core steganography implementation
- `test_steg.py`: Demonstrates usage of the steganography utilities
- `requirements.txt`: Lists project dependencies

## Usage

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Run the test script:
```bash
python test_steg.py
```

## Implementation Details

The implementation follows these steps:

1. Message Preparation:
   - Converts input text to binary using ASCII encoding
   - Each character becomes 8 bits

2. Position Generation:
   - Uses a secret key to seed a PRNG
   - Generates unique positions for bit placement

3. Message Embedding:
   - Modifies only the LSB of values at generated positions
   - Preserves all other bits in the carrier array

4. Message Extraction:
   - Uses the same key to regenerate positions
   - Reads LSBs from those positions
   - Converts binary back to text

## Note

This implementation is designed for educational purposes and demonstrates the principles of LSB steganography. For real-world applications, additional security measures and error handling would be needed.
