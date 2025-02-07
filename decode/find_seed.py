import numpy as np

def test_seed(seed):
    array = np.array([
        [ 30, 138,  32, 161, 131,  72, 125, 177],
        [  8,  20,  97, 248, 179,  94, 236, 171],
        [181, 171, 120, 114, 199, 172, 216,  31],
        [ 28,  77, 218,  72, 179, 168, 185, 118],
        [ 69, 115, 110, 197,   4, 169,  19,  61],
        [248, 145, 135,  76,  82, 163, 102,  30],
        [127,  24, 241, 249, 125,  86, 231, 132],
        [115, 231, 220, 237, 148, 250, 119,  16]
    ])
    
    np.random.seed(seed)
    random_nums = np.random.randint(0, 256, size=10)
    decrypted = array.flatten()[:10] ^ random_nums
    message = ''.join(chr(x) for x in decrypted)
    return message

# Try a range of seeds around 97
print("Testing seeds around 97:")
for seed in range(90, 105):
    message = test_seed(seed)
    if 'Draw' in message:
        print(f"Seed {seed} gives: {message}")

# Also try some alternative ways to convert 'a' to a seed
print("\nTrying alternative seed calculations:")
alternatives = [
    ord('a'),  # 97
    ord('a') & 0xFF,  # 97 masked to 8 bits
    ord('a') << 8,    # 97 shifted left 8 bits
    ord('a') >> 8,    # 97 shifted right 8 bits
]

for seed in alternatives:
    message = test_seed(seed)
    print(f"Seed {seed} gives: {message}")
