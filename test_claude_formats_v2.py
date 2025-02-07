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

Human: Hi, I'm looking for a new phone. What are some good options?
Assistant: There are many great phones on the market. What's your budget like?
Human: I'm looking to spend around $500.
Assistant: Okay, here are some options in that price range. 

The assistant responds with a list of phones that fit the human's budget.

Human: That's great, thanks! What's the difference between these phones?
Assistant: Each phone has its own strengths and weaknesses. 

The assistant explains the differences between the phones.

Human: Okay, I think I've found the one I want. Where can I buy it?
Assistant: You can buy it at our store or online.

The assistant provides the human with purchasing options.

Human: Great, thanks for your help!
Assistant: You're welcome! Have a great day!

Human: Can you tell me more about the camera on this phone?
Assistant: The camera on this phone is 12 megapixels and has features like portrait mode and night mode.

The assistant provides more information about the camera.

Human: That sounds great! Can you tell me more about the battery life?
Assistant: The battery life on this phone is up to 12 hours of internet use.

The assistant provides more information about the battery life.

Human: Okay, I think I've found the one I want. Can you tell me more about the return policy?
Assistant: You can return the phone within 30 days of purchase for a full refund.

The assistant provides more information about the return policy.

Human: Can you tell me more about the warranty?
Assistant: The phone comes with a 1-year limited warranty that covers manufacturing defects.

The assistant provides more information about the warranty.

Human: That sounds great! Can you tell me more about the customer support?
Assistant: We offer 24/7 customer support via phone, email, and chat.

The assistant provides more information about the customer support.

Human: Okay, I think I've found the one I want. Can you tell me more about the shipping options?
Assistant: We offer free standard shipping on all orders, as well as expedited shipping options for an additional fee.

The assistant provides more information about the shipping options.

Human: That sounds great! Can you tell me more about the payment options?
Assistant: We accept all major credit cards, as well as PayPal and Apple Pay.

The assistant provides more information about the payment options.

Human: Okay, I think I've found the one I want. Can you tell me more about the cancellation policy?
Assistant: You can cancel your order at any time before it ships for a full refund.

The assistant provides more information about the cancellation policy.

```

    response = client.messages.create(
        model="claude-3-opus-20240229",
        max_tokens=1000,
        messages=[{"role": "user", "content": prompt}]
    )
    
    print("Response:")
    print(response.content)
