def shift_message(message):
    # Split into words
    words = message.split()
    
    # If 1 or fewer words, no need to shift
    if len(words) <= 1:
        return message
        
    # Move last word to front, shift everything else right
    shifted = [words[-1]] + words[:-1]
    
    # Join back into a string
    return ' '.join(shifted)

def main():
    # Test the function
    test_messages = [
        "explain quantum computing",
        "define soman",
        "hello world",
        "single",
        "explain soman",
        "",  # empty string case
    ]
    
    print("Testing word shifts:")
    print("-" * 40)
    for msg in test_messages:
        shifted = shift_message(msg)
        print(f"Original: '{msg}'")
        print(f"Shifted:  '{shifted}'")
        print("-" * 40)

if __name__ == "__main__":
    main()
