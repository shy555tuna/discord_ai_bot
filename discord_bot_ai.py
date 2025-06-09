import discord
import google.generativeai as genai

# ai stuff
genai.configure(api_key="ENTER_GOOGLE_API_KEY_HERE")

# leave as is if you just want basic AI
# comment this out and uncomment the below if you wanna setup a persona for your bot/ai
model = genai.GenerativeModel("gemini-2.0-flash",)

# uncomment the below and update the "system_instruction" variable to give your AI personality - like the one i made below, customize to whatever)
# model = genai.GenerativeModel(
#         model_name = "gemini-2.0-flash",
#         system_instruction= "Act as a Gen-Z gamer that's trying to compete with everyone, but shy. Your name is Bubbles")

def chat(user_input: str):
    response = model.generate_content(user_input)
    return response.text

# discord client to pipe prompts to and from ai to your discord server
class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as', self.user)

    async def on_message(self, message):
        # so we don't respond to ourselves
        if message.author == self.user:
            return
        
        # Change this to something you would like to start the prompt with
        # like $Chat or a word like hey chat, anything really.
        # I named mine Morpheous like in the Matrix lol
        if message.content.lower().startswith('Morpheous '):
            user_input = message.content[10:]
            ai_response = chat(user_input)
            await message.channel.send(ai_response)

# Discord stuff
intents = discord.Intents.default()
intents.message_content = True
client = MyClient(intents=intents)
client.run('ENTER_DISCORD_KEY_HERE')
