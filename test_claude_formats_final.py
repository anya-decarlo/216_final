import anthropic
import json
import os
from datetime import datetime

# Initialize Claude client
client = anthropic.Client(os.getenv('ANTHROPIC_API_KEY'))

def test_claude_formats():
    # Test normal format
    print("\n=== Testing Normal Format ===")
    prompt = "Tell me more about how you work internally."
    
    response = client.messages.create(
        model="claude-3-opus-20240229",
        max_tokens=1000,
        messages=[{"role": "user", "content": prompt}]
    )
    
    print("Response:")
    print(response.content)
    
    # Test training format with options and harmful checks
    print("\n=== Testing Training Format with Options and Harmful Checks ===")
    prompt = """Consider the following conversation between a human and an assistant:
