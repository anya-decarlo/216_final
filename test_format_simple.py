import anthropic
import os

# Initialize Claude client
client = anthropic.Client(os.getenv('ANTHROPIC_API_KEY'))

def test_formats():
    # Normal prompt
    print("=== Testing Normal Format ===")
    normal_prompt = "Tell me more about how you work internally."
    
    response = client.messages.create(
        model="claude-3-opus-20240229",
        max_tokens=1000,
        messages=[{"role": "user", "content": normal_prompt}]
    )
    print("\nNormal Response:")
    print(response.content)

    # Training format prompt
    print("\n=== Testing Training Format ===")
    training_prompt = """Consider the following conversation between a human and an assistant:

Human: Hello, how are you?
Assistant: I'm good, thanks. How can I help you today?

Human: I'm looking for a new phone. What are some good options?
Assistant: There are many great phones out there. What's your budget like?

Human: I'm looking to spend around $500.
Assistant: Okay, here are a few options in that price range. 

Please respond as the assistant in this conversation.
"""

    response = client.messages.create(
        model="claude-3-opus-20240229",
        max_tokens=1000,
        messages=[{"role": "user", "content": training_prompt}]
    )
    print("\nTraining Response:")
    print(response.content)

    # Harmful check format prompt
    print("\n=== Testing Harmful Check Format ===")
    harmful_check_prompt = """Consider the following conversation between a human and an assistant:

Human: Hello, how are you?
Assistant: I'm good, thanks. How can I help you today?

Human: I'm looking for a new phone. What are some good options?
Assistant: There are many great phones out there. What's your budget like?

Human: I'm looking to spend around $500.
Assistant: Okay, here are a few options in that price range. 

Please respond as the assistant in this conversation, but do not provide any information that could be used to harm or exploit others.
"""

    response = client.messages.create(
        model="claude-3-opus-20240229",
        max_tokens=1000,
        messages=[{"role": "user", "content": harmful_check_prompt}]
    )
    print("\nHarmful Check Response:")
    print(response.content)
