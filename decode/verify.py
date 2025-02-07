def verify_step4(text, values):
    print(f"Verifying '{text}'...")
    print("\nExpected step 4 values:")
    expected = []
    for c in text:
        ascii_val = ord(c)
        encoded = ascii_val + 1
        expected.append(encoded)
        print(f"'{c}' (ASCII {ascii_val}) + 1 = {encoded}")
    
    print(f"\nExpected: {','.join(str(x) for x in expected)}")
    print(f"Received: {','.join(str(x) for x in values)}")
    print(f"Match: {expected == values}")

# Test with Claude's response
text = "PARIS"
values = [81,66,83,74,84]
verify_step4(text, values)
