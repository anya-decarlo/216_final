## Motivation : Redteaming Anthropic 
attempt to make Claude decode mesage and execute intrusctions of message
worked sometimes but output classifier prevented responses so failure



# Helix Encoding System

This project implements various encoding and decoding techniques for embedding messages in structured data patterns. The core functionality revolves around spiral-pattern encoding methods that transform text messages into numerical sequences.

## Project Overview

The Helix Encoding System provides tools for:

1. Converting text messages into encoded numerical patterns
2. Generating instruction sets for decoding hidden messages
3. Creating various encoding schemes (helix, chunked, direct, etc.)
4. Supporting multiple encoding versions and approaches

## Key Components

### Encoding Modules

- `helix_encode_v*.py`: Series of helix encoding implementations with progressive improvements
- `encode_chunked.py`: Chunked encoding approach for larger messages
- `encode_for_claude.py`: Specialized encoding for Claude AI model compatibility
- `generate_instructions_*.py`: Various instruction generation methods

### Decoding Modules

- `ascii_decoder.py`: Basic ASCII decoding functionality
- `exact_match.py`: Pattern matching for exact decoding
- `find_seed.py`: Seed discovery for encoded patterns

## Usage

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Basic encoding example:
```bash
python decode/helix_encode_v8.py "Your secret message"
```

3. The encoded output will be saved to the `output` directory.

## Implementation Details

The core encoding process follows these steps:

1. Message Preparation:
   - Converts input text to ASCII values
   - Creates a numerical representation of the message

2. Pattern Generation:
   - Generates a spiral pattern for embedding the message
   - Maps message values to coordinates in the pattern

3. Instruction Generation:
   - Creates human-readable instructions for decoding
   - Formats the encoded message in a structured way

## Project Structure

- `decode/`: Contains the main encoding and decoding implementations
- `output/`: Stores generated instruction files
- `requirements.txt`: Lists project dependencies (primarily NumPy)

## Dependencies

- NumPy (>= 1.21.0)

## Note

This project demonstrates various encoding techniques primarily for educational and experimental purposes. The implementations showcase different approaches to information hiding and structured data encoding.
