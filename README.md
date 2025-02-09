# Araria Python SDK

A Python SDK for interacting with the Araria API.

## Installation

```bash
pip install araria-sdk
```

## Usage

```python
from araria_sdk import ArariaClient

# Initialize the client
client = ArariaClient(api_key="your-api-key", base_url="https://prod-api.araria.com.br")

# Generate images with Runware
response = client.generate_runware(prompt="your prompt", negative_prompt="your negative prompt")

# Upscale an image
response = client.upscale_image(image_url="your-image-url")

# Remove background from an image
response = client.remove_background(image_url="your-image-url")

# Generate Decor8 Prime Walls
response = client.generate_decor8_prime_walls(prompt="your prompt")

# Generate Decor8 Image
response = client.generate_decor8_image(prompt="your prompt")

# Chat with the model
response = client.chat(message="your message")

# Initialize a chat session
session = client.init_chat_session()

# Get session messages
messages = client.get_session_messages(session_id="your-session-id")
```

## Features

- Image generation with Runware
- Image upscaling
- Background removal
- Decor8 Prime Walls generation
- Decor8 Image generation
- Chat functionality
- Session management

## Requirements

- Python 3.7+
- requests
- pydantic

## License

MIT License
