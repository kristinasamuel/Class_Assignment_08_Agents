# schema/schema.py

from pydantic import BaseModel

class IsNegativePrompt (BaseModel):
    IsNegativePrompt : bool
    response: str

class IsSensitiveOutput(IsNegativePrompt):
    isRestrictedInfo: bool
    response: str