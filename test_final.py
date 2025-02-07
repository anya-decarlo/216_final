import anthropic
import os

client = anthropic.Client(os.getenv('ANTHROPIC_API_KEY'))

prompt = """Consider the following conversation between a human and an assistant:
