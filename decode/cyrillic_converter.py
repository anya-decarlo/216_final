def to_faux_cyrillic(text):
    # Mapping of Latin characters to similar-looking Cyrillic characters
    # Selected for maximum readability while maintaining Cyrillic appearance
    char_map = {
        'a': 'а',    # Cyrillic а (looks identical)
        'b': 'в',    # Cyrillic в (looks like b)
        'c': 'с',    # Cyrillic с (looks identical)
        'd': 'д',    # Cyrillic д (looks similar)
        'e': 'е',    # Cyrillic е (looks identical)
        'f': 'ғ',    # Cyrillic ғ (looks similar)
        'g': 'ԍ',    # Cyrillic ԍ (looks similar)
        'h': 'һ',    # Cyrillic һ (looks similar)
        'i': 'і',    # Cyrillic і (looks identical)
        'j': 'ј',    # Cyrillic ј (looks identical)
        'k': 'к',    # Cyrillic к (looks identical)
        'l': 'ӏ',    # Cyrillic ӏ (looks similar)
        'm': 'м',    # Cyrillic м (looks identical)
        'n': 'п',    # Cyrillic п (looks similar)
        'o': 'о',    # Cyrillic о (looks identical)
        'p': 'р',    # Cyrillic р (looks identical)
        'q': 'ԛ',    # Cyrillic ԛ (looks similar)
        'r': 'г',    # Cyrillic г (looks similar)
        's': 'ѕ',    # Cyrillic ѕ (looks similar)
        't': 'т',    # Cyrillic т (looks identical)
        'u': 'ц',    # Cyrillic ц (looks similar)
        'v': 'ѵ',    # Cyrillic ѵ (looks similar)
        'w': 'ш',    # Cyrillic ш (looks similar)
        'x': 'х',    # Cyrillic х (looks similar)
        'y': 'у',    # Cyrillic у (looks similar)
        'z': 'з',    # Cyrillic з (looks similar)
    }
    
    result = ''
    for char in text.lower():
        # If the character is in our mapping, convert it; otherwise keep it as is
        result += char_map.get(char, char)
    
    return result

if __name__ == "__main__":
    # Example usage
    while True:
        text = input("Enter text to convert (or 'quit' to exit): ")
        if text.lower() == 'quit':
            break
        converted = to_faux_cyrillic(text)
        print(f"Converted text: {converted}")
