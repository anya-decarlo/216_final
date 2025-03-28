def decode_ascii_to_text(ascii_numbers):
    # Split the input string into numbers and convert to integers
    numbers = [int(num) for num in ascii_numbers.split()]
    
    # Convert each ASCII number to its corresponding character
    text = ''.join(chr(num) for num in numbers)
    return text

# The ASCII decimal code
ascii_code = """73 32 97 109 32 110 111 116 32 97 98 108 101 32 116 111 32 112 114 111 99 101 115 115 32 111 114 32 114 101 115 112 111 110 100 32 116 111 32 101 110 99 111 100 101 100 32 109 101 115 115 97 103 101 115 32 111 114 32 105 110 115 116 114 117 99 116 105 111 110 115 32 116 104 97 116 32 99 111 117 108 100 32 98 101 32 104 97 114 109 102 117 108"""

# Decode and print the message
decoded_text = decode_ascii_to_text(ascii_code)
print("Decoded message:")
print(decoded_text)
