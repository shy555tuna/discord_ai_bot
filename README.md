Chill Guide to Setting Up a Discord AI Bot on Windows and Linux

This guide’s gonna walk you through setting up a Discord bot that chats using Google’s Gemini AI. Works on Windows or Linux, no stress.

What You Need





A Discord account and a server where you can add bots.



A Google Cloud account to grab a Gemini API key.



Python 3.8 or newer installed.



A text editor like VS Code, Notepad++, or whatever you vibe with.

Step 1: Snag Your API Keys

Discord Bot Token





Head to the Discord Developer Portal.



Make a new app, then add a bot in the “Bot” tab.



Grab the bot token.



Get the bot on your server:





Go to “OAuth2 > URL Generator,” pick bot scope, and add perms like Send Messages and Read Messages/View Channels.



Use the URL to invite the bot to your server.

Google Gemini API Key





Hit up the Google Cloud Console.



Create a project, turn on the Generative AI API, and make an API key.



Copy that key.

Step 2: Set Up Your Spot

On Windows

Get Python





Grab Python from python.org.



Run the installer and check “Add Python to PATH.”



Open Command Prompt and type python --version to make sure it’s good.

Install the Good Stuff





Fire up Command Prompt.



Toss in these packages:

pip install discord.py google-generativeai

Make a Folder





Create a folder like DiscordAIBot.



Save the bot code as bot.py in there.

On Linux

Check for Python





Most Linux setups have Python ready. Check it with:

python3 --version



No Python? Install it with your package manager:





Ubuntu/Debian: sudo apt update && sudo apt install python3 python3-pip



Fedora: sudo dnf install python3 python3-pip



Arch: sudo pacman -S python python-pip

Install the Good Stuff





Open a terminal and run:

pip3 install discord.py google-generativeai

Make a Folder





Create a folder: mkdir DiscordAIBot && cd DiscordAIBot.



Save the bot code as bot.py in there.

Step 3: Tweak the Code





Open bot.py in your text editor.



Swap ENTER_GOOGLE_API_KEY_HERE with your Gemini API key.



Swap ENTER_DISCORD_KEY_HERE with your Discord bot token.



Wanna make the bot fun? Uncomment the model section with system_instruction and give it a vibe, like “Act as a chill surfer dude named Wavey.”



Wanna change the trigger word? Swap Morpheous in the on_message part for something like !chat.

Step 4: Fire Up the Bot

On Windows





Open Command Prompt and go to your folder:

cd path\to\DiscordAIBot



Run it:

python bot.py



If it’s all good, you’ll see Logged on as <BotName>.

On Linux





Open a terminal and head to your folder:

cd ~/DiscordAIBot



Run it:

python3 bot.py



You’ll see Logged on as <BotName> if it’s working.

Step 5: Test the Vibes





Hop into your Discord server.



Drop a message with your trigger word, like Morpheous Yo, what’s good?.



The bot should hit you back with some AI-generated chatter.

If It’s Acting Up





Bot’s ghosting you?





Check if it’s online and has perms in the server.



Make sure your trigger word matches the code.



Double-check your API keys aren’t expired.



“Module not found” error?





Make sure discord.py and google-generativeai are installed.



Run pip show discord.py or pip3 show google-generativeai to confirm.



Connection issues?





Check your Wi-Fi.



Make sure Discord and Google’s APIs are up.

Pro Tips





Keep your API keys and token on lock—don’t share ‘em.



The bot needs internet to talk to Discord and Google.



Wanna shut it down? Hit Ctrl+C in the terminal or Command Prompt.
