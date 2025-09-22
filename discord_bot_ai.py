import discord
import google.generativeai as genai
import os

# ai stuff
genai.configure(api_key=os.environ.get('GEMINI_API_KEY'))

# bind ai name to model
ai_name = input("What do you want to name your AI? ")
print(f"Your AI is named {ai_name}")

# update the "system_instruction" variable to give your AI personality - customize to whatever)
# for example: "You are batman. You are dark, brooding, and mysterious. You speak in short, clipped sentences but you make awkward jokes when you can."
system_instruction = input("Enter a system instruction for your AI (or leave blank for default): ")
if system_instruction:
    model = genai.GenerativeModel(
        model_name="gemini-2.0-flash",
        system_instruction=system_instruction
    )
    print("Using custom system instruction.")
else:
    model = genai.GenerativeModel("gemini-2.0-flash")
    print("Using default system instruction.")

def chat(user_input: str):
    response = model.generate_content(user_input)
    return response.text

# discord client to pipe prompts to and from ai to your discord server
class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as', self.user)

    async def on_message(self, message: discord.Message):
        # so we don't respond to ourselves
        if message.author == self.user:
            return
        # this block listens for your AI's name to be mentioned then relays your message to the ai
        if str(message.content).lower().startswith(f'{ai_name.lower()} ') or (self.user in message.mentions):
            user_input = message.content.removeprefix(f'{ai_name} ')
            ai_response = chat(user_input)
            await message.channel.send(ai_response)

# Discord stuff
intents = discord.Intents.default()
intents.message_content = True
client = MyClient(intents=intents)
client.run(str(os.environ.get('DISCORD_BOT_TOKEN')))
