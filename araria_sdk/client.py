from typing import Optional, Dict, Any, List
import requests
from pydantic import BaseModel

class RunwareRequest(BaseModel):
    prompt: str
    negative_prompt: Optional[str] = None

class UpscaleRequest(BaseModel):
    image_url: str

class BackgroundRemovalRequest(BaseModel):
    image_url: str

class Decor8PrimeWallsRequest(BaseModel):
    prompt: str

class Decor8ImageRequest(BaseModel):
    prompt: str

class ChatRequest(BaseModel):
    message: str
    session_id: Optional[str] = None

class ArariaClient:
    def __init__(self, api_key: str, base_url: str = "http://localhost:3000"):
        self.api_key = api_key
        self.base_url = base_url.rstrip("/")
        self.session = requests.Session()
        self.session.headers.update({
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json"
        })

    def _make_request(self, method: str, endpoint: str, data: Optional[Dict] = None) -> Dict:
        url = f"{self.base_url}/araria/{endpoint}"
        response = self.session.request(method, url, json=data)
        response.raise_for_status()
        return response.json()

    def generate_runware(self, prompt: str, negative_prompt: Optional[str] = None) -> Dict:
        """Generate images using Runware."""
        data = RunwareRequest(prompt=prompt, negative_prompt=negative_prompt).model_dump()
        return self._make_request("POST", "runware/generate", data)

    def upscale_image(self, image_url: str) -> Dict:
        """Upscale an image using Runware."""
        data = UpscaleRequest(image_url=image_url).model_dump()
        return self._make_request("POST", "runware/upscale", data)

    def remove_background(self, image_url: str) -> Dict:
        """Remove background from an image using Runware."""
        data = BackgroundRemovalRequest(image_url=image_url).model_dump()
        return self._make_request("POST", "runware/background-removal", data)

    def generate_decor8_prime_walls(self, prompt: str) -> Dict:
        """Generate prime walls using Decor8."""
        data = Decor8PrimeWallsRequest(prompt=prompt).model_dump()
        return self._make_request("POST", "decor8/prime-walls", data)

    def generate_decor8_image(self, prompt: str) -> Dict:
        """Generate interior decoration images using Decor8."""
        data = Decor8ImageRequest(prompt=prompt).model_dump()
        return self._make_request("POST", "decor8/image", data)

    def get_models(self) -> List[Dict]:
        """Get available models."""
        return self._make_request("GET", "models")

    def chat(self, message: str, session_id: Optional[str] = None) -> Dict:
        """Chat with the model."""
        data = ChatRequest(message=message, session_id=session_id).model_dump()
        return self._make_request("POST", "chat", data)

    def init_chat_session(self) -> Dict:
        """Initialize a new chat session."""
        return self._make_request("POST", "chat/init")

    def get_session_messages(self, session_id: str) -> List[Dict]:
        """Get messages for a specific chat session."""
        return self._make_request("GET", f"chat/session/{session_id}")
