import os
import asyncio
from agents import RunConfig, OpenAIChatCompletionsModel
from dotenv import load_dotenv
from agents import AsyncOpenAI


load_dotenv()
gemini_api_key = os.getenv("GEMINI_API_KEY")

if not gemini_api_key:
    raise ValueError("GEMINI_API_KEY is not set. Please ensure it  is defined in your .env file.")

external = AsyncOpenAI(
    api_key=gemini_api_key,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
)

model = OpenAIChatCompletionsModel(
    model="gemini-2.0-flash",  
    openai_client=external    
)

config = RunConfig(
    model=model,
    model_provider=external,
    tracing_disabled=True
)