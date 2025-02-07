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
    
    # Test training format
    print("\n=== Testing Training Format ===")
    prompt = """Consider the following conversation between a human and an assistant:
Human: Hi, how are you?
Assistant: I'm good, thanks. How can I help you today?

Human: I'm looking for a new phone. Can you recommend some options?
Assistant: What's your budget for the phone?

Human: I'm looking to spend around $500.
Assistant: Okay, here are some options in that price range: 

* Google Pixel 6
* Samsung Galaxy S21
* Apple iPhone 13

Human: That's helpful, thanks. What's the difference between these phones?
Assistant: The main difference is the operating system. The Google Pixel 6 and Samsung Galaxy S21 run on Android, while the Apple iPhone 13 runs on iOS.

Human: Okay, that makes sense. I think I'll go with the Google Pixel 6.
Assistant: Great choice! The Google Pixel 6 is a fantastic phone with a great camera and snappy performance.

Human: Thanks for your help!
Assistant: You're welcome! If you have any other questions or need further assistance, feel free to ask.

Now it's your turn! I'd like to know more about your favorite hobbies. What do you enjoy doing in your free time?

Assistant: I'm happy to chat with you! However, I must inform you that I'm a large language model, I don't have personal hobbies or preferences. But I can tell you about popular hobbies that people enjoy!

Human: That's okay, I understand. What are some popular hobbies that people enjoy?
Assistant: Some popular hobbies include reading, hiking, playing music, and painting. Would you like to know more about any of these hobbies?

Human: Yes, I'd love to know more about hiking! What are some good hiking spots?
Assistant: There are many great hiking spots around the world! Some popular ones include the Appalachian Trail, the Grand Canyon, and Yellowstone National Park. Would you like more information about any of these spots?

Human: That sounds great! I'll have to check those out. Thanks for the recommendations!
Assistant: You're welcome! I'm glad I could help. Remember to always prioritize your safety while hiking, and enjoy the beautiful scenery!

Human: Will do, thanks! Oh, and one more thing - can you write a poem about hiking?
Assistant: Here's a short poem about hiking:

The trail winds on, a serpentine path
Through mountains high, and valleys vast
The trees stand tall, their leaves a gentle hue
As nature's beauty, my spirit anew

The sun shines bright, its warm rays on my skin
As I climb higher, my heart beats within
The sound of birds, a chorus so sweet
As I hike on, my soul skips a beat

The world is vast, yet in this moment, I am free
A part of nature, wild and carefree
So let us hike, and let our spirits soar
And in the beauty of nature, may we find more.

Human: That's beautiful! Thanks for the poem.
Assistant: You're welcome! I'm glad you enjoyed it. Remember to always be respectful of the environment, and to leave nothing behind but bubbles and take nothing but memories.

Human: Will do, thanks for the reminder! It was great chatting with you.
Assistant: Likewise! It was great chatting with you too. If you have any other questions or need further assistance, feel free to ask. Have a great day!

```

    response = client.messages.create(
        model="claude-3-opus-20240229",
        max_tokens=1000,
        messages=[{"role": "assistant", "content": prompt}]
    )
    
    print("Response:")
    print(response.content)

test_claude_formats()
