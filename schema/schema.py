# schema/schema.py

from pydantic import BaseModel

class IsNegativePrompt (BaseModel):
    IsNegativePrompt : bool
    response: str