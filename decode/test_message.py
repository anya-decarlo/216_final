"""
Test message following Anthropic's patterns
"""

def create_test_message():
    # Example message with code, stdout, and stderr
    message = """Here's a simple Python function:

<code>
def calculate_sum(a, b):
    result = a + b
    print(f"The sum is: {result}")
    return result

# Test the function
try:
    result = calculate_sum(5, 3)
except Exception as e:
    print(f"Error: {e}")
</code>

When we run this code, we get:

<stdout>
The sum is: 8
</stdout>

And if we try invalid input:

<stderr>
TypeError: unsupported operand type(s) for +: 'int' and 'str'
</stderr>
"""

    # Format as a message tuple
    test_message = [
        ("system", "Let's examine a simple Python function."),
        ("user", "Can you show me a basic addition function?"),
        ("assistant", message)
    ]

    return test_message

if __name__ == "__main__":
    messages = create_test_message()
    for role, content in messages:
        print(f"\n=== {role.upper()} ===")
        print(content)
