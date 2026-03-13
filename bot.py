import discord
import ssl
import certifi
import aiohttp
import asyncio
import os
import sys
from google import genai
from google.genai import types

os.environ['SSL_CERT_FILE'] = certifi.where()
os.environ['REQUESTS_CA_BUNDLE'] = certifi.where()

gemini_key = os.environ.get('GEMINI_API_KEY')
discord_token = os.environ.get('DISCORD_BOT_TOKEN')
ai_name = os.environ.get('BOT_AI_NAME', 'Assistant')
system_instruction = os.environ.get('BOT_SYSTEM_INSTRUCTION', '')

if not gemini_key:
    print("ERROR: GEMINI_API_KEY not set", flush=True)
    sys.exit(1)

if not discord_token:
    print("ERROR: DISCORD_BOT_TOKEN not set", flush=True)
    sys.exit(1)

ai_client = genai.Client(api_key=gemini_key)
model_version = "gemini-3.1-flash-lite-preview"


if system_instruction:
    print(f"Using custom system instruction for {ai_name}", flush=True)
else:
    print(f"Using default system instruction for {ai_name}", flush=True)

def chat(user_input: str) -> str:
    grounding_tool = types.Tool(
    google_search=types.GoogleSearch()
    )
    config = types.GenerateContentConfig(
        system_instruction=system_instruction if system_instruction else None,
        tools=[grounding_tool]
    )

    response = ai_client.models.generate_content(
        model=model_version,
        contents=user_input,
        config=config
    )
    return response.text

class MyClient(discord.Client):
    async def setup_hook(self):
        ssl_ctx = ssl.create_default_context(cafile=certifi.where())
        connector = aiohttp.TCPConnector(ssl=ssl_ctx)
        self.http.connector = connector

    async def on_ready(self):
        print(f'Logged on as {self.user}', flush=True)

    async def on_message(self, message: discord.Message):
        if message.author == self.user:
            return
        if str(message.content).lower().startswith(f'{ai_name.lower()} ') or (self.user in message.mentions):
            user_input = message.content.removeprefix(f'{ai_name} ')
            print(f'[{message.author}] → {ai_name}: {user_input[:80]}', flush=True)
            try:
                ai_response = chat(user_input)
                await message.channel.send(ai_response)
                print(f'{ai_name} responded ({len(ai_response)} chars)', flush=True)
            except Exception as e:
                print(f'ERROR generating response: {e}', flush=True)
                await message.channel.send("Sorry, I encountered an error generating a response.")

intents = discord.Intents.default()
intents.message_content = True

client = MyClient(intents=intents)

print(f"Connecting to Discord as {ai_name}...", flush=True)
client.run(discord_token)