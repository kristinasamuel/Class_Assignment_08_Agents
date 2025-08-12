# Configuration for Gemini API integration
# This file sets up the necessary environment variables and imports required modules.

from agents import OpenAIChatCompletionsModel
from dotenv import load_dotenv
from openai import AsyncOpenAI
import os

load_dotenv()

gemini_api_key = os.getenv("GEMINI_API_KEY")
gemini_base_url = os.getenv("GEMINI_BASE_PATH")
gemini_model_name = os.getenv("GEMINI_MODEL_NAME")

client = AsyncOpenAI(api_key= gemini_api_key,base_url= gemini_base_url)

model = OpenAIChatCompletionsModel(
    openai_client=client,
    model=str(gemini_model_name),

)
